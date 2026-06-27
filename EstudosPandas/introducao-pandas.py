import numpy as np
import pandas as pd

g7_pop = pd.Series([35.467,63.951,80.940,60.655,127.061,64.511,318.523])

print(g7_pop)

g7_pop.name = "G7 poppulation in millions"

print(g7_pop)

print(g7_pop.dtype)
print(g7_pop.values)
print(type(g7_pop.values))

print(g7_pop[0])
print(g7_pop[1])

print(g7_pop.index)

g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'Brasil',
    'Usa'
]

print(g7_pop)
print(g7_pop.index)


# Index
print(g7_pop['Canada'])
print(g7_pop['Japan'])
print(g7_pop.iloc[0])
print(g7_pop.iloc[-1])
print(g7_pop[['Italy', 'Germany']])
print(g7_pop.iloc[[0,-1]])

# Boolean Arrays
print(g7_pop > 70)
print(g7_pop[g7_pop > 70])
print(g7_pop.mean())
print(g7_pop[g7_pop > g7_pop.mean()])
print(g7_pop.std())
print(g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)])

# Operation Methods
print(g7_pop * 1_000_000)
print(g7_pop.mean())
print(np.log(g7_pop))
print(g7_pop['France' : 'Italy'].mean())

# Modifying Series
g7_pop['Canada'] = 40.5
print(g7_pop)

g7_pop.iloc[-1] = 500
print(g7_pop)

g7_pop[g7_pop < 70] = 90.5
print(g7_pop)
