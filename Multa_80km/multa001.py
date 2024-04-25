"""
Programa Multa
Descrição: Este programa que pergunta ao usuário a sua velocidade e, se for acima de 80km/h, retorna uma multa cinco vezes o valor excedido do limite de velocidade.
Autor: Gabriel Peixoto da Costa
Data: 25/04/2024
Versao: 0.0.1
"""

#Alocação de memória
velocidade = 0
velocidade_lim = 80
multa = 0

#Entrada de dados
velocidade = float(input("Qual a velocidade do carro? "))

#Processamento e saída de dados
if velocidade > velocidade_lim:
    multa = (velocidade - velocidade_lim) * 5
    print(f'Voce foi multado em R${multa}.')
else:
    print('Parabéns, você seguiu o limite de velocidade!')