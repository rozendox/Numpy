
#Criando uma matriz Bidimensional
MatrizBid = np.array([[3,5,7],[7,5,3],[2,4,6]])

#Imprimindo os dados da variável "MatrizBid"
print(MatrizBid)

"""
output: 
        [[3 5 7]
         [7 5 3]
         [2 4 6]]
"""
"""
Criando uma variável que recebe os valores da matriz 1 com os dados 
Convertidos para float
"""

MatrizBid2 = MatrizBid.astype(float)

#Imprimindo os Valores da Variável MatrizBid2
print(MatrizBid2)

"""
output: 
        [[3. 5. 7.]
         [7. 5. 3.]
         [2. 4. 6.]]
"""

#Criando uma matriz Bidimensional do tipo float

mtzbf = np.array([[3.1 , 4.2 , 6.7], [7.2 , 5.4 , 3.9], [9.2, 10.2, 67.2] ])

#Imprimindo os dados da variável "mtzbf"
print(mtzbf)

"""
output: 
        [[ 3.1  4.2  6.7]
         [ 7.2  5.4  3.9]
         [ 9.2 10.2 67.2]]
"""
"""
Criando uma variável que recebe os valores da mtzbf,
E transforma o tipo de float para int.
"""

mtzbf2 = mtzbf.astype(int)

#Imprimindo os valores da variável mtzbf2
print(mtzbf2)

#Imprimindo o tipo da variável mtzbf2
print(type(mtzbf2))

"""
output: 
        [[ 3  4  6]
         [ 7  5  3]
         [ 9 10 67]]

     <class 'numpy.ndarray'>
     

"""


"""
Criando arrays Vazios Tipificados
O empty significa que eles não são inicializados
não que são vazios
"""

emp = np.empty([3,2], dtype = int)

#Imprimindo os Valores da Variável "emp"
print(emp)

"""
(vale reassaltar que os valores do output 
 serão aleatórios)

output: 
       [[6029409 7209025]
        [6488161 7209071]
        [6357092 6029363]]
""" 

#Criando uma matriz 3x3 com valores zero
zero = np.zeros([3,3])

#Imprimindo os Valores da Variável "zero"
print(zero)

"""
output: 

       [[0. 0. 0.]
        [0. 0. 0.]
        [0. 0. 0.]]
""" 

#Criando uma matriz 4x2 com valores iguais a um

unos = np.ones([4,2])

#Imprimindo os Valores da Variável "unos"
print(unos)

"""
output: 

        [[1. 1.]
         [1. 1.]
         [1. 1.]
         [1. 1.]]
"""


"""
Criando uma matriz quadrada com diagonal principal
contendo valores 1 e os outros valores 0
"""

diag1 = np.eye(5)

#Imprimindo os valores da variável "diag1"
print(diag1)

"""
output: 

      [[1. 0. 0. 0. 0.]
       [0. 1. 0. 0. 0.]
       [0. 0. 1. 0. 0.]
       [0. 0. 0. 1. 0.]
       [0. 0. 0. 0. 1.]]
       
       
"""

#Criando valores entre zeros e uns
aleat = np.random.random((5))
print(aleat)


"""
output: 

        [0.52724901 0.10202178 0.3079136  0.93807065 0.78919295]
        
        
"""


#Valores aeatórios contendo negativos
aleat2 = np.random.randn((5))
print(aleat2)

"""
output: 

       [ 0.29244046  1.25815897  0.04045272 -0.63142693 -0.443084  ]
  
  
  
"""
