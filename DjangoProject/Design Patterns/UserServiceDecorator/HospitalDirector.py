from BaseUserDecorator import BaseUserDecorator


class HospitalDirector(BaseUserDecorator):

    def request_statistics(self) -> str:
        return f"Blood type statistics and {self._base_user.request_statistics()})"
