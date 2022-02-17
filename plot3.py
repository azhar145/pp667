
def plot3(df5,df7):
    # u33=date
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt2
    from matplotlib.axis import Axis
    from matplotlib.widgets import Slider, Button, RadioButtons 
    import numpy as np    
    import sys

    print(df,' mm')

    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')] 
    
    print(df.columns.get_loc('s2'),'  ',df.iloc[3,df.columns.get_loc('s2')])
    print(df.columns.get_loc('Close'),'  ','Close')
    print(df.columns.get_loc('Close_vwap'),'Close_vwap')
    print(df.columns.get_loc('EMA-510'),'EMA-510')
    print(df.columns.get_loc('EMA-1021'),'EMA-1021')
    print(df.columns.get_loc('EMA-2150'),'EMA-2150')
    print('\n')
    print(df.columns.get_loc('EMA_3_vwap'),'EMA_3_vwap')
    print(df.columns.get_loc('EMA_5_vwap'),'EMA_5_vwap')
    print(df.columns.get_loc('EMA_10_vwap'),'EMA_10_vwap')
    print(df.columns.get_loc('EMA_21_vwap'),'EMA_21_vwap')
    print(df.columns.get_loc('EMA_50_vwap'),'EMA_50_vwap')
    print(df.columns.get_loc('MOM'),'MOM')
    print('EMAs','\n')
    print(df.columns.get_loc('EMA_3s'),'EMA_3s')
    print(df.columns.get_loc('EMA_5s'),'EMA_5s')
    print(df.columns.get_loc('EMA_10s'),'EMA_10s')
    print(df.columns.get_loc('EMA_21s'),'EMA_21s')
    print(df.columns.get_loc('EMA_50s'),'EMA_50s')
    print(df.columns.get_loc('EMA_100s'),'EMA_100s')
    print(df.columns.get_loc('EMA_200s'),'EMA_200s')
    print(df.columns.get_loc('macd'),'macd')
##    print(df.columns.get_loc('SARx'),'sarx')
    print(df.columns.get_loc('CCI'),'cci')
    print(df.columns.get_loc('RSI'),'rsi')
    print(df.columns.get_loc('adx'),'adx')
    print(df.columns.get_loc('ATR'),'ATR')
    print(df.columns.get_loc('AD'),'AD')
    print(df.columns.get_loc('SAR'),'SAR')
    print(df.columns.get_loc('SARx'),'SARx')
    print(df.columns.get_loc('TR'),'TR')
    print(df.columns.get_loc('squeeze_on'),'squeeze_on')
    

    print('\n',df.columns)


    
##    print(df.columns.get_loc('Boling_upper2'))
##    print(df.columns.get_loc('Boling__middle2'))
##    print(df.columns.get_loc('Boling_lower2'))                         
    
##    print(df.columns['s2'])
##    u=df.iloc[3,'ticker']
##    print(df['ticker'][4])
##    sys.exit()




##    df3b=df[df['MOM'] > 0 & (df['MOM']-df['MOM'].shift(1)) < 0]
    
    
    print(df.shape,' 44')
    df4=df[df['MOM']<0]
    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    df3a=df[(df['MOM'] > 0) & ((df['MOM']-df['MOM'].shift(1)) > 0)]
    df3b=df[(df['MOM'] > 0) & ((df['MOM']-df['MOM'].shift(1)) < 0)]

    df4a=df[(df['MOM'] < 0) & ((df['MOM']-df['MOM'].shift(1)) > 0)]
    df4b=df[(df['MOM'] < 0) & ((df['MOM']-df['MOM'].shift(1)) < 0)]
    
    fig1, (ax1, ax2, ax3,ax4,ax5,ax6,ax7) = plt.subplots(7, 1,sharex=True)
    fig1.suptitle('baba5', fontsize=5)
    
    bb=df.columns.get_loc('s2')
    df.sort_values(['s2'],ascending=True,inplace=True)

    plt.rc('legend',fontsize=3) # using a size in points
    plt.rc('legend',fontsize='small') # using a named size
    plt2.rc('legend',fontsize=3) # using a size in points
    plt2.rc('legend',fontsize='small') # using a named size

    
    
    plt.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    plt2.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    mclrs5=[]
#########################
    for x in df.index:


    ####################################        
##        if df.iloc[x,df.columns.get_loc('MOM')] > 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('green')
##        elif df.iloc[x,df.columns.get_loc('MOM')] > 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('cyan')        
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('red')
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('green')

        if df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('green')
        elif df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')  

########################    
        
##    ax1.title.get_name('k')
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close_vwap')]),color='green', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)
    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    ax1.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')


    
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-510')]))
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-1021')]))
    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-2150')]))
    
    ax1.bar(df3a.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3a.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color=mclrs5)
##    ax1.bar(df3b.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')

    
    ax1.bar(df4a.iloc[:,df4a.columns.get_loc('s2')],pd.to_numeric(df4a.iloc[:,df4a.columns.get_loc('MOM')]), width=2, color='blue')
    ax1.bar(df4b.iloc[:,df4a.columns.get_loc('s2')],pd.to_numeric(df4b.iloc[:,df4b.columns.get_loc('MOM')]), width=2, color='cyan')

