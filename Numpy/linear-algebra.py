import sys
import time

import numpy as np

# Utilizando numpy em matrizes

matrix_1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

matrix_2 = np.array([
    [6,5],
    [4,3],
    [2,1]
])

print(matrix_1)
print(matrix_2)

print(matrix_1.dot(matrix_2))
print(matrix_1@matrix_2)

print(matrix_2.T)

print(matrix_2.T @ matrix_1)

# Calculanto tempo de execução e tamanho dos objetos na memória

print(sys.getsizeof(1)) # tamanho de um inteiro no python

print(sys.getsizeof(10**100))

print(np.dtype(int).itemsize) # tamanho de um inteiro em numpy

print(np.dtype(float).itemsize)

print(sys.getsizeof([1])) # tamanho de uma lista com um inteiro em python

print(np.array([1]).nbytes) # tamanho de uma lista com um inteiro no numpy

a = np.arange(1000)

inicio = time.perf_counter()

np.sum(a**2)

fim = time.perf_counter()

print(f"Tempo: {fim - inicio:.6f} s")

l = list(range(1000))

inicio = time.perf_counter()

for i in l:
    i = i**2

sum(l)

fim = time.perf_counter()

print(f"Tempo: {fim-inicio:.6f} s")

