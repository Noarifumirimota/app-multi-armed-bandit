# Imports.
import numpy as np
import pandas as pd

# Read CSV file and set conversion rates.
conversionRates = pd.read_csv('kn_data.csv',skiprows=1001,nrows=1,usecols=range(2,71))

# Set Number of samples.
N = 1000
d = len(conversionRates)

# Data set.
x = np.zeros((N, d))
print(conversionRates.columns.to_numpy())
# for i in range(N):
#     for j in range(d):
#         if np.random.rand() < conversionRates[j]:
#             x[i][j] = 1