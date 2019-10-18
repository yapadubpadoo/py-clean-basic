from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_id, identity_number, name, lastname, balance):
        self.type = None
        self.account_id = account_id
        self.name = name
        self.lastname = lastname
        self.balance = balance
        super().__init__()

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_account_id(self):
        pass

    @abstractmethod
    def get_account_name(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def set_balance(self):
        pass
