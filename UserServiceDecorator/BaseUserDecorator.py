from BaseUser import BaseUser


class BaseUserDecorator(BaseUser):
    _base_user: BaseUser = None

    def __init__(self, base_user: BaseUser) -> None:
        self._base_user = base_user

    @property
    def base_user(self) -> BaseUser:
        return self._base_user

    def request_statistics(self, *args) -> str:
        return self._base_user.request_statistics()
