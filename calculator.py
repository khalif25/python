def inputnumber(firstnumber,secoundnumber,operator):
    if operator == "+" :
        jogfol = firstnumber + secoundnumber ;
        print(jogfol) ;
    elif operator == "-" :
        biogfol = firstnumber - secoundnumber;
        print(biogfol);
    elif operator == "*" :
        gunfol = firstnumber * secoundnumber ;
        print(gunfol);
    elif operator == "/" :
        if firstnumber > secoundnumber :
            bagfol = firstnumber / secoundnumber ;
            print(round(bagfol,2));
        else:
            bagfol = secoundnumber/firstnumber;
            print(bagfol,2)
    else: print("select correct operator");

inputnumber(1000,20.40,"/");
