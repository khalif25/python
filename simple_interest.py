def lubkoto(munafa,interest,how_years):
    OneYearLUB = (interest * munafa) / 100 ;
    EndYearLub = OneYearLUB *  how_years ;
    totalLUB =  EndYearLub + munafa ;
    print(totalLUB) ;

lubkoto(100000,5,5);

