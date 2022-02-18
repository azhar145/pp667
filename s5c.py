def s5c(u33,y,d2,d3,df):
    import pandas as pd
    import talib as ta
    import finta as f
    from finta import TA as ff
    import s6

##    df.set_index(df['Datetime'],inplace=True)
##    df['s3b']=''
##    df['s2b']=''
##    df['i']=0
##    i=0
##    for x in df.index:
##        df['i'].loc[x]=i
##        df['s3b'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
##        df['s2b'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]
##        i=i+1
##
####    df.drop('Datetime', axis=1, inplace=True)
##    
####    df['Datetime']=df['s3b']+'-'+df['s2b']
####    df.set_index(df['Datetime'],inplace=True)
##
####    print(df,'s5c')
##    pp=df['s3b'].unique()
##
##
####    print(pp)
##    for x in pp:
##        df=df.iloc[df['s3']==pp]
##    print(df,'filtered by single date')

##    df=gt4
# https://pythonrepo.com/repo/peerchemist-finta-python-finance
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    df = df.assign(vwap=(tp * v).cumsum() / v.cumsum())
      
    for x in df.index:


        df['VZO']=f.TA.VZO(df,14)
##        df['CTI']=f.TA.CTI(df,14)
        df['ADL']=f.TA.ADL(df)
##        VZO=ff.VZO(df,10)
##        PZO=ff.PZO(df,14)
##        VFI=ff.VFI(df,14)
##        SQZMI=ff.SQZMI(df,14)
##        BASP=ff.BASP(df,14)
##        CHANDELIER=ff.CHANDELIER(df,14)
##        ZLEMA=ff.ZLEMA(df,14)
##        EVWMA=ff.EVWMA(df,14)
##        SAR=ff.SAR(df,14)
##        DMI=ff.DMI(df,14)
##        VORTEX=ff.VORTEX(df,14)
##        STC=ff.STC(df,14)
##        df['VW_MACD']=f.finta.TA['VW_MACD'](df['Close'],signal=9,period_slow=26, period_fast=12)
        df['CCI'] = ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
        df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['signal'] = ''
        df['EMA_3'] = ta.EMA(df['Close'], timeperiod=3)
        df['EMA_5'] = ta.EMA(df['Close'], timeperiod=5)
        df['EMA_10'] = ta.EMA(df['Close'], timeperiod=10)
        df['EMA_50'] = ta.EMA(df['Close'], timeperiod=50)
        df['EMA_100'] = ta.EMA(df['Close'], timeperiod=100)
        df['EMA_200'] = ta.EMA(df['Close'], timeperiod=200)
        
        df['EMA_21'] = ta.EMA(df['Close'], timeperiod=21)
        df['MOM'] = ta.MOM(df['Close'], timeperiod=14)
        df['Close_vwap'] = df['Close'] - df['vwap']
        df['EMA-35'] = df['EMA_3'] - df['EMA_5']
        df['EMA-510'] = df['EMA_5'] - df['EMA_10']
        df['EMA-1021'] = df['EMA_10'] - df['EMA_21']
        df['EMA-2150'] = df['EMA_21'] - df['EMA_50']
        df['EMA_3_vwap'] = df['EMA_3'] - df['vwap']
        df['EMA_5_vwap'] = df['EMA_5'] - df['vwap']
        df['EMA_10_vwap'] = df['EMA_10'] - df['vwap']
        df['EMA_21_vwap'] = df['EMA_21'] - df['vwap']
        df['EMA_50_vwap'] = df['EMA_50'] - df['vwap']
        df['EMA_100_vwap'] = df['EMA_100'] - df['vwap']
        df['EMA_200_vwap'] = df['EMA_200'] - df['vwap']
        df['macd_35'], df['macdsignal'], df['macdhist'] = ta.MACD(
        df['Close'], fastperiod=3, slowperiod=5, signalperiod=3)
        df['Close_EMA3'] = df['Close'] - df['EMA_3']
        df['Close_EMA5'] = df['Close'] - df['EMA_5']
        df['Close_EMA10'] = df['Close'] - df['EMA_10']
        df['Close_EMA21'] = df['Close'] - df['EMA_21']
        df['Close_EMA50'] = df['Close'] - df['EMA_50']
        df['Close_vwap'] = df['Close'] - df['vwap']

        df['EMA_3s']=ta.MA(df['Close'], timeperiod=3)
        df['EMA_5s']=ta.MA(df['Close'], timeperiod=5)
        df['EMA_10s']=ta.MA(df['Close'], timeperiod=10)
        df['EMA_21s']=ta.MA(df['Close'], timeperiod=21)
        df['EMA_50s']=ta.MA(df['Close'], timeperiod=50)
        df['EMA_100s']=ta.MA(df['Close'], timeperiod=100)
        df['EMA_200s']=ta.MA(df['Close'], timeperiod=200)

        df['adx'] = ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['ATR'] = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['TR'] = abs(df['High'] - df['Low'])
        df['AD'] = ta.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])

        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=300, maximum=5)
        df['SARx'] = df['Close'] - df['SAR']
        df['PLUS_DI'] = ta.PLUS_DI(df['High'],df['Low'],df['Close'],timeperiod=14)
        df['MINUS_DI'] = ta.MINUS_DI(df['High'], df['Low'], df['Close'], timeperiod=14)
        df['PLUS_DM'] = ta.PLUS_DM(df['High'], df['Low'], timeperiod=14)
        df['MINUS_DM'] = ta.MINUS_DM(df['High'], df['Low'], timeperiod=14)
        df['DM_delta'] = df['PLUS_DM'] - df['MINUS_DM']
        df['DI_delta'] = df['PLUS_DI'] - df['MINUS_DI']
        ## squeeze info
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (2 * df['stddev'])
        df['upper_band'] = df['20sma'] + (2 * df['stddev'])
        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)

        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)
        




