"""
Programa soma
Descrição:Esse programa lê deois número interiores Digitados pelo usuário e põe na tela e soma deles.
Autor: Gabriel Peixoto da Costa
Data: 12/04/2024
Versao: 0.0.1
"""


# Alocação de memória

numero_1: int = 0
numero_2: int = 0
soma: int = 0


# Entrada de dados

numero_1 = int(input('Digite o primeiro número'))
numero_2 = int(input('Digite o segundo número'))


# Processamento de dados

soma = numero_1+numero_2

# Saída de dados

print(soma)