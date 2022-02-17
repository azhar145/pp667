
def s6(dfd,u33,df7a):
    df=dfd
##def cc(df,test,gt4,x,df9,ss):
    import time
    import matplotlib.pyplot as plt 
    import pandas as pd
    import sys
    from datetime import date
    from dateutil import parser
    ##print('-------------------start of [s6] module-----------------------------')

##
##    ##print(df,'88')

    
##    print('\n\n\n\n')
##    print('********************** summary Data frame df 7 **********************************')
##    print(df7,'df7')
##    print('********************** summary Data frame df 7 **********************************')
##    sys.exit()
    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns = 255
    pd.options.display.max_rows = 6500000

    ##pd.options.display.max_rows = 999999
    pd.options.display.max_columns = 76
    pd.set_option("display.max_columns", 200)
    pd.set_option('display.width', 1000)
    pd.set_option('display.expand_frame_repr', False)


    pd.options.display.float_format = '{:.2f}'.format
    pd.options.display.max_columns = 255
    pd.options.display.max_rows = 6500000

    ##pd.options.display.max_rows =999999 
    ##pd.options.display.max_columns = 36
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 200)
    pd.set_option('display.max_columns', 0)
    pd.set_option('display.max_columns', None)
    pd.set_option("expand_frame_repr", True)

    df_short = pd.DataFrame()
    df4 = pd.DataFrame()
    df5 = pd.DataFrame()
    # df3=df
    g6 = pd.DataFrame()
    g7 = pd.DataFrame()

    # SAR reversal
##    df.reset_index(inplace=True)
    m2 = []
    m3 = []
    m4 = []
    t5=0
    t6=0

    p44=[]
    p45=[]
    i2='53'
    df['i2']=''
    df['i2a']=''





##    print(df,'from s4.py  55 kkkkkk')
##    print(test,'========== inside s6 ============')
# print(df.index,'ddddddddddddddddddd')

########################## buy condition ######################################
# print(df.index,'kkkkkkkkkkkkkkkkkkkkkkkkkkk')

    u=0
    g43=0;g44=0;g45=' ';g46=0.0;g47=0.0
    s43=0;s44=0;s45=' ';s46=0.0;s47=0.0
    v5=0.0
    v6=0.0
    buy_signal_counter=0
    buy_signal_counter_sig=0


##    df.set_index(df['counter'],inplace=True)
##    print(df,'888')
##    print(df.index,'jj')
##    df.reset_index(inplace=True,drop=True)
##    print('\n\n')
##    print(df.index,'jj22-------------------------')
##    df.set_index([s3,s2],inplace=True)
##    print(df.index,'jj22-------------------------')
##    print('\n\n')
##    df['i']=df.index
    df.reset_index(inplace=True,drop=True)
    df.set_index(df['i'],inplace=True)
##    print(df)


    #print(df,'4444444444444444444444444444444444444444444444444444444444444444444444444444444444444')
    
##    df.set_index(df['Datetime'])
    k57=0
##    print(df,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')



    ##print('babu khan ', df,df.shape)
#################################################################################################
##    print('\n\n\n')
    
    dfm=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    df=dfm
    ##print('\n\n\n')
    ##print('babu khan2 ', df,df.shape)
##    sys.exit()
#################################################################################################

##########################################################################################################    
##    print(df,'nn ',u33)
    for z in df.index:
        buy_signal_counter=buy_signal_counter+1
##        print(z,'azhar 2')
        u=u+1
        t5=t5+1
        k57=k57+1
        df['i2'].loc[z]=i2



##        buy_condition = df['macd'].loc[z] > 0 and df['macd'].shift(1).loc[z] < 0

        buy_condition = df['Close_vwap'].loc[z] > 0 and (df['Close_vwap'].shift(1).loc[z] > 0) and (df['Close_vwap'].shift(2).loc[z] < 0)\
                and df['macd'].loc[z] > 0 and df['EMA-510'].loc[z] > 0



