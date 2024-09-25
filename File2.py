# Imports.
import numpy as np

# Set conversion rates & number of samples.
conversionRates = [
    0.08, 0.25, 0.25, 0.17, 0.11
]
N = 10
d = len(conversionRates)

# Data set.
x = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            x[i][j] = 1

print(x)