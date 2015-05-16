class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill.".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())

a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a)
str(a)
print(a)
print(a == b)
print(a == c)

money_holder = {}

money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print(money_holder)


class BillBatch:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        bill_count = []
        for bill in self.bills:
            bill_count.append(self.bills[bill])
        return sum(bill_count)

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)


class CashDesk:

    def __init__(self):
        self.money_dict = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self.money_dict.append(int(money))
        elif isinstance(money, BillBatch):
            for bill in money:
                self.money_dict.append(bill)

    def total(self):
        total_money = 0
        for bill in self.money_dict:
            total_money += int(bill)
        return total_money

    def inspect(self):
        inspectation = {}
        for money in self.money_dict:
            if isinstance(money, Bill):
                if money in inspectation:
                    inspectation[money] += 1
                else:
                    inspectation[money] = 1
        print("We have a total of {}$ in the desk".format(self.total()))
        print("We have the following count of bills:")
        return inspectation

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
print(desk.inspect())
