

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

import warnings
import sys
from datetime import date
import datetime
from datetime import timedelta
from dateutil import parser
from dateutil import parser
import s3
import s5c
import s6
import s4


 
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 76
pd.set_option("display.max_columns", 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

gg5 = []


warnings.filterwarnings("ignore")

pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_columns = 255
pd.options.display.max_rows = 6500000

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 36
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 0)
pd.set_option('display.max_columns', None)



df7a=pd.DataFrame()
df7a=pd.DataFrame(columns=['stragety','Date','ticker','Buy_at','Sell_at','Profit','b_Close_vwap','b_macd','b_mom','b_VZO','b_CCI'])

df8=pd.DataFrame()
df9=pd.DataFrame()
df9a=pd.DataFrame()
#################################################################
u33,y , x2,ATR_target,adx_target,d2,d3,gt4=s3.vv(df7a,df8,df9,df9a)

u33,y,d2,d3,df=s4.s4(u33,y , x2,ATR_target,adx_target,d2,d3)
u33,df=s5c.s5c(u33,y,d2,d3,df)
df,df7a=s6.s6(df,u33,df7a)

##u33,y,d2,d3,gt4=s3.bb(df7a,df8,df9,df9a)
##u33,dfd=s5c.s5c(u33,y,d2,d3,gt4)
##df,df7a=s6.s6(dfd,u33,df7a)
#################################################################
print(df)
print('\n')
print(df7a,'ddd')
##df9=df9a.append(df8)
##print(df9,' df9a ==================stupid ======================')
##print('pppp')

