from app.entities.bank_account import BankAccount


class SavingAccount(BankAccount):
    def __init__(self, account_id, name, lastname, balance):
        self.type = 'Saving'
        self.account_id = account_id
        self.name = name
        self.lastname = lastname
        self.balance = balance

    def get_account_id(self):
        return self.account_id

    def get_account_name(self):
        return f"{self.name} {self.lastname}"

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def can_withdraw(self, amount):
        return 'YES' if self.balance - amount >= 0 else 'NO'

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount
