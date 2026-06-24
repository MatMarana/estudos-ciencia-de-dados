import numpy as np 

# Boolean arrays também são chamados de máscaras

"""
Quando temos um array podemos acessar os elementos deles através de
array[índice].

Podemos também utlizar arrays como índices, fazendo com que o retorno
seja um array somente com os elementos desejados
"""

array = np.arange(4)
print(array)

print(array[[1,-1]])

print(array[[True, False, False, True]])

# Se utilizarmos uma expressão booleana com o array
# O retorno é um array booleano com o resultado da expressão
print(array >= 2)

# Podemos utlizar a expressão booleana como parâmetro
# O retorno são os elemetos do array que satifazem essa expressão
print(array[array>=2])

# Exemplo com a média
media = array.mean()
print(f"media = {media}")
print(array[array>=media])

# Conseguimos utlizar operadores lógicos na expressão
print(array[~(array > media)]) # NOT

print(array[(array > 2) & (array >= media)]) # AND

print(array[(array > media) | (array < 1)]) # OR

# MATRIZES

matriz = np.random.randint(100, size=(3,3))
print(matriz)

print(matriz > 30)

print(matriz[matriz>30])

# UTILIZANDO DOIS ARRAYS
c = np.arange(6)
d = np.array([1,2,3,4,5,6])

print(c)
print(d)

print(d[c<3])