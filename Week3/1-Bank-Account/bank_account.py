class BankAccount:
    def __init__(self, name, start_balance, currency):
        self.name = str(name)
        self.balance = start_balance
        self.currency = currency
        self.history = []

        if start_balance < 0:
            raise ValueError

        self.history.append("Account was created")

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"
        return message.format(self.name, self.balance, self.currency)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.history.append("Deposited: {}{}".format(self.balance, self.currency))
        return True

    def get_balance(self):
        self.history.append("Balance check -> {}{}".format(self.balance, self.currency))
        return int(self.balance)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        if self.balance - amount < 0:
            return False
        self.balance -= amount
        self.history.append("Withdrawed: {}{}".format(self.balance, self.currency))
        return True

    def __int__(self):
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        if self.balance < amount:
            return False
        self.balance -= amount
        account.balance += amount
        self.history.append("Transfer to {} for {}{}".format(account.name, self.balance, self.currency))
        account.history.append("Transfer from {} for {}{}".format(self.name, self.balance, self.currency))
        return True

    def save_history(self, thing):
        self.history.append(thing)

    def get_history(self):
        return self.history


account = BankAccount("Rado", 0, "$")

print (account)
print(account.deposit(1000))
print (account.get_balance())
print (str(account))
print (int(account))
print (account.get_history())
print (account.withdraw(500))
print (account.get_balance())
print (account.get_history())
print (account.withdraw(1000))
print (account.get_balance())
print (account.get_history())

rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")

print (rado.transfer_to(ivo, 500))
print (rado.get_balance())
print (ivo.get_balance())
print(rado.get_history())
print(ivo.get_history())
