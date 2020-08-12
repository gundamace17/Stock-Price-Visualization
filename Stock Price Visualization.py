# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:02:49 2020

@author: gunda
"""

# Import Libraries
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

# For Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# For reading stock data from yahoo
from pandas_datareader import data

# For time stamps
from datetime import datetime

# Create the list of Target Stock
# tech_list = ['AMD', 'BTC-USD', 'GOLD', 'CL=F']

# Set up the time scale from the start to the end
end = datetime.now()
start = datetime(end.year-20, end.month, end.day)

# Use DataReader to get the data from Yahoo
# for stock in tech_list:
#     globals()[stock] = data.DataReader(stock, 'yahoo', start, end)

# Use DataReader to get the data from Yahoo and
# rename the new ADJ Close column to avoid the confusing
# of each Stock    
BTC = data.DataReader('BTC-USD', 'yahoo', start, end)
Crude_Oil = data.DataReader('CL=F', 'yahoo', start, end)
AMD = data.DataReader('AMD', 'yahoo', start, end)
GOLD = data.DataReader('GOLD', 'yahoo', start, end)
BTC['BTC Adj Close'] = BTC['Adj Close']
Crude_Oil['Crude_Oil Adj Close'] = Crude_Oil['Adj Close']
AMD['AMD Adj Close'] = AMD['Adj Close']
GOLD['GOLD Adj Close'] = GOLD['Adj Close']

# Concatenate all of the Stock data together
df_list = [AMD['AMD Adj Close'], GOLD['GOLD Adj Close'], Crude_Oil['Crude_Oil Adj Close']]
Bob_HW_0 = pd.concat(df_list, axis = 1)
# Join the BTC data seperately due to the different time scale
Bob_HW = Bob_HW_0.join(BTC['BTC Adj Close'])
Bob_HW

# Due to the different of scales between Stocks and BTC
# The plots should be made seperately or BTC would dominate the whole plot
# Set up two axis for two plots
f, (axis1, axis2) = plt.subplots(2, 1, figsize = (12, 8))

# Bob_HW_0 for AMD, GOLD, Crude-Oil will be plotted in the axis1 and BTC in axis2
# Set up xy labels and the limit
Fig1 = Bob_HW_0.plot(ax = axis1)
Fig1.set(ylabel = 'Price', xlim = ('2000', end), xlabel = '')
Fig2 = Bob_HW['BTC Adj Close'].plot(y = 'Price',ax = axis2, color = 'orange')
Fig2.set(ylabel = 'Price', xlim = ('2000', end))
Fig2.legend()