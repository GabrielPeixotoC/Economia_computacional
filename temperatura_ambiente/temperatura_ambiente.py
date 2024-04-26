"""
Programa temperatura_soma
Descrição: Este programa que pergunta a temperatura do ambiente. Se ela for menor que ou igual a 18 graus Celsius, imprime está frio. Se ela estiver de 18 a 28 graus Celsius, imprime está agradável. Se estiver mais do que 28 graus Celsius, imprime está quente
Autor: Gabriel Peixoto
Data: 12/04/2024
Versao: 0.0.1
"""

#alocação de memoria

temperatura: float = 0

#entrada de dados

temperatura = float(input("Qual a temperatura do ambiente? "))

#processamento e saída de dados

if temperatura <= 18:
    print('Está Frio')

elif temperatura > 18 and temperatura < 28:
    print('O clima está agradável')
    
else:
    print('Está quente')