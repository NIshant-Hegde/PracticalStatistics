import numpy as np
import pandas as pd
from scipy.stats import *
import wquantiles
from statsmodels import robust

state = pd.read_csv("state.csv")
print(state)
print("\n")

#Calculating location estimatates - Central Tendencies

# 1. Mean
print("Mean: ",  state['Population'].mean())

# 2. Median
print("Median: ", state['Population'].median())

#3. Trimmed Mean
print("Trimmed Mean: ", trim_mean(state['Population'], 0.1))  #0.1 - Excludes 10% of the smallest and largest data points in the Population column/feature

#4. Weighted Mean
print("Weighted Mean: ", np.average(state['Murder.Rate'], weights=state['Population']))

#5. Weighted Median
print("Weighted Median: ", wquantiles.median(state['Murder.Rate'], weights=state['Population']))

#Calculating Estimates of Variability

#6. Standard Deviation - Square root of variance 
print("Standard Deviation: ", state['Population'].std())

#7 Interquantile Range (IQR) = 75th quantile - 25th quantile
print("Interquantile Range: ", state['Population'].quantile(0.75) - state['Population'].quantile(0.25))

#8 Mean Absolute Deviation (MAD)
print("Mean Absolute Deviation: ", robust.scale.mad(state['Population']))

