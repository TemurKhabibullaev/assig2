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
        instance.sort()
    if option == 2:
        instance.sum()
    if option == 3:
        instance.product()
    if option == 4:
        instance.mean()
    if option == 5:
        instance.median()
    if option == 6:
        instance.mode()
    if option == 7:
        instance.dup()
    if option == 8:
        instance.lar()
    if option == 9:
        instance.sma()
    if option == 10:
        instance.eve()
    if option == 11:
        instance.odd()
    if option == 12:
        instance.exi()
    if option == 13:
        instance.sec_lar()
    if option == 0:
        print("Bye!")
        break

