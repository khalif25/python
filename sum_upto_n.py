def khalif():
    sum_number = int(input("How any Number you Want To Sum :"))
    strat = 0
    for i in range(1,sum_number+1):
        sum = i +  strat;
        strat=sum;
    print(strat)
    print("You want to Start Again This program ? ")
    print("1.yes")
    print("2.no")
    permission = int(input())
    if permission == 1:
        khalif()
    else:
        exit()
khalif();
