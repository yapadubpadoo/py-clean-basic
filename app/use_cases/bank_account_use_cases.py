class BankAccountUseCases:
    def __init__(self, bank_account_repo, saving_interest_calculator):
        self.bank_account_repo = bank_account_repo
        self.saving_interest_calculator = saving_interest_calculator

    def update_saving_account_with_saving_interest(self, account_id):
        saving_account = self.bank_account_repo.get_by_account_id(account_id)
        current_balance = saving_account.get_balance()
        interest = self.saving_interest_calculator.calculate_interest_from_balance(
            current_balance)
        saving_account.set_balance(current_balance+interest)
        self.bank_account_repo.update(saving_account)

    def create_new_saving_account(self, name, lastname, initial_balance):
        return self.bank_account_repo.create(name, lastname, initial_balance)
