
def s4(u33,y , x2,ATR_target,adx_target,d2,d3):
    import sys
    import time
    import os
    import plotly.graph_objects as go
    import yfinance as yf
    import pandas as pd
    import datetime as dt
    import talib as ta
    import finta as f
    import inspect
    from inspect import currentframe, getframeinfo
    import numpy as np
    import sys,trace
    import random
    import s4

    import warnings
    import sys
    from datetime import date
    import datetime
    from datetime import timedelta
    from dateutil import parser
    from dateutil import parser


    
        
        
        
        


    proxies = [
##        'http://138.197.222.35:80',
##        'http://1138.197.222.35:8080'
    '103.105.49.53:80'
    '167.172.248.53:3128',
    '194.226.34.132:5555',
    '203.202.245.62:80',
    '141.0.70.211:8080',
    '118.69.50.155:80',
    '201.55.164.177:3128',
    '51.15.166.107:3128',
    '91.205.218.64:80',
    '128.199.237.57:8080',
    '206.253.164.146:80', 
    '206.253.164.122:80', 
    '206.253.164.101:80', 
    '69.75.122.146:39593', 
    '103.105.49.53:80', 
    '67.201.33.9:25280', 
    '47.254.89.30:7328', 
    '23.251.138.105:8080', 
    '67.201.33.10:25283', 
    '47.56.69.11:8000', 
    '132.145.103.245:8118', 
    '4.53.28.242:80', 
    '47.242.116.120:59394', 
    '47.242.6.186:59394',
    '65.20.187.60:5678', 
    '65.20.155.226:5678', 
    '159.65.69.186:9200', 
    '65.21.183.114:3232', 
    '54.193.134.2:20030', 
    '165.225.114.76:10605', 
    '138.68.18.219:9050', 
    '47.90.132.228:8081', 
    '47.242.86.153:59394', 
    '193.123.227.220:59394', 
    '161.82.252.35:4153', 
    '35.184.126.42:80', 
    '165.225.124.97:10605', 
    '154.212.5.190:5678', 
    '184.105.134.166:48324', 
    '47.242.158.41:8080', 
    '68.183.130.112:19053', 
    '47.242.5.82:5678', 
    '35.232.186.191:3128'

    ]
    
    proxyb = random.choice(proxies)

    df = yf.download(x2,start=d3,end=d2,interval='1m',auto_adjust = True,threads = True,prepost=True,progress=False, proxies=proxyb)
    df['ticker']=''
    for x in df.index:
        df['ticker'].loc[x]=x2
        
        
##    print(df,x2,' === ',u33,' ===')
    return(u33,y,d2,d3,df)



def bb(df7a,df8,df9,df9a):
    import warnings
    import sys
    from datetime import date
    import datetime
    from datetime import timedelta
    from dateutil import parser
    from dateutil import parser
        
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


        p=datetime.datetime.date(parser.parse(p2b))+datetime.timedelta(days=1)
        d2=str(p)

        pdate=p
        d3=datetime.datetime.date(parser.parse(d2))-datetime.timedelta(days=1)


##        print('end of main, 4444')  
        for y in dict:
                for x2 in dict[y]:
                        
##                        print(y,'  ',x2)

##                        print('start of s4, 4445') 
        # ===================================================================================================== >   [55]                
                        u33,y,d2,d3,gt4=s4(u33,y , x2,ATR_target,adx_target,d2,d3)
##                        print('end of s4, 4445')
##                        print('====================================================')
                        
##        print('====================================================') 



##        print(" s4 ")
##        print('s4 input [u33,y , x2,ATR_target,adx_target,d2,d3]', u33,y , x2,ATR_target,adx_target,d2,d3)
##        print('s4 output [u33,y,d2,d3,gt4]',u33,y,d2,d3,gt4)
##        print(" s4 ")
##        print('\n\n\n')
        return(u33,y,d2,d3,gt4)




'''    
        u33,dfd=s5c(u33,y,d2,d3,gt4)


##        print(" s5c ")
##        print('s5c input [u33,y,d2,d3,gt4]', u33,y,d2,d3,gt4)
##        print('s5c output [u33,dfd] ',u33,dfd)
##        print(" s5c ")
##        print('\n\n\n')

##        df7a=pd.DataFrame(columns=['stragety','Date','ticker','Buy_at','Sell_at','Profit','b_Close_vwap','b_macd','b_mom','b_VZO','b_CCI'])
##        print('\n\n\n\n\n')
##        print(df7a,' -------------------------------------------------------------- before')


        df=dfd
##        print(dfd,'input to s6')
        df,df7=s6(df,u33,df7a)
##
##        if df7a==empty:
##   
##            s5d={'stragety':'-1','Date':str(u33),'ticker':s45,'Buy_at':'50','Sell_at':'50','Profit':0,\
##             'b_Close_vwap':'55','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}
##            df7a=df7a.append(s5d,ignore_index=True)
            
        print(df7,'output_df7')
##        print('\n\n')
##        print(df,'output_df')
##        print('\n\n')
        df8=df8.append(df7)
        print('\n\n')
        print(df8,'output_df8')
        print('\n')
        print(t5,'  dates array')
        
        
##        print(df8,'/// df7')
##        print('s45=',s45,'   v4=',v4,'   sell_at:',v5)

##        print(df7,' df7 =========== from main ===========')
##        plot3(df5)
##        print(df,'s6')

    df9=df8.append(df8)
    return(df9)
    print(df9,'88')

'''   
