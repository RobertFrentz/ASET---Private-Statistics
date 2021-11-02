from django.views import View
from django.http import JsonResponse
from users.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from users.users_helper import UsersHelper


@method_decorator(csrf_exempt, name='dispatch')
class Users(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        response, success_code = UsersHelper.create_data(data)

        if success_code == -1:
            return JsonResponse({"message": f"{response}"}, status=400)
        else:
            user = User.objects.create(**response)
            return JsonResponse({"message": f"New user added to Users with id: {user.id}"}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
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
