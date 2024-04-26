"""
Programa: calculo_media_notas
Nome: Gabriel Peixoto
Data: 26/04/2024
Versão: 0.0.1
Problema: Esse programa calcula a média de 7 notas fornecidas pelo usuário e imprime na tela.

"""


#alocação de memória
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
indice = 0
media = 0

# entrada e processamento de dados

while indice<7:
    notas[indice]=float(input(f'Digite a Nota {indice + 1}'))
    soma += notas[indice]
    indice += 1
    
media = soma/indice

#Saída de dados

print(f'Média: {media}')