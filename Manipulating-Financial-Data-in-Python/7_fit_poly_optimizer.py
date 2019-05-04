#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:49:53 2019

@author: yangwh
"""

"""Fit a polynomial to a given set of data points using optimization."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def error_poly(C, data):
    """Compute error between given polynomial and observed data.
    
    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficients
    data: 2D array where each row is a point (x, y)
    """
    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:,1] - np.polyval(C, data[:,0])) ** 2)
    return err

def fit_poly(data, error_func, degree=4):
    """Fit a polynomial to given data, using a supplied error function.
    
    Parameters
    ---------
    data: 2D array where each row is a point (X, Y)
    error_func: function that computes the error between a polynomial and observed data
    
    Returns polynomial that minimizes the error function.
    """
    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree+1, dtype=np.float32))
    
    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")
    
    # Call optimizer to minimize error function
    result = spo.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x) # convert optimal result into a poly1d object and return
    

def test_run():
   # Define original polynomial
   Corig = np.poly1d(np.float32([1.5, -10, -5, 60, 50]))
   print("Original polynomial:\n{}".format(Corig))
   Xorig = np.linspace(-5, 5, 21)
   Yorig = np.polyval(Corig, Xorig)
   plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")
   
   # Generate noisy data points
   noise_sigma = 30.0
   noise = np.random.normal(0, noise_sigma, Yorig.shape)
   data = np.asarray([Xorig, Yorig + noise]).T
   plt.plot(data[:, 0], data[:, 1], 'go', label = "Data points")
   
   # Try to fit a line to this data
   p_fit = fit_poly(data,error_poly)
   print("Fitted poly:\n{}".format(p_fit))
   plt.plot(data[:, 0], np.polyval(p_fit, data[:, 0]), 'r--', linewidth = 2.0, label = "Fitted line")
   
   
   plt.legend(loc = 'upper right')
   plt.show()


if __name__ == "__main__":
    test_run()