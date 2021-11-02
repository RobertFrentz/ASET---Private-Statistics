from users.models import User


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

        user_data = {
            'username': username,
            'password': password,
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
            'password': password
        }
        return user_data, 1

    @staticmethod
    def check_credentials(login_data):
        user = User.objects.filter(username=login_data['username'], password=login_data['password'])
        if not user.exists():
            return -1
        return 1
