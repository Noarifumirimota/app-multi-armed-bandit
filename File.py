import numpy as np

# Set conversion rates & number of samples.
conversionRates = [0.05, 0.12, 0.09]
n = 1000
l = len(conversionRates)

# Data set.
x = np.zeros((n, l))
for i in range(n):
    for j in range(l):
        if np.random.rand() < conversionRates[j]:
            x[i][j] = 1

# Winners and losers tables.
nPosReward = np.zeros(l)
nNegReward = np.zeros(l)