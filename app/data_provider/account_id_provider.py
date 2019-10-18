import uuid


class AccountIDProvider:
    @staticmethod
    def get_next():
        return str(uuid.uuid1())
