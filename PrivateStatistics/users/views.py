from django.views import View
from django.http import JsonResponse

from users.aspects.users_aspect import users_aspect
from users.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from users.users_helper import UsersHelper


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