##        buy_condition = df['macd'].loc[z] > 0 and df['macd'].shift(1).loc[z] < 0 and df['macd'].shift(2).loc[z] < 0\
##                        and df['aroonup'].loc[z].round(1) > 85 

         

##        buy_condition = df['MOM'].loc[z] - df['MOM'].shift(1).loc[z] > 0 and\
##                        df['macd'].loc[z] > 0 and df['adx'].loc[z] > 24 and df['ATR'].loc[z] > .9 and df['TR'].loc[z] > .5

##        buy_condition = df['MOM'].loc[z] - df['MOM'].shift(1).loc[z] 
####################################################################################################################################
        '''
        if buy_condition == True:
            print('-------------------------------------------------------------------------------------------------------------------------------')
            print('index->', z,'  ',buy_condition,' tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(3),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),
                  '----------------------------------------------------------->')
            print('-------------------------------------------------------------------------------------------------------------------------------')
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1),' ------------>')

        elif df['macd'].loc[z] > 0:
            print('-------------------------------------------------------------------------------------------------------------------------------')
            print('index->', z,'  ',buy_condition,' tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(3),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),
                  '----------------------------------------------------------->')

##            print('-------------------------------------------------------------------------------------------------------------------------------')
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1),' ------------>')

        else:
            print('index->', z,' **** ',buy_condition,'**** tkr-> ',df['ticker'].loc[z],' macd-> ',df['macd'].loc[z].round(1),' adx-> ',df['adx'].loc[z].round(3),
              ' MOM-> ',df['MOM'].loc[z].round(1),' ATR->',df['ATR'].loc[z].round(1),' Close_vwap->',df['Close_vwap'].loc[z].round(1),' sqz_on->',\
                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1))
##            print(' Close_vwap->',df['Close_vwap'].loc[z].round(1),' squeeze_on->',
##                  df['squeeze_on'].loc[z],' aroonup->',df['aroonup'].loc[z].round(1),' CCI->',df['CCI'].loc[z].round(1),'EMA-35->',
##                  df['EMA-35'].loc[z].round(1),' EMA_5_vwap->',df['EMA_5_vwap'].loc[z].round(1),'EMA_50_vwap->',df['EMA_5_vwap'].loc[z].round(1))
        '''
####################################################################################################################################            

        if buy_condition:
##        if buy_condition and i2=='53':
            i2 = '51'

            df['signal'].loc[z] = "Buy_signal"

##            print('              Buy signal         ')
##            print('         ----------------------       ')
##            print('Close=',df['Close'].loc[z])
##            print('Close_vwap = ',df['Close_vwap'].loc[z])
##            print('macd=',df['macd'].loc[z])
##            print('adx=',df['adx'].loc[z])
##            if df['VZO'].loc[z] > 100:
##                print('VZO=',df['VZO'].loc[z],'   Will go down')
##            if df['VZO'].loc[z] < -100:
##                print('VZO=',df['VZO'].loc[z],'   Will go up')
##            else:
##                print('VZO=',df['VZO'].loc[z],'   sideways/not sure')
##            print('CCI=',df['CCI'].loc[z])
##            print('MOM=',df['MOM'].loc[z])
##            print('         ----------------------       ')
##            print('\n')

            b_Close_vwap=df['Close_vwap'].loc[z]
            b_macd=df['macd'].loc[z]
            b_mom=df['MOM'].loc[z]
            b_VZO=df['VZO'].loc[z]
            b_CCI=df['CCI'].loc[z]

            b48=b_Close_vwap
            b47=b_macd
            b46=b_mom
            b49=b_VZO
            b50=b_CCI
            

##            =================================================== >>>>>
##            df['signal'].loc[z] = 55
            
            v5 = df['Close'].loc[z]  # v5 is buy
            v6 = df['CCI'].loc[z]
            t_buy = df['Datetime'].loc[z]

            v8 = df['ticker'].loc[z]
