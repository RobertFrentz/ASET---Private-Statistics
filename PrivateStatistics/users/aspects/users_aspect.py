import json

from users.hash_generator import HashGenerator


def users_aspect(function):
    def inner(*args):
        user_data = json.loads(args[1].body.decode())
        user_data["password"] = HashGenerator.generate_sha256_hash(user_data["password"])
        print(f"Function {function.__name__} from {args[0].__class__.__name__} called with parameters {user_data}")
        response = function(*args)
        print(f"Function returns response {response.content.decode()} with status code {response.status_code}")
        return response

    return inner
