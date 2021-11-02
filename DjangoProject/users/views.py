from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


@method_decorator(csrf_exempt, name='dispatch')
class User(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        user_data = {
            'username': username,
            'password': password,
            'email': email,
        }

        user = User.objects.create(**user_data)

        data = {
            "message": f"New user added to Users with id: {user.id}"
        }
        return JsonResponse(data, status=201)
