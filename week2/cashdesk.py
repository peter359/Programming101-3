class Bill:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Money must be positeve number")
        if not isinstance(amount, int):
            raise TypeError("Money must be whole number")
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __lt__(self, other):
        return int(self) < int(other)


class BillBatch:
    def __init__(self, banknotes):
        self.banknotes = banknotes

    def __len__(self):
        return len(self.banknotes)

    def __getitem__(self, index):
        return self.banknotes[index]

    def total(self):
        return sum([int(banknote) for banknote in self.banknotes])


class CashDesk:

    def __init__(self):
        self.money_holder = {}

    def __update_money_holder(self, bill):
        if bill in self.money_holder:
            self.money_holder[bill] += 1
        else:
            self.money_holder[bill] = 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.__update_money_holder(money)
        if(isinstance(money, BillBatch)):
            for bill in money:
                self.__update_money_holder(bill)

    def total(self):
        m = self.money_holder
        return sum([int(bill) * m[bill] for bill in m])

    def inspect(self):
        m = self.money_holder
        print("We have a total of {}$ in the desk".format(self.total()))
        print("We have the following count of bills, sorted in ascending order:")
        bills = [bill for bill in m.keys()]
        bills.sort()
        for bill in bills:
            print("{}$ bills - {}".format(int(bill), m[bill]))