##    ax1.bar(df3b.iloc[:,df3b.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')


##    ax1.bar(df3.iloc[:,df3.columns.get_loc('s2')],pd.to_numeric(df3.iloc[:,df3.columns.get_loc('MOM')]), width=2, color='yellow')
##    ax1.bar(df4.iloc[:,df4.columns.get_loc('s2')],pd.to_numeric(df4.iloc[:,df4.columns.get_loc('MOM')]), width=2, color='blue')
##    
    ax1.legend(['Close_vwap', 'EMA-510','EMA-1021','EMA-2150','MOM'],loc=3, fontsize = 'x-small')
##    ax1.hlines(0, df.iloc[:,43].min(), df.iloc[:,43].max(), lw=1, color='black')
    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')

##    ax1.get_animated
##    ax1.grid(which='minor',visible=None,axis='both')
##    ax1.grid()

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    ax5.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('adx')]))
##    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,43]))
    ax5.fill_between(p1, p2, where=(pd.to_numeric(p2) > 25), color='#00FF00')
    ax5.fill_between(p1, p2, where=(pd.to_numeric(p2) < 25), color='#ff0000')
    ax5.fill_between(p1, p2, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
    ax5.hlines(40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax5.legend(['adx (adx >40/breakout'],loc=3, fontsize = 'x-small')


    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]),color='black', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)
    ax2.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_3s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_5s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_10s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_21s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_50s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_100s')]))
    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_200s')]))
    ax2.legend(['Close','vwap','EMA_3s','EMA_5s','EMA_10s','EMA_21s','EMA_50s','EMA_100s','EMA_200s'],loc=2, fontsize = 'x-small')
    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    ax2.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('SARx')]
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close_vwap')]),color='green', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)

    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    ax3.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_3_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_5_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_10_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_21_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA_50_vwap')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('SARx')]))
    ax3.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
    ax3.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
    ax3.legend(['Close_vwap','EMA_3_vwap','EMA_5_vwap','EMA_10_vwap','EMA_21_vwap','EMA_50_vwap','SARx'],loc=2, fontsize = 'x-small')
##    ax3.hlines(0, df.iloc[:,43].min(), df.iloc[:,43].max(), lw=1, color='black')
    ax3.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')



##    ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,4]),color='green', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('CCI')]
    p3=100
    p4=-100

    g1=df.iloc[:,df.columns.get_loc('s2')]
    g2=df.iloc[:,df.columns.get_loc('RSI')]
    g3=70
    g4=30
    
    ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('CCI')]))
    ax4.set_title('CCI')
        
    ax4.fill_between(p1, p2,p3, where=(pd.to_numeric(p2) > p3), color='#00FF00')
    ax4.fill_between(p1, p2,p4, where=(pd.to_numeric(p2) < p4), color='#ff0000')

    ax4.fill_between(g1, g2,g3, where=(pd.to_numeric(g2) > g3), color='#00FF00')
    ax4.fill_between(g1, g2,g4, where=(pd.to_numeric(g2) < g4), color='#ff0000')
    
    ax4.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('RSI')]))         
    ax4.legend(['CCI','RSI'],loc=2, fontsize = 'x-small')
    ax4.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax4.hlines(100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax4.hlines(-100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    ax4.hlines(30, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='green')
    ax4.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='green')

    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('CCI')]
    ax4.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('macd')] 
    ax6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))

    ax6.legend(['macd'],loc=3, fontsize = 'x-small')
    ax6.fill_between(p1, p2, p2+325, where=(pd.to_numeric(p2) > 0), color='#00FF00')
    ax6.fill_between(p1, p2,p2-5, where=(pd.to_numeric(p2) < 0), color='#ff0000')
    ax6.legend(['macd'],loc=3, fontsize = 'x-small')
    ax6.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=4, color='green')


    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('macd')]
    ax6.fill_between(p1, p2a.min()-2-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('squeeze_on')]
    ax7.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('squeeze_on')]))
    ax7.fill_between(p1, p2, where=(p2 =='in_squeeze'), color='#00FF00')
##    ax2.fill_between(p1, p2, where=(p2 is None), color='#ff0000')
    ax7.legend(['squeeze_on'],loc=3, fontsize = 'x-small')

##    # adx
##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('adx')]
##    p2a=df.iloc[:,df.columns.get_loc('squeeze_on')]
##    ax7.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-510')]))
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-1021')]))
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('EMA-2150')]))
##    
##    ax1.bar(df3a.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3a.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color='blue')
##    ax1.bar(df3b.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')
##'EMA-510','EMA-1021','EMA-2150'
    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    fig3, (gp,gp2,gp3) = plt.subplots(3,1,sharex=True)
    fig3.suptitle('baba5', fontsize=5)

  # , ax2a, ax3a,ax4a
