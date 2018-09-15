def mahmud():
    whichnumber = int(input("which number sum of divisor you want ?"))
    sum = 0;
    for i in range (1,whichnumber+1):
        if whichnumber % i == 0:
            sumf = sum + i ;
            sum = sumf
    print(sum)
    print("Start program again?")
    print("1.yes")
    print("2.no")
    permission=int(input("Enter Your Choice Here:"))
    if permission==1:
        mahmud();
    else:
        exit();
mahmud()