##            print(z,'  z vs u        ',u)
            g43 = z
            g44=df['Datetime'].loc[z]
            g45=df['ticker'].loc[z]
            g46=df['MOM'].loc[z]
            g47=df['macd'].loc[z]
            buy_signal_counter_sig==buy_signal_counter
            break
            
##########################################################################
######################## SELL CONDITION ##################################
##    print('g43=',g43,' 00000000000000000000000000000000000000000000000000000000000')
    i = 0
    mm3 = 'MOM'
    t6=0
##    print('\n')
    
##    print(g43,'   ',g44,'  ',df['ticker'][-1],'----------- buy signal received here --------------')
##    print(u33,'  Buy ',g43,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
##    print('\n')
##    print(u33,'  index Buy ',g43,'  buy=',v5,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
    

    sell_signal_counter=0
    sell_signal_counter_sig=0

    df.dropna(subset=[mm3], how='all', inplace=True)
    ##print(df,df.shape,'8887')



    if v5 == 0:
        
        
        s5d={'stragety':'2','Date':str(u33),'ticker':g45,'Buy_at':'0','Sell_at':'0','Profit':'',\
             'b_Close_vwap':'dummy','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}
        df7a=df7a.append(s5d,ignore_index=True)
    



    if v5 != 0:  # (if sell/v5 !=0 )
        
        
        for z in range(g43, df.index[-1]):
    ##    for z in range(g43, df.index[-1]):
            sell_signal_counter=sell_signal_counter+1
    ##        print(g43,'------------------',df.index[-1])       
            t6=t6+1
            
            sell_condition = df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0
    ##        print(df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0,'  oooooooooooooooooooooooooooooo')
    ##        sell_condition = df['macd'].loc[z] < 0 and df['macd'].shift(1).loc[z] > 0


            
            
    ##        sell_condition = (df[mm3].loc[z] < 0 and (df[mm3].loc[z] - df[mm3].shift(1).loc[z] < 00) and df['Close'].loc[z] > v5)

            if sell_condition and i2=='51' and g43 != None:                
                sell_signal_counter_sig==sell_signal_counter
##            if sell_condition:                
##                sell_signal_counter_sig==sell_signal_counter
                



                s_Close_vwap=df['Close_vwap'].loc[z]
                s_macd=df['macd'].loc[z]
                s_mom=df['MOM'].loc[z]
                s_VZO=df['VZO'].loc[z]
                s_CCI=df['CCI'].loc[z]


    ##        sell_condition = (df['Close'].loc[z] > v5) and df['macd'].loc[z] < 0
    ##        print(df['macd'].loc[z])
    ##        sell_condition = df['macd'].loc[z] 
            
    ##        sell_condition = df['Close'].loc[z] - df['Close'].shift(1).loc[z] < (.5) or df['Close'].loc[z] < v5-.1 
    ##                         (df['Close'].loc[z] < 0 and df['Close'].shift(1).loc[z] < 0 and df['Close'].shift(2).loc[z] < 0\
    ##                             and df['Close'].shift(3).loc[z] < 0)
            
    ##        sell_condition = (df[mm3].loc[z] < 0 and (df[mm3].loc[z] - df[mm3].shift(1).loc[z] < 00) and df['Close'].loc[z] > v5)
    ##        if float(df['macd'].loc[z])  < float(0):  
    ####        if sell_condition and i2=='51' and g43 != None:
    ##            sell_signal_counter_sig==sell_signal_counter
    ##            print('buy price: ',v5, ' exit price=',v5-.25)
                
                df['i2a'].loc[z]=i2
                i2='53'
                ##                        print(' sell cond')

                ##                    sell_condition=df[mm3].loc[z] < 0
                
                df['signal'].loc[z] = "Sell_signal"
                

                
                t_sell = df['Datetime'].loc[z]
                v4 = df['Close'].loc[z]
                v7 = df['ticker'].loc[z]
    ##                        print(v7,'  ',v4,'/',v5,'  ',v4-v5,'  ',t_sell,'/',t_buy)
                xm = v7
                x2 = v5
                x3 = v4
                x5 = v6
                x4 = v4 - v5

                g6 = g6.append([[xm, v5, v4, x4, v7, t_buy, t_sell]])

                i = i + 1

                s43 = z
                s44=df['Datetime'].loc[z]
                s45=df['ticker'].loc[z]
                s46=df['MOM'].loc[z]
                s47=df['macd'].loc[z]
                s48=df['Close_vwap'].loc[z]
                s49=df['VZO'].loc[z]
                s50=df['CCI'].loc[z]
                s51=df['RSI'].loc[z]

            else:
                if z==df.index[-1]:
                    
                    ##print('No Sell')
                    pass

               

    ##                    print('============= Bought but sell condition not met during the day/Loss ===================')
    ##    print(s43,'   at time:  ticker= '' ----------- [sell] signal received here --------------')
    ##    print(u33,'  Sell ',s43,'   at time: ',s44,'  ticker= ',s45,' MOM=',s46,'  MACD=',s47,' ----------- [sell] signal received here --------------')
##        print(u33,'  index Sell ',s43,'  buy=',v4,'   at time: ',s44,'  ticker= ',s45,' MOM=',s46,'  MACD=',s47,' ----------- [sell] signal received here --------------')
        
    ##    print(u33,'  index Buy ',g43,'  buy=',v5,'   at time: ',g44,'  ticker= ',g45,' MOM=',g46,'  MACD=',g47,' ----------- buy signal received here --------------')
        
        print('\n')
        if v4-v5 > 0:
            print('================= Profit=',round((v4-v5),2),df)
            print('Buy_condition=',buy_condition)
            print('Sell_condition=',sell_condition)
            print(df[['Close','ticker','s3','s2','signal']])
        else:
            print('================= Loss=',round((v4-v5),2),df)
            print('Buy_condition=',buy_condition)
            print('Sell_condition=',sell_condition)
            print(df[['Close','ticker','s3','s2','signal']])
        print('\n')

        print('\n\n\n\n\n')
    ##    print('Close market: ',df['Close'].loc['c2'],'/',df['Close'].loc['c3'],'  ')
        g6.drop_duplicates(subset=None, keep='last', inplace=True)
        

##        s5d={'f2':'34','f3':'55'}
        n=77
        n3=87
        print(v5,'v5 (buy) -----------------------------------------')
        if v5 != 0:
            s5d={'stragety':'2','Date':str(u33),'ticker':s45,'Buy_at':v5,'Sell_at':v4,'Profit':v4-v5,\
             'b_Close_vwap':s48,'b_macd':s47,'b_mom':s46,'b_VZO':s49,'b_CCI':s50}
            df7a=df7a.append(s5d,ignore_index=True)


        if v4==0:
            v5=0
##            s6d={'stragety':'3','Date':str(u33),'ticker':s45,'Buy_at':n,'Sell_at':n3,'Profit':0,\
##             'b_Close_vwap':'55','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}

            df7a = pd.DataFrame({'stragety':'3','Date':str(u33),'ticker':s45,'Buy_at':n,'Sell_at':n3,'Profit':0,\
             'b_Close_vwap':'55','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'})


 
##################################################################
##        if v5 == 0:
##        if df7a.empty==True:    
##            s6d={'stragety':'-1','Date':str(u33),'ticker':s45,'Buy_at':'50','Sell_at':'50','Profit':0,\
##             'b_Close_vwap':'55','b_macd':'dummy','b_mom':'dummy','b_VZO':'dummy','b_CCI':'dummy'}
##            df7a=df7a.append(s6d,ignore_index=True)
##            print(df7a,' =========================================================bbbbbbbbbbbbbbbbb')

##            b_Close_vwap=df['Close_vwap'].loc[z]
##            b_macd=df['macd'].loc[z]
##            b_mom=df['MOM'].loc[z]
##            b_VZO=df['VZO'].loc[z]
##            b_CCI=df['CCI'].loc[z]        



###################################################################

##        if v4==0:
##            v5==0
##            s45==df['ticker'][2]
            
            

##        df7a=df7a.append(s5d,ignore_index=True)

##        print(df7,'--------------- gg55')
        
        '''
        df = df[['Datetime','i2',
                 's3',
                 's2',
                 'i',
                 'ticker',
                 'signal',
                 'Close',
                 'Close_delta',
                 'MOM',
                 'macd',
                 'adx',
                 'ATR',
                 'TR',
                 'Close_vwap',
                 'Open',
                 'Open_delta',
                 'High',
                 'High_delta',
                 'Low',
                 'Low_delta',
                 'Close',
                 'Volume',
                 'Red',
                 'Red_breath',
                 'vwap',
                 'ATR',
                 'TRANGE',
                 'TR',
                 'adx',
                 'MOM',
                 'MOM_slope',
                 'Boling_upper2',
                 'Boling__middle2',
                 'Boling_lower2',
                 'x',
                 'SAR',
                 'SARx',
                 'tail',
                 'lower_band',
                 'upper_band',
                 'bolinger_width',
                 'lower_keltner',
                 'upper_keltner',
                 'vwap_bw_bolinger',
                 'EMA50_bw_bolinger',
                 'squeeze_on',
                 'aroondown',
                 'aroonup',
                 'CCI',
                 'RSI',
                 'EMA_slope',
                 'fastk',
                 'fastd',
                 'TSF',
                 'cross',
                 'mama_fama',
                 'DM_delta',
                 'DI_delta',
                 'mama',
                 'fama',
                 'KAMA',
                 'AD',
                 'MA',
                 'MA2',
                 'macd_slope',
                 'mama',
                 'fama',
                 'KAMA',
                 'AD',
                 'ADOSC',
                 'DEMA',
                 'HT_DCPERIOD',
                 'HT_DCPHASE',
                 'CMO',
                 'PLUS_DI',
                 'MINUS_DI',
                 'PLUS_DM',
                 'MINUS_DM',
                 'ADOSC',
                 'DEMA',
                 'LINEARREG',
                 'LINEARREG_ANGLEG',
                 'LINEARREG_INTERCEPT',
                 'LINEARREG_SLOPE',
    ##             'macd',
                 'macdsignal',
                 'macdhist',
                 'EMA-35',
                 'EMA-510',
                 'EMA-1021',
                 'EMA-2150',
                 'EMA_3_vwap',
                 'EMA_5_vwap',
                 'EMA_10_vwap',
                 'EMA_21_vwap',
                 'EMA_50_vwap',
                 'Close_EMA3',
                 'Close_EMA5',
                 'Close_EMA10',
                 'Close_EMA21',
                 'Close_EMA50',
                 'Close_vwap']]
        '''

        ####print(df.shape,'sin34') 
##        if s44 != 0:
##            
##            print(u33,'    45      ','df','      ','g45','  buy sell-signal  ','\n')
##
##                  
##        if s44==0:
##            print(u33,'    46      ','df','      ','s45','  buy sell-signal  ==== [no sell] ====','\n')

        
        
        print(u33,' -------------------end of [s6] module-----------------------------')
        
        ####print(df.shape,'sin36')

##    x    return(df7,df5)
    return(df,df7a)
##    print('\n\n')
##    print(' df7 train ------------------------------------------------------------------------------------------------------')
##    print(df7)
##    print('------------------------------------------------------------------------------------------------------------------')
##    print('s6-end')  
##    print('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

####################################### no ploytting ###########################################