##    if df.loc[:,'vwap'] > 800 & (type(df.loc[:,'vwap']) == int or float):

 
    bb=df.columns.get_loc('s2')
    df.sort_values(['s2'],ascending=True,inplace=True)

    plt.rc('legend',fontsize=3) # using a size in points
    plt.rc('legend',fontsize='small') # using a named size
    plt2.rc('legend',fontsize=3) # using a size in points
    plt2.rc('legend',fontsize='small') # using a named size


    plt.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    plt2.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))

    dfs2=df.loc[(df['Close_vwap'] > 0)]
    dfs3=df.loc[(df['Close_vwap'] < 0)]
    df.to_csv('/home/az2/hh.txt')

##    ax1a.bar(df3a.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color='blue')
##    ax1a.bar(df3b.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')
##    ax1.bar(df3a.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3a.iloc[:,df3a.columns.get_loc('MOM')]), width=2, color='blue')
##    ax1.bar(df3b.iloc[:,df3a.columns.get_loc('s2')],pd.to_numeric(df3b.iloc[:,df3b.columns.get_loc('MOM')]), width=2, color='yellow')

    clrs=[];clrs2=[]
    for x in df.index:
    ##    print(df.loc[x,'Close_vwap'])
        if df.loc[x,'Close_vwap'] < 0:
            clrs.append('red')
        else:
##            df.loc[x,'Close_vwap'] > 0:
            clrs.append('green')


##        if df.loc[x,'EMA_510'] <= 0:
##            clrs2.append('red')
##        elif df.loc[x,'EMA_510'] > 0:
##            clrs2.append('green')      
## was up
    df['clrs']=clrs
    print(df,'88')
    df.drop(['clrs'],axis=1,inplace=True)

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    gp.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
    gp.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=clrs,width=2)
    gp.legend(['Close_vwap','ADX > 40'],loc=3, fontsize = 'x-small')
    for x in df.index:     
            
        if df.loc[x,'MOM'] < 0:
            clrs2.append('red')
        else:
            clrs2.append('green')


     # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    gp.fill_between(p1, p5a.min(),0, where=(pd.to_numeric(p2) > 25) & (pd.to_numeric(p2) < 40), color= '#ff9a00')
           
            
##    gp2.bar(df.iloc[:,df.columns.get_loc('MOM')],df.iloc[:,df.columns.get_loc('MOM')],color=clrs2,width=2)
##    gp2.legend(['MOM'],loc=3, fontsize = 'x-small')


# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close')]
    gp2.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    gp2.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)
             
        

    gp2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]),color='black', marker='o', linestyle='dashed',
     linewidth=1, markersize=2)

    dfp=df.loc[df['Close']>df['SAR']]
    dfg=df.loc[df['Close']<df['SAR']]
   
    gp2.plot(dfp.iloc[:,bb],pd.to_numeric(dfp.iloc[:,dfp.columns.get_loc('SAR')]),color='Green', marker='v', linestyle='dashed',\
                 linewidth=0, markersize=2)
    gp2.plot(dfg.iloc[:,bb],pd.to_numeric(dfg.iloc[:,dfg.columns.get_loc('SAR')]),color='Red', marker='^', linestyle='dashed',\
                 linewidth=0, markersize=2)


    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Close')]
    gp2.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 25) & (pd.to_numeric(p2) < 40), color= '#ff9a00')
    
        
##    gp2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('SARx')]),color='red', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)

    gp2.legend(['Close','SAR','ADX > 40','vwap'],loc=2, fontsize = 'x-small')
##    gp2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('SAR')],color='red',width=2)
##    gp2.legend(['SAR'],loc=3, fontsize = 'x-small')
##    gp2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('SARx')],color='blue',width=2)
##    gp2.legend(['SARx'],loc=3, fontsize = 'x-small')



# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('VZO')]
    gp3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('VZO')]
    gp3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 25) & (pd.to_numeric(p2) < 40), color= '#ff9a00')
    

    gp3.plot(df.loc[:,'s2'],df.loc[:,'VZO'],color='black', marker='o', linestyle='dashed',linewidth=1, markersize=2)
    gp3.legend(['VZO','ADX > 40'],loc=3, fontsize = 'x-small')

    ##    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    gp3.hlines(60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    gp3.hlines(40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    gp3.hlines(-60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    gp3.hlines(-40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    gp3.hlines(-5, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='green',label='ddd')
    gp3.hlines(15, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='red')

    
##    gp3.bar(df.iloc[:,df.columns.get_loc('EMA_510')],df.iloc[:,df.columns.get_loc('EMA_510')],color=clrs,width=2)
##    gp3.legend(['EMA_510'],loc=3, fontsize = 'x-small')

