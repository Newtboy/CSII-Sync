class Account:
    def __init__(self, name: str, balance: float = 0.0):
        self.__account_name = name
        self.__account_bal = max(0.0, balance)

    def deposit(self, amt: float) -> bool:
        if amt <= 0:
            return False

        self.__account_bal += amt
        return True

    def withdraw(self, amt: float) -> bool:
        if amt <= 0 or amt > self.__account_bal:
            return False

        self.__account_bal -= amt
        return True

    def get_balance(self) -> float:
        return self.__account_bal

    def get_name(self) -> str:
        return self.__account_name

    def set_balance(self, amt: float):
        self.__account_bal = max(0.0, amt)

    def set_name(self, name: str):
        self.__account_name = name

    def __str__(self):
        return (
            f"Account name = {self.get_name()}, "
            f"Account balance = {self.get_balance():.2f}"
        )


# ------------------------------------------------------------ #


class SavingAccount(Account):
    MINIMUM = 100.00
    RATE = 0.20

    def __init__(self, name: str, bal: float = 0.0):
        self.__deposit_count = 0
        super().__init__(name, max(self.MINIMUM, bal))

    def apply_interest(self):
        bal = self.get_balance()
        interest = round(bal * self.RATE, 2)
        self.set_balance(bal + interest)

    def deposit(self, amt: float) -> bool:
        reply = super().deposit(amt)

        if reply:
            self.__deposit_count += 1

            if self.__deposit_count % 5 == 0:
                self.apply_interest()

        return reply

    def set_balance(self, amt: float):
        super().set_balance(max(self.MINIMUM, amt))

    def __str__(self):
        return "SAVING ACCOUNT: " + super().__str__()