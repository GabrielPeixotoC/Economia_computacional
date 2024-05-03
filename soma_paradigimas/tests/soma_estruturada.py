# Definição de variáveis

i = 0
numeros = [0, 0]
soma = 0 

# Entrada de dados
while i < 2:
    numeros[i] = int(input(f'digite a parcela {i+1}:'))
    i +=1
    
# processamento de dados

for i in numeros:
    soma = soma + i
    
# Saída de dados

print(f'A soma dos numeros é {soma}')