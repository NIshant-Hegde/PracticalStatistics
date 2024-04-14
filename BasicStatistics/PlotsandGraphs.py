import numpy as np
import pandas as pd
from scipy.stats import *
import wquantiles
from statsmodels import robust
import matplotlib.pyplot as plt


#Plot display toggless
boxplot_show = False
histogram_show = False
histogram_with_Density_show = True

state = pd.read_csv("state.csv")
print(state)
print("\n")

#Box Plot
plt.boxplot(state['Population']/1000000)
plt.ylabel('Population in millions')
if boxplot_show:
    plt.show()

#Frequency Table
#Step 1: Divide the range of Population colum in 10 bins
binnedPopulation = pd.cut(state['Population'], 10)

#Step 2: Return how many values fall with each range
print(binnedPopulation.value_counts())

#Histogram
plt.hist(state['Population']/1000000)
plt.ylabel('Population in millions')
if histogram_show:
    plt.show()

plt.hist(state['Population']/1000000, density=True)
plt.ylabel('Population in millions')
if histogram_with_Density_show:
    plt.show()