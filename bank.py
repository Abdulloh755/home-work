
class Bank:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance


class MyBank(Bank):
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

# bank.py (продолжение)
class AdvancedBank(MyBank):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value

# users.py
from bank import AdvancedBank

user_account = AdvancedBank(1000, 5.5)

# Изменяем значения через property
user_account.balance = 1500
user_account.interest_rate = 4.8

print(f"Баланс: {user_account.balance}")
print(f"Процентная ставка: {user_account.interest_rate}")