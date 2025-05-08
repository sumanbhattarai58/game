import numpy as npy
import pandas as pds
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Generating Sample Data
npy.random.seed(42)
x = npy.random.rand(10) * 2
y = 3 * x + npy.random.normal(0, 3, 10)  # Linear relation with noise
data = pds.DataFrame({'X': x, 'Y': y})
print(data)