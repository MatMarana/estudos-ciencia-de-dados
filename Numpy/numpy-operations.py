import numpy as np

"""
Para fazer uma multiplcação dos elementos de uma lista em python
é necessário utilizar o for. Caso não seja utitiluzado a lista
apenas é repetida dentro dela mesma
"""
print("----LISTA-----")
lista = [0,1,2,3,4]
print(lista)

for i in range (len(lista)):
    lista[i] = i*10

print(lista)

# Quando utilizamos a lista * 2
print(lista*2)

"""
Utlizar um array em numpy é consideravelmente mais rápido e performático
que utilizar listas em python.

Isso acontece pois os arrays são armazenados de maneira contígua na memória
Como feito em C, tornado o acesso a elementos otimizado
"""

print("----ARRAY-----")

# montar um array com x elementos
array = np.arange(5) # x = 5
print(array)

# OPERAÇÕES COM ARRAY EM NUMPY

# soma
print(array + 10)

# multiplicação
print(array * 10)

# alteração de valores
array += 100
print(array)

# OPERAÇÕES COM ARRYS DIFERENTES
b = np.arange(4)
c = np.array([5,6,7,8])

print(b+c)

print(b*c)