##
##    dfs2=df.loc[(df['EMA-510'] > 0)]
##    dfs3=df.loc[(df['EMA-510'] < 0)]
##    ax2a.bar(dfs2.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,dfs2.columns.get_loc('EMA-510')]), width=2, color='blue')
##    ax2a.bar(dfs3.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,dfs3.columns.get_loc('EMA-510')]), width=2, color='cyan')
##    ax2a.legend(['EMA-510'],loc=3, fontsize = 'x-small')
##
##
##
##    dfs2=df.loc[(df['EMA-1021'] > 0)]
##    dfs3=df.loc[(df['EMA-1021'] < 0)]
##    ax3a.bar(dfs2.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,dfs2.columns.get_loc('EMA-1021')]), width=2, color='blue')
##    ax3a.bar(dfs3.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,dfs3.columns.get_loc('EMA-1021')]), width=2, color='cyan')
##    ax3a.legend(['EMA-1021'],loc=3, fontsize = 'x-small')
##
##    dfs2=df.loc[(df['EMA-2150'] > 0)]
##    dfs3=df.loc[(df['EMA-2150'] < 0)]
##    ax4a.bar(dfs2.iloc[:,dfs2.columns.get_loc('s2')],pd.to_numeric(dfs2.iloc[:,dfs2.columns.get_loc('EMA-2150')]), width=2, color='blue')
##    ax4a.bar(dfs3.iloc[:,dfs3.columns.get_loc('s2')],pd.to_numeric(dfs3.iloc[:,dfs3.columns.get_loc('EMA-2150')]), width=2, color='cyan')
##    ax4a.legend(['EMA-2150'],loc=3, fontsize = 'x-small')
##    ax4a.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('Close')]),color='black', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)
##    ax4a.legend(['Close'],loc=3, fontsize = 'x-small')



##    print(df.columns[43],'column 43')
##    ax2.title(df.iloc[3,df.columns.get_loc('ticker')])


##        df['adx'] = ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
##        df['ATR'] = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
##        df['TR'] = abs(df['High'] - df['Low'])
##        df['AD'] = ta.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'])
####        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
####        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
##        df['SAR'] = ta.SAR(df['High'], df['Low'], acceleration=300, maximum=5)
##        df['SARx'] = df['Close'] - df['SAR']
##        df['PLUS_DI'] = ta.PLUS_DI(df['High'],df['Low'],df['Close'],timeperiod=14)
##        df['MINUS_DI'] = ta.MINUS_DI(df['High'], df['Low'], df['Close'], timeperiod=14)
##        df['PLUS_DM'] = ta.PLUS_DM(df['High'], df['Low'], timeperiod=14)
##        df['MINUS_DM'] = ta.MINUS_DM(df['High'], df['Low'], timeperiod=14)
##        df['DM_delta'] = df['PLUS_DM'] - df['MINUS_DM']
##        df['DI_delta'] = df['PLUS_DI'] - df['MINUS_DI']

    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]

    df.sort_values(['s2'],ascending=True,inplace=True)
    print(df,'5555555555555555555555555555555555  ')
    fig2, (ax3,ax5) = plt.subplots(2, 1,sharex=True)
    fig2.suptitle('baba6', fontsize=5)
     
    bb=df.columns.get_loc('s2')
    

    plt.rc('legend',fontsize=3) # using a size in points
    plt.rc('legend',fontsize='small') # using a named size
    plt2.rc('legend',fontsize=3) # using a size in points
    plt2.rc('legend',fontsize='small') # using a named size

    plt.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))
    plt2.suptitle(str(df.iloc[3,df.columns.get_loc('ticker')])+str('  ')+str(p2b)+str('  ')+str(p2d))

##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,19]),color='green', marker='o', linestyle='dashed',
##     linewidth=1, markersize=2)

##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('macd')] 
##    ax1.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))
##
##    ax1.legend(['macd'],loc=3, fontsize = 'x-small')
##    ax1.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
##    ax1.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
##    ax1.legend(['macd'],loc=3, fontsize = 'x-small')




##    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
##    ax1.hlines(100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
##    ax1.hlines(-100, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
##    ax1.hlines(20, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
##    ax1.hlines(70, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')


##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('adx')]
##    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('adx')]))
####    ax2.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,43]))
##    ax2.fill_between(p1, p2, where=(pd.to_numeric(p2) > 25), color='#00FF00')
##    ax2.fill_between(p1, p2, where=(pd.to_numeric(p2) < 25), color='#ff0000')
##    ax2.legend(['adx'],loc=3, fontsize = 'x-small')


# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('ATR')]
    ax3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')



    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('ATR')]
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('ATR')]))
    ax3.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('TR')]))
    ax3.legend(['ATR','TR'],loc=3, fontsize = 'x-small')


    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('squeeze_on')]

##    for x in df.index:
##        if df.iloc[x,df.columns.get_loc('squeeze_on')]=='in_squeeze':
##            df.iloc[x,df.columns.get_loc('squeeze_on')]=int(7)


    
##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('squeeze_on')]
##    ax4.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('squeeze_on')]))
##    ax4.fill_between(p1, p2, where=(p2 =='in_squeeze'), color='#00FF00')
####    ax2.fill_between(p1, p2, where=(p2 is None), color='#ff0000')
##    ax4.legend(['squeeze_on'],loc=3, fontsize = 'x-small')



# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('Boling_lower2')]
    ax5.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')




    d1=df.iloc[:,df.columns.get_loc('upper_keltner')]
    d2=df.iloc[:,df.columns.get_loc('Boling_upper2')]

    f1=df.iloc[:,df.columns.get_loc('lower_keltner')]
    f2=df.iloc[:,df.columns.get_loc('Boling_lower2')]                                

    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('upper_keltner')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('lower_keltner')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Close')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Boling_upper2')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Boling__middle2')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('Boling_lower2')]))
    ax5.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)
