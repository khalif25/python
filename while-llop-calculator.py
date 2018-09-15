numberOne = int(input("Enter Number One :"))
numberTwo = int(input("Enter Number Two:"))
print("Now what you wnat to do ?")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. Exit")
choice =int(input("enter Your Choice :"))
while choice != 5:
    if choice == 1:
        jog = numberOne + numberTwo;
        print(jog)
    elif choice == 2:
        biog = numberOne - numberTwo;
        print(biog)
    elif choice == 3:
        gun =numberOne * numberTwo;
        print(gun)
    else:
        vag = numberOne/numberTwo;
        print(vag)
    choice = int(input("enter Your Choice :"))
print("thanks For visiting Us")

