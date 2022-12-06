from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import datetime as dt
import pandas_ta as pta
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
yf.pdr_override()

# In[4]:
stocksymbol=[]
inputdata = int(input("No of companies"))
for i in range(0,inputdata):
  temp = input("Company :")
  stocksymbol.append(temp)
  
stocksymbol = ['TATASTEEL.NS','NFLX','RELIANCE.NS','WIPRO.NS','CIPLA.NS']
val_weight = 1/inputdata
weight=[]
for i in range(0,inputdata):
  weight.append(val_weight)

weight = np.array(weight)
print(type(weight))
# %%
