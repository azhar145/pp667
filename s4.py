

def s4(u33,y , x2,ATR_target,adx_target,d2,d3):
    import sys
    import time
    import os

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

    import warnings
    import sys
    from datetime import date
    import datetime
    from datetime import timedelta
    from dateutil import parser
    from dateutil import parser

##    print(u33,'<- u33    d2 ->',d2,' d3->',d3)
        
    
        
        


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

##    df =yf.download(tickers,  start = "2021-02-01" , end = "2021-02-04")

    df = yf.download(x2,start=d2,end=d3,interval='60m',auto_adjust = True,threads = True,prepost=True,progress=False, proxies=proxyb)
    print(df,' eeeeeeeeeeeeeeeeeeeee from s4')  
    df['ticker']=''
    for x in df.index:
        df['ticker'].loc[x]=x2
        
        
##    print(df,x2,' === ',u33,' ===')
      
    return(u33,y,d2,d3,df)



#
