@Rozendox_

#Importando a biblioteca numpy.
import numpy as np

#Criando uma matriz unidimensional.
matriz1 = np.array([12,15,18,22])

#Imprimindo a matriz.
print(matriz1)

#Printando o tipo da variável.
print(type(matriz1))

"""
output: 
        [12 15 18 22]
        <class 'numpy.ndarray'>
"""

"""
-Alterando o tipo do array-
*Criando um array do tipo inteiro, e mudando para float*

---A variável arrfloat recebe o array cuja os valores "1","2","3",
Antes do tipo inteiro, passam a se tornar do tipo float---
"""
arrfloat = np.array([1,2,3], dtype = np.float64)

#imprimindo os dados da variável "arrfloat"
print(arrfloat)

#verificando a tipagem da variável "arrfloat"
print(type(arrfloat))

"""
output: 
        [1. 2. 3.]
        <class 'numpy.ndarray'>

"""

