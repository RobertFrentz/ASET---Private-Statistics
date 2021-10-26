from BaseUser import BaseUser


class User(BaseUser):

    def request_statistics(self, *args) -> str:
        return "Age, weight and height statistics"