##    ax5.fill_between(pd.to_numeric(d2), pd.to_numeric(d1), where=(pd.to_numeric(d2) < pd.to_numeric(d1)), color='#00FF00')
    ax5.fill_between(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Boling_upper2')], df.iloc[:,df.columns.get_loc('Boling_lower2')]
                     ,color='#00FF00')
    ax5.fill_between(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('upper_keltner')], df.iloc[:,df.columns.get_loc('lower_keltner')]
                     ,color='black')
##    ax5.fill_between(f1, f2, where=(pd.to_numeric(f2) < f1), color='#ff0000')
    ax5.legend(['upper_keltner','lower_keltner','Close','Boling_upper2','Boling__middle2','Boling_lower2','vwap'],loc=3, fontsize = 'x-small')


#######################################
## 44
    df['color']=""
    df['Volume_g']=""
    df['Volume_r']=""
    df['Close_r']=""
    df['Close_g']=""
    df['Close_h']=""

    for x in df.index:

    ##    df['ticker'].loc[x]=ticker
        if df['Close'].loc[x]-df['Open'].loc[x] >= 0:
            df['color'].loc[x]=='green'      
            df['Volume_g'].loc[x]=df['Volume'].loc[x]
        else:
            df['Volume_g'].loc[x]=0
    ##        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]+.1
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
        if df['Close'].loc[x]-df['Open'].loc[x] < 0:
            df['color'].loc[x]=="Red"       
            df['Volume_r'].loc[x]=-1*df['Volume'].loc[x]

        if df['Close'].loc[x]-df['Close'].shift(1).loc[x] < 0:
            df['Close_r'].loc[x]=df['Close'].loc[x]

        if df['Close'].loc[x]-df['Close'].shift(1).loc[x] > 0:
            df['Close_g'].loc[x]=df['Close'].loc[x]

    ##    elif df['Close'].loc[x]-df['Close'].shift(1).loc[x] < 0.1 and df['Close'].loc[x]-df['Close'].shift(1).loc[x] > -0.1:
    ##        df['Close_h'].loc[x]=df['Close'].loc[x]

            
    for x in df.index:
        if df['Volume_g'].loc[x]=='':
            df['Volume_g'].loc[x]=0
        if df['Volume_r'].loc[x]=='':
            df['Volume_r'].loc[x]=0
        if df['Close_g'].loc[x]=='':
            df['Volume_g'].loc[x]=0
        if df['Close_r'].loc[x]=='':
            df['Close_g'].loc[x]=0
        if df['Close_h'].loc[x]=='':
            df['Close_h'].loc[x]=0
     
    df=df.loc[(df['s2'] > '09:00') & (df['s2'] < '16:01')]
    fig,(bx2,bx3,bx4,bx5,bx6,bx7,bx8,bx9) = plt.subplots(8,1,sharex=True)
    fig.suptitle('baba7', fontsize=9)
 
    mclrs=[];mclrs2=[];mclrs3=[];mclrs4=[];mclrs5=[];mclrs6=[]
    
    for x in df.index:

    ##    print(df.loc[x,'Close_vwap'])
        if df.loc[x,'Close_vwap'] < 0:
            mclrs.append('red')
        elif df.loc[x,'Close_vwap'] >= 0:
            mclrs.append('green')
            
        if df.loc[x,'EMA-510'] < 0:
            mclrs2.append('red')
        elif df.loc[x,'EMA-510'] >= 0:
            mclrs2.append('green')
            
        if df.loc[x,'EMA-1021'] < 0:
            mclrs3.append('red')
        elif df.loc[x,'EMA-1021'] >= 0:
            mclrs3.append('green')
            
        if df.loc[x,'EMA-2150'] < 0:
            mclrs4.append('red')
        elif df.loc[x,'EMA-2150'] >= 0:
            mclrs4.append('green')
    ####################################        
##        if df.iloc[x,df.columns.get_loc('MOM')] > 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('green')
##        elif df.iloc[x,df.columns.get_loc('MOM')] > 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('cyan')        
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] > 0:
##            mclrs5.append('red')
##        elif df.iloc[x,df.columns.get_loc('MOM')] < 0 and  df.iloc[x,df.columns.get_loc('MOM')] - df.shift(1).iloc[x,df.columns.get_loc('MOM')] < 0:
##            mclrs5.append('green')

        if df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('green')
        elif df.loc[x,'MOM'] > 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) > 0:
            mclrs5.append('red')
        elif df.loc[x,'MOM'] < 0 and (df.loc[x,'MOM'] - df.shift(1).loc[x,'MOM']) < 0:
            mclrs5.append('red')    
            
            
            
                     
##        if df.loc[x,'Close'] < df.shift(1).loc[x,'Close']:
##            mclrs6.append('blue')
##        elif df.loc[x,'Close'] >= df.shift(1).loc[x,'Close']:
##            mclrs6.append('green')    
        
    import math
    print((df.iloc[:25,df.columns.get_loc('Volume_g')]))
    print(type(df.iloc[25,df.columns.get_loc('Volume_g')]))
# 214


# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    p5a=df.iloc[:,df.columns.get_loc('Close_vwap')]
    bx2.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    bx2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=mclrs,width=2,label='Close_vwap')
    bx2.legend(['Close_vwap'],loc=3, fontsize = 'x-small')
