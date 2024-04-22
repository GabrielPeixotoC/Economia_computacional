"""
Programa soma
Descrição:Esse programa lê dois número interiores Digitados pelo usuário e põe na tela e soma deles.
Autor: Gabriel Peixoto da Costa
Data: 12/04/2024
Versao: 0.0.2
"""


# Alocação de memória

i: int = 0
numero: int = 0
soma: int = 0


# Entrada e processamento de dados

while i < 2:
    numero = int(input(f"Digite o primeiro número {i+1}: "))
    soma += numero
    i += 1

# Saída de dados

print(f"A soma dos números digitados é igual a {soma}!")