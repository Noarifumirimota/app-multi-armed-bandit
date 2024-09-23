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

# Winners and losers tables. How many times a specific slot machine returns 0 or 1 in previous rounds.
nPosReward = np.zeros(l)
nNegReward = np.zeros(l)

# Thompson.
for i in range(n):
    selected = 0
    maxRandom = 0
    for j in range(l):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j
    if x[i][selected] == i:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

# Print best slot machine.
nSelected = nPosReward + nNegReward
for i in range(l):
    print('Machine: ' + str(i + 1) + ' was selected: ' + str(nSelected[i]) + ' times.')
print('Best machine is machine number: ' + str(np.argmax(nSelected) + 1))