# Imports.
import numpy as np
import pandas as pd

# Read CSV file and set conversion rates.
conversionRates = pd.read_csv('kn_data.csv',skiprows=1001,nrows=2,usecols=range(1,71))
conversionRates = conversionRates.to_numpy()[0]

# Set Number of samples.
N = 1000
d = len(conversionRates)

# Data set.
x = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            x[i][j] = 1

# Winners and losers tables(for beta). How many times a specific slot machine return positive or negative.
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

# Thompson.
# Thompson stuff.
for i in range(N):
    selected = 0
    maxRandom = 0
    for j in range(d):
        # Beta.
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j

    if x[i][selected] == i:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

# Best machine.
nSelected = nPosReward + nNegReward
for i in range(d):
    print('Machine: ' + str(i + 1) + ' was selected: ' + str(nSelected[i]) + ' times.')
print('Best machine is machine number: ' + str(np.argmax(nSelected) + 1))