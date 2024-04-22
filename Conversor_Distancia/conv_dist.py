"""

Programa conv_dist

Descrição: Este programa que converte um valor de metros para centimetros.
Autor: Gabriel Peixoto
Data: 12/04/2024
Versão: 0.0.1
"""


#Alocação de memória

metros: float = 0
centimetros: float = 0

#Entrada de dados

metros = float(input("Digite o número em metros "))

#Processamento de dados

centimetros = metros * 100

# Saída de dados

print(f'\n O número em centimetros é {centimetros} cm.')