##    if m5.isdigit()==True and m6.isdigit()==True:
##    print(m5,m6,math.atan2(math.radians(m5),math.radians(m6)),'  jjj')
#214
##    dfp=df.loc[df['Close']>df['SAR']]
##    dfg=df.loc[df['Close']<df['SAR']]
##    dfp=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] < 0 ]
##    dfg=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] > 0 ]

    dfp=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] >= 0]
    dfg=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')] < 0]

 
##    print(df.shape,'   ',dfp.shape,'   ',dfg.shape)
##    sys.exit()
##    dfg=df.loc[df.iloc[:,df.columns.get_loc('Close_vwap')]-df.shift(1).iloc[:,df.columns.get_loc('Close_vwap')] < 0 ]
##    bx2.bar(dfp.iloc[:,dfp.columns.get_loc('s2')],dfp.iloc[:,dfp.columns.get_loc('Close_vwap')],color='blue', marker='o', markersize=1)
##    bx2.bar(dfg.iloc[:,dfg.columns.get_loc('s2')],dfg.iloc[:,dfg.columns.get_loc('Close_vwap')],color='yellow', marker='o', markersize=1)
##    bx2.plot(dfg.iloc[:,dfg.columns.get_loc('s2')],dfg.iloc[:,dfg.columns.get_loc('Close_vwap')],color='yellow', marker='o', markersize=1)
##            
## 

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    p5a=df.iloc[:,df.columns.get_loc('EMA-510')]
    bx3.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    
    bx3.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-510')],color=mclrs2,width=2)
    bx3.legend(['EMA-510'],loc=3, fontsize = 'x-small')

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('EMA-1021')]
    bx4.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

    bx4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-1021')],color=mclrs3,width=2)
    bx4.legend(['EMA-1021'],loc=3, fontsize = 'x-small')

# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('EMA-2150')]
    bx5.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
    bx5.legend(['EMA-2150'],loc=3, fontsize = 'x-small')

    bx5.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA-2150')],color=mclrs4,width=2)



# adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p5a=df.iloc[:,df.columns.get_loc('MOM')]
    bx6.fill_between(p1, p5a.min(),p5a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')



    bx6.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('MOM')],color=mclrs5,width=2)
    bx6.legend(['MOM/under const'],loc=3, fontsize = 'x-small')
############### ############### ############### ############### ############### ############### ############### 
############### ############### ############### ############### ############### ############### ###############
############### ############### ############### ############### ############### ############### ############### 
    bx7.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
    
###############  adding adx in close #################
    bx7.vlines(df.iloc[300,df.columns.get_loc('s2')],\
               df.iloc[:,df.columns.get_loc('Close')].min(), \
               df.iloc[:,df.columns.get_loc('Close')].max(),\
               linestyles ="dashed", colors ="k", label = 'test')

    # adx
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]
    

##    print(p2)
##    sys.exit()

    bx7.fill_between(p1, p2a-65,p2a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
    ## where:
    ## p2 = 'adx'
    ## p1 = 's2'
    ## p2a = 'Close'
    ## color #00e5ff = 'blue' [or 'adx' > 40]
## 66 #########################################
##    p1=df.iloc[:,df.columns.get_loc('s2')]
##    p2=df.iloc[:,df.columns.get_loc('macd')] 
##    ax6.plot(df.iloc[:,bb],pd.to_numeric(df.iloc[:,df.columns.get_loc('macd')]))
##
##    ax6.legend(['macd'],loc=3, fontsize = 'x-small')
##    ax6.fill_between(p1, p2, where=(pd.to_numeric(p2) > 0), color='#00FF00')
##    ax6.fill_between(p1, p2, where=(pd.to_numeric(p2) < 0), color='#ff0000')
##    ax6.legend(['macd'],loc=3, fontsize = 'x-small')

    # macd
    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('macd')]
    p2a=df.iloc[:,df.columns.get_loc('Close')]

    bx7.fill_between(p1, p2a-3,p2a, where=(pd.to_numeric(p2) > 0), color='#33ff00')
    bx7.fill_between(p1, p2a-3,p2a, where=(pd.to_numeric(p2) < 0), color='#c3c4c2')
    bx7.legend(['Close/macd/adx>40(breakout)/SAR'],loc=3, fontsize = 'x-small')
    ## where:
    ## p2 = 'macd'
    ## p1 = 's2'
    ## p2a = 'Close'  
    ## color=#33ff00' macd > 0 --- Green.
    ## color='#c3c4c2' macd < 0 -- Grey.


    dfp=df.loc[df['Close']>df['SAR']]
    dfg=df.loc[df['Close']<df['SAR']]
   
    bx7.plot(dfp.iloc[:,bb],pd.to_numeric(dfp.iloc[:,dfp.columns.get_loc('SAR')]+7),color='Green', marker='v', linestyle='dashed',\
                 linewidth=0, markersize=2)
    bx7.plot(dfg.iloc[:,bb],pd.to_numeric(dfg.iloc[:,dfg.columns.get_loc('SAR')]-7),color='Red', marker='^', linestyle='dashed',\
                 linewidth=0, markersize=2)
