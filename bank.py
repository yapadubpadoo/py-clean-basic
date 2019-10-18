import fire
from app.data_provider.json_file_provider import JSONFileProvider
from app.data_provider.account_id_provider import AccountIDProvider
from app.data_provider.bank_account_data_provider import BankAcccountDataProvider
from app.repositories.bank_account_repo import BankAccountRepo
from app.use_cases.bank_account_use_cases import BankAccountUseCases
from app.services.saving_interest_calculator_service import SavingInterestCalculatorService

account_data_provider = JSONFileProvider('./data/accounts.json')
account_id_provider = AccountIDProvider

bank_account_data_provider = BankAcccountDataProvider(account_data_provider)
bank_account_repo = BankAccountRepo(
    bank_account_data_provider, AccountIDProvider)

bank_account_use_cases = BankAccountUseCases(
    bank_account_repo, SavingInterestCalculatorService)


class BankingCommand:
    @staticmethod
    def create_saving_account(name, lastname, initial_balance):
        new_saving_account = bank_account_use_cases.create_new_saving_account(
            name, lastname, initial_balance)
        print(f"New account created({new_saving_account.get_account_id()})")

    @staticmethod
    def update_saving_interest(account_id):
        bank_account_use_cases.update_saving_account_with_saving_interest(
            account_id)


if __name__ == '__main__':
    fire.Fire(BankingCommand)
