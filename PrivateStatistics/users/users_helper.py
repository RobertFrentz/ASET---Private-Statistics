from users.email_exceptions import EmailNotValidError
from users.hash_generator import HashGenerator
from users.models import User
import re

from users.password_exceptions import PasswordNotValidError, PasswordTooShortError


class UsersHelper:

    @staticmethod
    def create_data(request_data):
        try:
            username = request_data['username']
        except KeyError:
            return 'Username is required', -1
        try:
            password = request_data['password']
        except KeyError:
            return 'Password is required', -1
        try:
            email = request_data['email']
        except KeyError:
            return 'Email is required', -1
        try:
            UsersHelper.validate_password(request_data)
        except PasswordTooShortError:
            return 'Use 8 characters or more for your password', -1
        except PasswordNotValidError:
            return 'Password must be a mix of letters, numbers, and symbols.', -1
        try:
            UsersHelper.validate_email(request_data)
        except EmailNotValidError:
            return 'Email is not valid', -1

        user_data = {
            'username': username,
            'password': HashGenerator.generate_sha256_hash(password),
            'email': email,
        }
        return user_data, 1

    @staticmethod
    def create_login_data(request_data):
        try:
            username = request_data['username']
        except KeyError:
            return 'Username is required', -1
        try:
            password = request_data['password']
        except KeyError:
            return 'Password is required', -1
        user_data = {
            'username': username,
            'password': HashGenerator.generate_sha256_hash(password)
        }
        return user_data, 1

    @staticmethod
    def check_credentials(login_data):
        user = User.objects.filter(username=login_data['username'], password=login_data['password'])
        if not user.exists():
            return -1
        return 1

    @staticmethod
    def check_existent_mail(request_data):
        user = User.objects.filter(email=request_data['email'])
        if not user.exists():
            return 1
        return -1

    @staticmethod
    def check_existent_username(request_data):
        user = User.objects.filter(username=request_data['username'])
        if not user.exists():
            return 1
        return -1

    @staticmethod
    def validate_password(request_data):
        if len(request_data["password"]) < 8:
            raise PasswordTooShortError
        elif re.fullmatch(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@!#$])[\w\d@#!$]{8,}$", request_data["password"]) is None:
            raise PasswordNotValidError

    @staticmethod
    def validate_email(request_data):
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', request_data["email"]) is None:
            raise EmailNotValidError
