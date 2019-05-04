#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:49:53 2019

@author: yangwh
"""

import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data
    
def compute_daily_returns(df):
    """Compute and return the daily return values"""
    daily_returns = df.copy()
    daily_returns.iloc[1:,:] = (df.iloc[1:,:]/df.iloc[:-1,:].values) - 1
    daily_returns.iloc[0,:] = 0 # set daily returns for row 0 to 0
    return daily_returns

def test_run():
    
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    #symbols = ['SPY'] 
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    
    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    
    # Plot a histogram
    #daily_returns.hist(bins=20) # change no. of bins to 20
    
    # Get mean and standard deviation
    #mean = daily_returns['SPY'].mean()
    #print("mean =", mean)
    #std = daily_returns['SPY'].std()
    #print("std =", std)
    
    #plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    #plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    #plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    #plt.show()

    # Compute kurtosis
    #print(daily_returns.kurtosis())

    
    # Plot histogram directly from dataframe
    daily_returns['SPY'].hist(bins=20, label="SPY")
    daily_returns['XOM'].hist(bins=20, label="XOM")
    plt.legend(loc='upper right')
    plt.show()
    
    
if __name__ == "__main__":
    test_run()