print("Do You Want To Calculate Something Now ?")
print("(1) Yes")
print("(2) No")
yesOrNo=str(input("Enter Your Choice Here (1 or 2): "))
if yesOrNo=="1" :
    # ----------------calculator start-------------------
    print("what Operator You Want To Calculate")
    print("\t (1)Jog")
    print("\t (2)Biog")
    print("\t (3)Gun")
    print("\t (4)Vag")
    print("\t (5)Bagshes")
    choiceOperator = int(input("Enter Your Choice Here (1 or 2 or 3 or 4 or 5):"))

    # =================JOGFOL==================

    if choiceOperator==1:
      how_many_number = int(input("How Many Nummber You want to add : "))
      if how_many_number < 2:
          print("you need at least Two Number For Addition")
      else:
           a = 0
           for i in range(1,how_many_number+1):
               enternumber =  int(input(f"Enter Your {i} number :" ) )
               c = enternumber + a
               a = c
           print(a)

    # =================Biogfol==================

    elif choiceOperator==2:
        biognumber1=int(input("Enter Your First Number : "))
        biognumber2=int(input("Enter Your secound Number : "))
        biogfol = biognumber1 - biognumber2
        print(f"Biogfol :  {biogfol}")


    # =================GUNFOL==================

    elif choiceOperator==3:
       gunsongkha = int(input("How Many Number You Want For Multiplication : "))
       if gunsongkha < 2 :
           print("Enter atleast Two Number for Multipication")
       else:
           count=1;
           for i in range(1,gunsongkha+1):
                gunnumber = int(input(f"Enter Your {i} Number :") )
                Ga = gunnumber * count  ;
                count = Ga;
           print(f"Result : {Ga}")








    # =================BAGFOL==================

    elif choiceOperator==4:
        bagnumber1=int(input("Enter Your First Number : "))
        bagnumber2=int(input("Enter Your secound Number : "))
        bagfol = bagnumber1 / bagnumber2
        print(f"Bagfol :  {bagfol}")





    # =================BAGSHES==================

    elif choiceOperator==5:
        baghshesnumber1=int(input("Enter Your First Number : "))
        baghshesnumber2=int(input("Enter Your secound Number : "))
        if baghshesnumber1 % baghshesnumber2 == 0:
            print("No Bagshes")
            bagshesResult = baghshesnumber1/baghshesnumber2;
            print(f"Bagfol Result : {bagshesResult}")
        else:
            if  baghshesnumber1 > baghshesnumber2 :
             bagshesholebag=int(baghshesnumber1/baghshesnumber2)
             gunkorepai = int(bagshesholebag * baghshesnumber2  )
             bagshesbiiog = baghshesnumber1 - gunkorepai
             print(f"Bagshes: {bagshesbiiog}")
            else:
             print("Bajjo Bajok er thaka choto Hole Dosomik a man asbe")
             dosomiman=  float(baghshesnumber1 / baghshesnumber2 ) ;
             print(f"Dosomik Result : {dosomiman}")

        # ----------------calculator end-------------------




    else:
        print("please Inpur Corrcet Value from (1 or 2 or 3 or 4 or 5)")
        







elif yesOrNo=="2":
        print("Thank you For Visiting Us")
elif yesOrNo== "":
        print("Without Inpur Your Choice You Can Not Calculate Anything")
else:
    print("plese Input correct value")

