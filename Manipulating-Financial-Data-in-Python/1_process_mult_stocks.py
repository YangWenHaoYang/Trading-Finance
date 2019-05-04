#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 00:16:27 2019

@author: yangwh
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

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

def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe"""
    return df/df.iloc[0,:]

def plot_data(df, title="Stock prices"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()
    
def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in given range."""
    df_slice = df.loc[start_index:end_index, columns]
    plot_data(df_slice, title='Selected data')
    
def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')
    
    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']    # SPY will be added in get_data()
    
    # Get stock data
    df = get_data(symbols, dates)
    
    # Slice by row range (dates) using DataFrame.ix[] selector
    #print(df.loc['2010-01-01': '2010-01-31', :]) # the month of January
    
    # Slice by column (symbols)
    #print(df['GOOG'])   # a single label selects a single column
    #print(df[['IBM', 'GLD']])   # a list of labels selects multiple columns
    
    # Slice by row and column
    #print(df.loc['2010-03-10':'2010-03-15', ['SPY', 'IBM']])
    
    # Slice and plot
    #plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')
    
    df_norm = normalize_data(df)
    plot_data(df_norm, title="Normalized prices")
    
    
    
if __name__ == "__main__":
    test_run()