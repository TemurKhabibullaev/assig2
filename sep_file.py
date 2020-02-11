# Temur Khabibullaev 2/10/2020 This is separate file
# too tired to explain but I know everything what each line does

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
        return ascending_order[int(5 / 2)]

    def mode(self):
        sorting = sorted(self.list)
        x = 0
        if sorting[0] < sorting[1]:
            pass
        elif sorting[0] == sorting[1]:
            x += sorting[0]
        if sorting[1] < sorting[2]:
            pass
        elif sorting[1] == sorting[2]:
            x += sorting[1]
        if sorting[2] < sorting[3]:
            pass
        elif sorting[2] == sorting[3]:
            x += sorting[2]
        if sorting[3] < sorting[4]:
            pass
        elif sorting[3] == sorting[4]:
            x += sorting[3]
        if sorting[4] == sorting[4]:
            pass
        return x, ' is a mode of the list'

    def dup(self):
        sorting = sorted(self.list)
        x = 0
        if sorting[0] < sorting[1]:
            pass
        elif sorting[0] == sorting[1]:
            x += sorting[0]
        if sorting[1] < sorting[2]:
            pass
        elif sorting[1] == sorting[2]:
            x += sorting[1]
        if sorting[2] < sorting[3]:
            pass
        elif sorting[2] == sorting[3]:
            x += sorting[2]
        if sorting[3] < sorting[4]:
            pass
        elif sorting[3] == sorting[4]:
            x += sorting[3]
        if sorting[4] == sorting[4]:
            pass

        for f in sorting:
            if x == sorting[0]:
                sorting[0] = ''
                return sorting
                break
            if x == sorting[1]:
                sorting[1] = ''
                return sorting
                break
            if x == sorting[2]:
                sorting[2] = ''
                return sorting
                break
            if x == sorting[3]:
                sorting[3] = ''
                return sorting
                break
            if x == sorting[4]:
                sorting[4] = ''
                return sorting
                break

    def lar(self):
        ascending_order = sorted(self.list)
        return ascending_order[4]

    def sma(self):
        ascending_order = sorted(self.list)
        return ascending_order[0]

    def eve(self):
        ascending_order = sorted(self.list)
        if (ascending_order[0] % 2) == 0:
            print(ascending_order[0], 'is an even number, so say bye to him')
            ascending_order[0] = ''
        if (ascending_order[1] % 2) == 0:
            print(ascending_order[1], 'is an even number, so say bye to him')
            ascending_order[1] = ''
        if (ascending_order[2] % 2) == 0:
            print(ascending_order[2], 'is an even number, so say bye to him')
            ascending_order[2] = ''
        if (ascending_order[3] % 2) == 0:
            print(ascending_order[3], 'is an even number, so say bye to him')
            ascending_order[3] = ''
        if (ascending_order[4] % 2) == 0:
            print(ascending_order[4], 'is an even number, so say bye to him')
            ascending_order[4] = ''
        return ascending_order

    def odd(self):
        ascending_order = sorted(self.list)
        if (ascending_order[0] % 2) != 0:
            print(ascending_order[0], 'is an odd number, so say bye to him')
            ascending_order[0] = ''
        if (ascending_order[1] % 2) != 0:
            print(ascending_order[1], 'is an odd number, so say bye to him')
            ascending_order[1] = ''
        if (ascending_order[2] % 2) != 0:
            print(ascending_order[2], 'is an odd number, so say bye to him')
            ascending_order[2] = ''
        if (ascending_order[3] % 2) != 0:
            print(ascending_order[3], 'is an odd number, so say bye to him')
            ascending_order[3] = ''
        if (ascending_order[4] % 2) != 0:
            print(ascending_order[4], 'is an odd number, so say bye to him')
            ascending_order[4] = ''
        return ascending_order

    def exi(self):
        ascending_order = sorted(self.list)
        num = int(input("What number are you looking for?\n>>>"))
        if num != ascending_order[0] and num != ascending_order[1] and num != ascending_order[2] and num != ascending_order[3] and num != ascending_order[4]:
            return "No, we don\'t know him"
        else:
            return "Yeah, he is with us"

    def sec_lar(self):
        ascending_order = sorted(self.list)
        return ascending_order[3]







