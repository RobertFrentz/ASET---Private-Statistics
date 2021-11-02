from BaseUserDecorator import BaseUserDecorator


class SocialWorker(BaseUserDecorator):

    def request_statistics(self) -> str:
        return f"Id card number, social security number and {self._base_user.request_statistics()})"