##    bx7.set_facecolor('xkcd:mint green')
############### ############### ############### ############### ############### ############### ############### 
############### ############### ############### ############### ############### ############### ###############
############### ############### ############### ############### ############### ############### ############### 
###########################################3

    

    bx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Volume_r')],color='red',width=2)
    bx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Volume_g')],color='green',width=2)
    bx8.legend(['Volume'],loc=3, fontsize = 'x-small')
###############  adding adx in close #################
##    bx8.vlines(df.iloc[300,df.columns.get_loc('s2')],\
##               df.iloc[:,df.columns.get_loc('Close')].min(), \
##               df.iloc[:,df.columns.get_loc('Close')].max(),\
##               linestyles ="dashed", colors ="k", label = 'test')

    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('Volume_g')]
    p3a=df.iloc[:,df.columns.get_loc('Volume_r')]

    print(p3a,'  ',p2,'  ',p2a,' =========================================== fffff')
    
##    bx8.fill_between(p1,p3a-5,p3a, where=(pd.to_numeric(p2) > 40), color='#00e5ff')
#########################################################
    bx9.plot(df.loc[:,'s2'],df.loc[:,'VZO'],color='black', marker='o', linestyle='dashed',linewidth=1, markersize=2)
    bx9.legend(['VZO/adx > 40(breakout)'],loc=3, fontsize = 'x-small')

    ##    ax1.hlines(0, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    bx9.hlines(60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    bx9.hlines(40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='black')
    bx9.hlines(-60, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    bx9.hlines(-40, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=1, color='g')
    bx9.hlines(-5, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='green',label='ddd')
    bx9.hlines(15, df.iloc[:,df.columns.get_loc('s2')].min(), df.iloc[:,df.columns.get_loc('s2')].max(), lw=2, color='red')
    



    p1=df.iloc[:,df.columns.get_loc('s2')]
    p2=df.iloc[:,df.columns.get_loc('adx')]
    p2a=df.iloc[:,df.columns.get_loc('VZO')]
    

##    print(p2)
##    sys.exit()
    bx9.fill_between(p1, -100,10, where=(pd.to_numeric(p2) > 40), color='#00e5ff')

###########################################################
    bp1=df.iloc[:,df.columns.get_loc('s2')]
    bp2=df.iloc[:,df.columns.get_loc('squeeze_on')]
    bp2a=df.iloc[:,df.columns.get_loc('VZO')]
    bx9.fill_between(bp1, -100,100, where=(bp2 =='in_squeeze'), color='#00FF00')
##    ax2.fill_between(p1, p2, where=(p2 is None), color='#ff0000')
##    bx9.legend(['squeeze_on'],loc=3, fontsize = 'x-small')



#########################################################
    bx2.set_ylabel('Cl_vwap',loc='top',labelpad=4)
    bx3.set_ylabel('EMA-510',loc='top',labelpad=4)
    bx4.set_ylabel('EMA-1021',loc='top',labelpad=4)
    bx5.set_ylabel('EMA-2150',loc='top',labelpad=4)
    bx6.set_ylabel('EMA-MOM',loc='top',labelpad=4)
    bx7.set_ylabel('Close',loc='top',labelpad=4)
    bx8.set_ylabel('Volume',loc='top',labelpad=4)


###############################################################################
    fig2,(bx20,bx21,bx22,bx2,bx3,bx4,bx5,bx6,bx7,bx8,bx9) = plt.subplots(11,1,sharex=True)
    fig2.suptitle('baba8', fontsize=5)

    clrs2bb=[];clrsb=[];clrs2b=[];clrs3b=[];clrs4b=[];clrs5b=[];clrs6b=[];clrs7b=[]
    for x in df.index:
    ##    print(df.loc[x,'Close_vwap'])
        if df.loc[x,'Close_vwap'] < 0:
            clrs2bb.append('red')
        elif df.loc[x,'Close_vwap'] >= 0:
            clrs2bb.append('green')


        
        if df.loc[x,'EMA_3_vwap'] < 0:
            clrsb.append('red')
        elif df.loc[x,'EMA_3_vwap'] >= 0:
            clrsb.append('green')
            
        if df.loc[x,'EMA_5_vwap'] < 0:
            clrs2b.append('red')
        elif df.loc[x,'EMA_5_vwap'] >= 0:
            clrs2b.append('green')
            
        if df.loc[x,'EMA_10_vwap'] < 0:
            clrs3b.append('red')
        elif df.loc[x,'EMA_10_vwap'] >= 0:
            clrs3b.append('green')
            
        if df.loc[x,'EMA_21_vwap'] < 0:
            clrs4b.append('red')
        elif df.loc[x,'EMA_21_vwap'] >= 0:
            clrs4b.append('green')

        if df.loc[x,'EMA_50_vwap'] < 0:
            clrs5b.append('red')
        elif df.loc[x,'EMA_50_vwap'] >= 0:
            clrs5b.append('green')

        if df.loc[x,'EMA_100_vwap'] < 0:
            clrs6b.append('red')
        elif df.loc[x,'EMA_100_vwap'] >= 0:
            clrs6b.append('green')

        if df.loc[x,'EMA_200_vwap'] < 0:
            clrs7b.append('red')
        elif df.loc[x,'EMA_200_vwap'] >= 0:
            clrs7b.append('green')      


    bx21.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
    bx21.plot(df.iloc[:,bb],(df.iloc[:,df.columns.get_loc('vwap')]),\
             color='blue', marker='o', linestyle='dashed',\
             linewidth=1, markersize=1)

    bx21.legend(['vwap'],loc=3, fontsize = 'x-small')
    bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_3')])
    bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_5')])
    bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_10')])
    ##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_21')])
    ##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_50')])
    ##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_100')])
    ##bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_200')])
    bx20.plot(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close')])
    bx20.legend(['EMA3/EMA5/EMA10/Close'],loc=3, fontsize = 'x-small')

    bx22.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('Close_vwap')],color=clrsb,width=2)
    bx22.legend(['Close_vwap'],loc=3, fontsize = 'x-small')
    bx2.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_3_vwap')],color=clrsb,width=2)
    bx3.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_5_vwap')],color=clrs2b,width=2)
    bx4.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_10_vwap')],color=clrs3b,width=2)
    bx5.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_21_vwap')],color=clrs4b,width=2)
    bx6.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_50_vwap')],color=clrs5b,width=2)
    bx7.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_100_vwap')],color=clrs6b,width=2)
    bx8.bar(df.iloc[:,df.columns.get_loc('s2')],df.iloc[:,df.columns.get_loc('EMA_200_vwap')],color=clrs7b,width=2)              


    bx2.legend(['EMA_3_vwap'],loc=3, fontsize = 'x-small')
    bx3.legend(['EMA_5_vwap'],loc=3, fontsize = 'x-small')
    bx4.legend(['EMA_10_vwap'],loc=3, fontsize = 'x-small')
    bx5.legend(['EMA_21_vwap'],loc=3, fontsize = 'x-small')
    bx6.legend(['EMA_50_vwap'],loc=3, fontsize = 'x-small')
    bx7.legend(['EMA_100_vwap'],loc=3, fontsize = 'x-small')
    bx8.legend(['EMA_200_vwap'],loc=3, fontsize = 'x-small')

    bx21.set_ylabel(['Close','vwap'],loc='top',labelpad=1,fontsize=5)
    bx22.set_ylabel('Close_vwap',loc='top',labelpad=1,fontsize=5)
    bx2.set_ylabel('EMA_3_vwap',loc='top',labelpad=1,fontsize=5)
    bx3.set_ylabel('EMA_5_vwap',loc='top',labelpad=1,fontsize=5)
    bx4.set_ylabel('EMA_10_vwap',loc='top',labelpad=1,fontsize=5)
    bx5.set_ylabel('EMA_21_vwap',loc='top',labelpad=1,fontsize=5)
    bx6.set_ylabel('EMA_50_vwap',loc='top',labelpad=1,fontsize=5)
    bx7.set_ylabel('EMA_100_vwap',loc='top',labelpad=1,fontsize=5)
    bx7.set_ylabel('EMA_200_vwap',loc='top',labelpad=1,fontsize=5)



