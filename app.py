#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import datetime as dt
import pandas_ta as pta
import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use('ggplot')
yf.pdr_override()



# In[4]:
stocksymbol=[]
investment = int(input("Enter the amount you are planning to invest"))
inputdata = int(input("No of companies"))
# for i in range(0,inputdata):
#   temp = input("Company :")
#   stocksymbol.append(temp)
  
stocksymbol = ['TATASTEEL.NS','NFLX','RELIANCE.NS','WIPRO.NS','CIPLA.NS']
val_weight = 1/inputdata
weights=[]
for i in range(0,inputdata):
  weights.append(val_weight)
weights = np.array(weights)
end = dt.datetime.now()
start = end - dt.timedelta(days = 1460)

data = pdr.get_data_yahoo(stocksymbol, start = start, end = end)['Adj Close']


# In[5]:



# In[6]:


plt.rcParams["figure.figsize"] = [8.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
fig.subplots_adjust(bottom=0.1)
for i in data.columns.values:
    plt.plot(data[i], label = i)
plt.title('Adj.Close History')
plt.xlabel('Year', fontsize = 18)
plt.ylabel('Adj.Close(in $)',fontsize = 18)
plt.legend(data.columns.values, loc = 'upper left')
plt.savefig('foo.png')



# In[7]:


returns = data.pct_change()
print(returns)


# In[8]:


cov_matrix = returns.cov()*252
print(cov_matrix)


# In[9]:


variance = np.dot(weights.T, np.dot(cov_matrix, weights))
round(variance, 3)


# In[10]:


volatility = np.sqrt(variance)
round(volatility, 4)


# In[14]:


simple_return = np.sum(returns.mean() * weights) * 251
round(simple_return, 4)


# In[16]:


perc_var = str(round(variance, 4) * 100) + '%'
print('Annual Variance : ' + perc_var)
perc_vola = str(round(volatility, 3) * 100) + '%'
print('Annual Volatility(risk) : ' + perc_vola)
perc_returns = str(round(simple_return, 4) * 100) + '%'
print('Annual Returns : ' + perc_returns)


# In[21]:


from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


# In[22]:


mu = expected_returns.mean_historical_return(data)
S = risk_models.sample_cov(data)
ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()
print(cleaned_weights)
ef.portfolio_performance(verbose = True)


# In[29]:


from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices


# In[31]:


latest_prices = get_latest_prices(data)
weights = cleaned_weights
disalloc = DiscreteAllocation(weights, latest_prices, total_portfolio_value = investment)
allocation, leftover = disalloc.greedy_portfolio()
print('Discrte Allocation : ', allocation)
print('Funds Remaining : {:.2f}$'.format(leftover))

print('#####################################33')
print(type(allocation))
print('#####################################33')
print(type(leftover))






ls = list(allocation.items())

print(ls)
