import random
import statistics as sta
import matplotlib.pyplot as plt

def CVCalc(data):
    ''' Calculation of the Cofficient of Variation.
        data: Input data
    '''
    return sta.stdev(data) / sta.mean(data)

# Population data
PopData = list()
# Random seed
random.seed(5)
N = 100

# Gathering N-random numbers
for _ in range(N):
    # Getting a random number between 0..10
    DataItem = random.random() * 10
    PopData.append(DataItem)

# Calculating of coefficient of variation of the population data
CVPopData = CVCalc(PopData)
print(f'Coefficient of variation on Population Data: {CVPopData}')

JackVal = list()
PseudoVal = list()

# Initializing the JackKnife sub-sampling with 0-value
for _ in range(N - 1):
    JackVal.append(0)

# Initializing the Pseudo values sub-sampling with 0-value
for _ in range(N):
    PseudoVal.append(0)

# Looping for N-Pseudo values
for i in range(N):
    # Looping for N-1 sub-sampling items
    for j in range(N - 1):
        if (j < i):
            JackVal[j] = PopData[j]
        elif (j > i):
            JackVal[j - 1] = PopData[j]
    # Calculating the dispersion of the CV* with resampling-CV
    PseudoVal[i] = N * CVPopData - (N - 1) * CVCalc(JackVal)

# Show the population dispersion
plt.hist(PseudoVal)
plt.show()

# Show the statistics data
print(f'Mean: {sta.mean(PseudoVal)}')
print(f'Variance: {sta.variance(PseudoVal)}')
print(f'JackKnife Variance: {sta.variance(PseudoVal) / N}')
