def main():
    num = int(input("Enter a number: "))
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")

    permiss=int(input("you want to Use This Program Again : "))
    print("1.yes")
    print("2.No")
    if permiss == 1 :
          main()
    else:
          exit()

main()
