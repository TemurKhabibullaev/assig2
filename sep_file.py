# Temur Khabibullaev 2/10/2020 This is separate file


class Engine:


    def __init__(self):
        self.first = int(input("Give me a first number:\n>>>"))
        self.second = int(input("Give me a second number:\n>>>"))
        self.third = int(input("Give a third number:\n>>>"))
        self.fourth = int(input("Give a fourth number:\n>>>"))
        self.fifth = int(input("Give me a fifth number:\n>>>"))
        self.list = [self.first, self.second, self.third, self.fourth, self.fifth]

    def sort(self):
        return sorted(self.list)

    def sum(self):
        return self.first + self.second + self.third + self.fourth + self.fifth

    def product(self):
        return self.first * self.second * self.third * self.fourth * self.fifth

    def mean(self):
        return (self.first + self.second + self.third + self.fourth + self.fifth) / 5

    def median(self):
        ascending_order = sorted(self.list)
        return ascending_order[2]

    def mode(self):
        new_list = [self.first, self.second, self.third, self.fourth, self.fifth]
        sorting = sorted(new_list)


    def lar(self):
        ascending_order = sorted(self.list)
        return ascending_order[4]

    def sma(self):
        ascending_order = sorted(self.list)
        return ascending_order[0]




