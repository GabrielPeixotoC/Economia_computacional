
"""
Programa raizes_2_grau
Descrição: Este programa que pede os coeficiente a, b e c de um polinômio de segundo grau e determina as raízes deste polinômio.
Autor: Gabriel Peixoto
Data: 25/04/2024
Versao: 0.0.1
"""


#Alocação de dados

a = 0
b = 0
c = 0
raiz_soma = 0
raiz_subtracao = 0

# Entrada de dados

a = float(input('Digite o valor de a: '))
b =  float(input('Digite o valor de b: '))
c =  float(input('Digite o valor de c: '))

# Processamento de dados

raiz_soma = ((b*(-1)) + (b**2 - 4 * a * c)**0.5)/ (2 * a)
raiz_subtracao = ((b*(-1)) - (b**2 - 4 * a * c)**0.5)/ (2 * a)

# Saída de dados

print(f'As raízes de seu polinômio são {raiz_soma:.2} e {raiz_subtracao:.2}.')
