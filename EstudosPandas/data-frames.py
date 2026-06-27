import numpy as np
import pandas as pd

"""
As colunas do dataframe são como series, ou seja cada dataframe é uma combinação de series
"""

df = pd.DataFrame({
    'Population' : [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    'GDP' : [1785387, 2833687, 3874437, 2167744, 4602367, 2950039, 17348075],
    'Surface Area' : [9984660, 640679, 357114, 301336, 377930, 242495, 9525067],
    'HDI' : [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
    'Continent' : ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America'] 
} ,columns= ['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

print(df)

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'UK',
    'USA'
]

print(df)
print(df.columns)
print(df.index)
print(df.info)
print(df.size)
print(df.shape)
print(df.describe())
print(df.dtypes)
print(df.dtypes.value_counts())

# Index, Slicing and Selection
print(df['Population'])
print(df.iloc[-1])
print(df['Population'].to_frame())
print(df[['Population', 'GDP']])

print(df[1:3])
print(df.loc['Italy'])
print(df.loc['France' : 'Italy', 'Population'])
print(df.loc['France' : 'Italy', ['Population', 'GDP']])

print(df.iloc[0])
print(df.iloc[-1])
print(df.iloc[[0,1,-1]])
print(df.iloc[1:3])
print(df.iloc[1:3, 3])
print(df.iloc[1:3, [0,3]])
print(df.iloc[1:3, 1:3])

# Conditional Selection
print(df['Population'] > 70)
print(df.loc[df['Population'] > 70])
print(df.loc[df['Population'] > 70, 'Population'])
print(df.loc[df['Population'] > 70, ['Population', 'GDP']])

# Dropping
# Não muda a tabela, cria uma nova sem os valores pedidos
print(df.drop('Canada'))
print(df.drop(['Canada', 'Japan']))
print(df.drop(columns=['Population', 'GDP']))
print(df.drop(['Italy', 'Canada'], axis=0))
print(df.drop(['Population', 'HDI'], axis=1))
print(df.drop(['Population', 'HDI'], axis='columns'))
print(df.drop(['Canada', 'Germany'], axis='rows'))

# Operations
print(df[['Population', 'GDP']])
print(df[['Population', 'GDP']] / 100)

crisis = pd.Series([-1_000_000, -0.3], index= ['GDP', 'HDI'])

print(df[['GDP', 'HDI']] + crisis)

# Modfying DataFrames
langs = pd.Series(
    ['French','German', 'Italy'],
    index=['France', 'Germany', 'Italy'], # mesmo index das colunas desejadas
    name='Language'
)

df['Language'] = langs
print(df)

# Replace value per column
df['Language'] = 'English'
print(df)

# Renaming collumns
df = df.rename(columns=
    {'HDI': 'Human Development Index',
    'Anual Popcorn Consuption': 'APC'},
    index={
        'USA' : 'United States',
        'UK' : 'United Kingdom',
        'Argentina' : 'AR',
    }
)
print(df)

print(df.rename(index=str.upper))
print(df.rename(index=lambda x: x.lower()))

# Dropping columns
df.drop(columns='Language', inplace=True)
print(df)

# Adding values
"""
dataframe.append não existe mais. Para realizar a operação usar pd.concat com duas colunas como no exemplo a abaixo

df.append(pd.Series({
    'Population' : 3,
    'GDP' : 5,
}, name='China')) ---> removido

"""
dfNew = pd.DataFrame({
    'Population' : 3,
    'GDP' : 5
}, columns=['Population', 'GDP'], index=['China'])

df = pd.concat([df, dfNew])
print(df)

df = df.drop('China')
print(df)

# Radical Index Changing
print(df.reset_index())
print(df.set_index('Population'))

# Creating columns from other columns
print(df[['Population','GDP']])

print(df['GDP'] / df['Population'])
df['GDP per Capita'] = df['GDP'] / df['Population']
print(df)

# Statistical Info
print(df.head())
print(df.describe())

population = df['Population']

print(population.min())
print(population.max())

print(population.sum())

print(population.sum() / len(population))
print(population.mean())

print(population.std())
print(population.median())
print(population.describe())
print(population.quantile(.25))
print(population.quantile([.2,.4,.6,.8,1]))
