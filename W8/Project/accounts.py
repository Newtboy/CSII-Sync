class Account: # {
    def __init__(self, name, bal=0):
        self.__account_name = name
        self.__account_balance = bal
        self.set_balance(bal)


    def deposit(self, amt) -> bool:
        dMon = max(amt, 0)
        self.__account_balance += dMon
        return dMon != 0
    # }
    def withdraw(self, amt) -> bool:
        if (amt > self.__account_balance): # {
            return False;
        # }
        if (amt <= 0): # {
            return False;
        # }
        self.__account_balance -= amt;
        return True;
    # }
    def get_balance(self):
        return self.__account_balance;
    # }
    def get_name(self):
        return self.__account_name;
    # }
    def set_balance(self, val):
        self.__account_balance = max(0, val)
    # }
    def set_name(self, val):
        self.__account_name = val;
    # }
    def __str__(self):
        return f"Account name = {self.__account_name}, Account balance = {self.__account_balance:.2f}"
    # }


class SavingAccount(Account):  # {
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name)
        self.__deposit_count = 0;
        self.set_balance(self.MINIMUM)

    def deposit(self, amt):
        response = super().deposit(amt);
        if ((response)): # {
            self.__deposit_count += 1
        if (self.__deposit_count - 5 == 0):  # {
            self.apply_interest()
            self.__deposit_count = 0;
        return response
    # }
    def apply_interest(self):
        self.set_balance(self.get_balance() * (1+self.RATE))

    def withdraw(self, amt):
        if (self.get_balance() - amt < self.MINIMUM): # {
            return False;
        # }
        return super().withdraw(amt)
    # }
    def get_balance(self):
        return super().get_balance()
    # }
    def get_name(self):
        return super().get_name()
    # }
    def set_balance(self, val):
        super().set_balance(max(val, self.MINIMUM))
    # }
    def set_name(self, val):
        super().set_name(val)
    # }
    def __str__(self):
        return "SAVING ACCOUNT: " + super().__str__();
    # }
