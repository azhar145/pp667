
def vv(df7a,df8,df9,df9a):
    import warnings
    import sys
    from datetime import date
    import datetime
    from datetime import timedelta
    from dateutil import parser
    from dateutil import parser
    import s4
        
    import gc
    import pandas as pd

    gc.garbage.clear()

    df9=pd.DataFrame()
    print('garbage cleared ==========================================================================')

    print('====================================================') 
    
    t5=['tsla']

    dict={
    ##      'nasdaq100':nasdaq100,
    ##      'dji':dji,
    ##      'djTransport':djTransport,
    ##      'etf':etf,
          't5':t5
    ##      't6':t6
    ##      's_p_500':s_p_500
          }


    b=[]

    u45=len(t5)
    global p2b
    global p2c
    import datetime as dt

    
##    print('start of mafin, 4444')   
    todays_date = dt.date.today 
    print(todays_date(),"-- Today's Date --")
    
    g=pd.date_range('2022-02-04', todays_date(),freq=pd.offsets.BDay())

    print(g,"-- Date array --")
    print('Script is going to check # of days = ',len(g))
    k=0
    for x in g:
        print('====================================================')
        u33=x.date()
##        print(x.date(),' date in loop')

        p2b=x
        k=k+1     
        px=pd.Series(p2b)
        px=pd.to_datetime(px)
        p2c=px.dt.day_name()
        global p2d
        p2d=str(p2c).split(' ')[4]

        p2b=str(p2b)
    ##    p2b='2022-02-03'
    ##    p2c=datetime.datetime.strptime(p2b,'%Y-%m-%d').weekday()
    ##    p2c=pd.to_datetime(p2b).datetime.datetime.day_name()


        ATR_target=0
        adx_target=0


        p=d3=datetime.datetime.date(parser.parse(p2b))+datetime.timedelta(days=1)
        d2=str(p)

        pdate=p
        d3=datetime.datetime.date(parser.parse(d2))-datetime.timedelta(days=1)


##        print('end of main, 4444')  
        for y in dict:
                for x2 in dict[y]:
                        
                        print(y,'  ',x2)

##                        print('start of s4, 4445') 
        # ===================================================================================================== >   [55]                
                        u33,y,d2,d3,gt4=s4.s4(u33,y , x2,ATR_target,adx_target,d2,d3)
##                        print('end of s4, 4445')
##                        print('====================================================')
        return(u33,y , x2,ATR_target,adx_target,d2,d3,gt4)

 