##        df['Boling_upper2'], df['Boling__middle2'], df['Boling_lower2'] = df['Boling_lower2'] = ta.BBANDS(df['Low'], timeperiod=20, nbdevup=2, nbdevdn=2)

        ##    df['EMA_3']=df['Close']-ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5']=df['Close']-ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10']=df['Close']-ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21']=df['Close']-ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50']=df['Close']-ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100']=df['Close']-ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200']=df['Close']-ta.MA(df['Close'], timeperiod=200)
##
##
##    df['EMA_3s']=ta.MA(df['Close'], timeperiod=3)
##    df['EMA_5s']=ta.MA(df['Close'], timeperiod=5)
##    df['EMA_10s']=ta.MA(df['Close'], timeperiod=10)
##    df['EMA_21s']=ta.MA(df['Close'], timeperiod=21)
##    df['EMA_50s']=ta.MA(df['Close'], timeperiod=50)
##    df['EMA_100s']=ta.MA(df['Close'], timeperiod=100)
##    df['EMA_200s']=ta.MA(df['Close'], timeperiod=200)

          

#######################
    df.reset_index(inplace=True)
##    print(x,'66',df.columns[0])
##    print(df,'663')
##    sys.exit()
    df['squeeze_on']=''
    p=0
    for x in df.index:
        ######################## squeeze 55


        if df['lower_band'].loc[x] > df['lower_keltner'].loc[x] and df['upper_band'].loc[x] < df['upper_keltner'].loc[x]:
            
            df['squeeze_on'].loc[x]='in_squeeze'
            p=p+1
##                print(x,"  in 1 min Squeeze, ATR=",df['ATR'].loc[z])
        else:
            df['squeeze_on'].loc[x]=' '

######################## squeeze 55
        
    df.set_index(df['Datetime'],inplace=True)
    df['s3']=''
    df['s2']=''
    df['i']=0
    i=0
    for x in df.index:
        df['i'].loc[x]=i
        df['s3'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[0]
        df['s2'].loc[x]=str(df['Datetime'].loc[x]).split(' ')[1][0:5]
        i=i+1

    df.drop('Datetime', axis=1, inplace=True)
    
    df['Datetime']=df['s3']+'-'+df['s2']
    df.set_index(df['Datetime'],inplace=True)


##############################
##    print(df['VZO'],' with VZO values',' == ',u33,' == ')
    print(df,'   s5c')
    return(u33,df)
    