## 44
##################################################   
##    plt.show()
##    plt2.legend(['Close'])          
##    plt2.show()
    import time
    plt.show()
##    plt.show(block=False)
##    start=time.localtime()
##    plt.pause(3)
##    end=start+(20)
    input("hit[enter] to end.")
    plt.close('all')
    import gc
    gc.garbage.clear()


##            df['EMA-35'] = df['EMA_3'] - df['EMA_5']
##        df['EMA-510'] = df['EMA_5'] - df['EMA_10']
##        df['EMA-1021'] = df['EMA_10'] - df['EMA_21']
##        df['EMA-2150'] = df['EMA_21'] - df['EMA_50']
##        df['EMA_3_vwap'] = df['EMA_3'] - df['vwap']
##        df['EMA_5_vwap'] = df['EMA_5'] - df['vwap']
##        df['EMA_10_vwap'] = df['EMA_10'] - df['vwap']
##        df['EMA_21_vwap'] = df['EMA_21'] - df['vwap']
##        df['EMA_50_vwap'] = df['EMA_50'] - df['vwap']
##        df['macd_35'], df['macdsignal'], df['macdhist'] = ta.MACD(
##        df['Close'], fastperiod=3, slowperiod=5, signalperiod=3)
##        df['Close_EMA3'] = df['Close'] - df['EMA_3']
##        df['Close_EMA5'] = df['Close'] - df['EMA_5']
##        df['Close_EMA10'] = df['Close'] - df['EMA_10']
##        df['Close_EMA21'] = df['Close'] - df['EMA_21']
##        df['Close_EMA50'] = df['Close'] - df['EMA_50']
##        df['Close_vwap'] = df['Close'] - df['vwap']

        
    ##plt.text(df.iloc[:,0],pd.to_numeric(df.iloc[:,1]),'s',horizontalalignment='right')
    ##plt.annotate('k',df.iloc[:,0],pd.to_numeric(df.iloc[:,1]))

##plt.show()
##plt.show(block=False)
##plt.pause(3)
##plt.close()
