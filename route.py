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

# new_saving_account = bank_account_use_cases.create_new_saving_account(
#     name="Nutt", lastname="Yod", initial_balance=500.00)
# print(new_saving_account)

# bank_account_use_cases.update_saving_account_with_saving_interest(
#     account_id="2379cc92-f195-11e9-af52-acde48001122")
