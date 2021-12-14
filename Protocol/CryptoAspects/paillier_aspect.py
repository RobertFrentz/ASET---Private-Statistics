

def paillier_aspect(function):
    def inner(*args):
        print(f"Function {function.__name__} from {args[0].__class__.__name__} called with parameters {args[1:]}")
        response = function(*args)
        print(f"Function returns response {response}")
        return response

    return inner
