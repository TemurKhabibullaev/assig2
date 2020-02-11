#from sep_file
from sep_file import *

while True:
    instance = Engine()
    print("""
Choose option (DIGITS ONLY):
0 EXIT
1 Sort the list
2 Sum of the list
3 Product of the list
4 Mean of the list
5 Median of the list
6 Mode of the list
7 Duplicate removal
8 Largest number in the list
9 Smallest number in the list
10 List without even numbers
11 List without odd numbers
12 Check if your number exists in the list
13 Second largest number""")
    option = int(input(">>>"))
    if option == 1:
        print(instance.sort())
    if option == 2:
        print(instance.sum())
    if option == 3:
        print(instance.product())
    if option == 4:
        print(instance.mean())
    if option == 5:
        print(instance.median())
    if option == 6:
        print(instance.mode())
    if option == 7:
        print(instance.dup())
    if option == 8:
        print(instance.lar())
    if option == 9:
        print(instance.sma())
    if option == 10:
        print(instance.eve())
    if option == 11:
        print(instance.odd())
    if option == 12:
        print(instance.exi())
    if option == 13:
        print(instance.sec_lar())
    if option == 0:
        print("Bye!")
        break

