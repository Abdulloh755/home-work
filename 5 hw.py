class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        try:
            amount = float(input("Введите сумму для добавления: "))
            self._balance += amount
            print(f"Счёт обновлён. Текущий баланс: {self._balance}")
        except ValueError:
            print("Ошибка: введите числовое значение.")

    def _kill(self):
        self._balance = 0
        print("Счёт обнулён.")

    def __jackpot(self):
        self._balance *= 10
        print(f"Джекпот! Ваш баланс теперь: {self._balance}")

    def merge_balance(self, other):
        """Метод объединения балансов с другим клиентом."""
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Ваш новый баланс: {self._balance}")
        else:
            print("Ошибка: необходимо указать объект класса Bank.")

if __name__  == "__main__":
    client1 = Bank("Клиент 1", 100)
    client2 = Bank("Клиент 2", 200)

    client1.moneyX()
    client1._kill()
    client1._Bank__jackpot()
    client1.merge_balance(client2)