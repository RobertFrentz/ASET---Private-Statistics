import random

from django.views import View
from django.http import JsonResponse

from Protocol.CriptosSistemPaillier import CriptosistPaillier
from Protocol.StatisticalFunctions import StatisticalFunctions
from users.aspects.users_aspect import users_aspect
from users.dtos.patient_dto import PatientDto
from users.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from users.patients_repository import PatientsRepository
from users.statistics import Statistic
from users.users_helper import UsersHelper

from faker import Faker

from users.file_helper import read_paillier_setup


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):
    @users_aspect
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        response, success_code = UsersHelper.create_data(data)

        if success_code == -1:
            return JsonResponse({"message": f"{response}"}, status=400)
        else:
            email_flag = UsersHelper.check_existent_mail(data)
            username_flag = UsersHelper.check_existent_username(data)
            if email_flag == -1:
                return JsonResponse({'message': 'Email already used'}, status=200)
            elif username_flag == -1:
                return JsonResponse({'message': 'Username already used'}, status=200)
            else:
                user = User.objects.create(**response)
                return JsonResponse({"message": f"New user added to Users with id: {user.id}"}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    @users_aspect
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        response, success_code = UsersHelper.create_login_data(data)
        if success_code == -1:
            return JsonResponse({'message': f'{response}'}, status=400)
        else:
            user_flag = UsersHelper.check_credentials(response)
            if user_flag == -1:
                return JsonResponse({'message': 'Username or password not correct'}, status=200)

        return JsonResponse({}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Statistics(View):
    def post(self):
        pass

    def get(self, request):
        hospitals = request.GET.getlist('hospitals', '')
        patient_attribute = request.GET.get('field', '')
        functions = request.GET.getlist('functions', '')
        response = dict()
        n, g, random_seed, s, shares, delta_patrat = read_paillier_setup()
        obiect = CriptosistPaillier()
        patientsRepository = PatientsRepository()
        patients = patientsRepository.get_patients(hospitals)
        attribute_values, bitlengths = patientsRepository.get_attribute_values(patients, patient_attribute)
        statistic = StatisticalFunctions(attribute_values, n, g, random_seed, s, shares, obiect, delta_patrat, 20)
        if Statistic.Mean.value in functions or len(functions) == 0:
            statistic.l_x = 20
            response["Mean"] = statistic.mean()
        if Statistic.Variance.value in functions or len(functions) == 0:
            response["Variance"] = statistic.variance()
        if Statistic.StandardDeviation.value in functions or len(functions) == 0:
            response["StandardDeviation"] = statistic.standard_deviation()
        if Statistic.StandardError.value in functions or len(functions) == 0:
            response["StandardError"] = statistic.standard_error()
        return JsonResponse(response, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class Patients(View):
    def post(self, request):
        fake_names_generator = Faker()
        hospitals = ["Arcadia", "Spiridon", "Spiru Haret", "Saint Marie"]
        patients = list()
        for patient_count in range(0, 100):
            name = fake_names_generator.name().split(' ')
            first_name, last_name = name[0], name[1]
            age = random.randint(10, 100)
            height = random.randint(100, 200)
            weight = random.randint(50, 120)
            hospital = hospitals[random.randint(0, 3)]
            patient_dto = PatientDto(first_name, last_name, age, weight, height, hospital)
            patients.append(patient_dto)
        patients_repository = PatientsRepository()
        patients_repository.add_patients(patients)


@method_decorator(csrf_exempt, name='dispatch')
class Hospitals(View):
    def get(self, request):
        patients_repository = PatientsRepository()
        response = patients_repository.get_hospitals_attributes()
        return JsonResponse(response, safe=False, status=200)
