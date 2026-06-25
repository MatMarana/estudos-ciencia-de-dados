import sys

import numpy as np

# CRIANDO UM ARRAY

array = np.array([1,2,3,4]) # Cria um array
array = np.arange(5) # Cria um array com indíce 5
print(array)
print(array[0],array[1])

# SLICING

print(array[:2]) # Separa até o elemento 2
print(array[1:]) # Separa do 1 em diante
print(array[1:4]) # Separa os elemetos do indíce 1 ao 4

#TIPOS DOS ARRAYS

print(array.dtype) # Mostra o tipo do array
b = np.array([1,2,3,4,5], dtype= np.float64) # Definindo o tipo de um array
print(b.dtype)
c = np.array(['a', 'b', 'c']) # Strings
print(c.dtype)
d = np.array([{'a':1}, sys]) # Objetos se pode armazenar, mas não há porquê, afinal é uma biblioteca de porcessamento numérico
print(d.dtype)

# MATRIZES

M = np.array([[1,2,3],   # Matriz 3x3
             [4,5,6],
             [7,8,9]])             
print(M.shape) # formato da matriz
print(M.ndim) # dimensão da matriz
print(M.size) # tamanho da matriz

N = np.array([    # Matriz 2x2x3
    [
        [10,11,12],
        [13,14,15]
    ],
    [
        [16,17,18],
        [19,20,21]
    ]
])
print(N.dtype)
print(N.shape) # formato da matriz
print(N.ndim) # dimensão da matriz
print(N.size) # tamanho da matriz

print(type(N[0])) #Tipo da matriz N na posição 0
print(type(N[0][0])) #Tipo da matriz N na posição 0 0 
print(type(N[0][0][0])) #Tipo da matriz N na posição 0 0 0 

#SLICING EM MATRIZES

print(N[0])
print(N[0][0])
print(N[0][0][0])
print(N[0][1][1:3])
print(N[:][:2][:2])

#Estatíscas do numpy

s = np.array([1,2,3,4,5,6])

r = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

print(s.sum()) # soma dos elementos
print(s.mean()) # media dos elementos
print(s.std()) # desvio padrão

print(r.sum()) # soma dos elementos
print(r.mean()) # media dos elementos
print(r.std()) # desvio padrão
print(r.sum(axis=0)) # soma das linhas
print(r.sum(axis=1)) # soma das colunas