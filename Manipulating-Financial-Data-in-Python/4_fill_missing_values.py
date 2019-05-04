#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:49:53 2019

@author: yangwh
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fill_missing_values(df_data):
    """Fill missing values in DataFrame, in place."""
    df_data.fillna(method='ffill', inplace=True)
    df_data.fillna(method='bfill', inplace=True)
    return df_data

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files"""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:    # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
        
    for symbol in symbols:
        # read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])
    
    return df

def plot_data(df):
    """Plot stock prices"""
    ax = df.plot(title="Incomplete Data", fontsize=12)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()
    
def test_run():
    # list of symbols
    symbollist = ["JAVA", "FAKE1", "FAKE2"]
    # date range
    start_date = '2005-12-31'
    end_date = '2014-12-07'
    # create date range
    dates = pd.date_range(start_date, end_date)
    # get adjusted close of each symbol
    df_data = get_data(symbollist, dates)
    
    # Fill missing values
    fill_missing_values(df_data)
    
    # plot
    plot_data(df_data)
    
if __name__ == "__main__":
    test_run()