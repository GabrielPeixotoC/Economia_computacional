'''
Programa: baixa_estoque
Utilidade: Esse programa lê um produto e a quantidade comprada fornecida pelo usuário e realiza a baixa nos estoques.
Data: 29/04/2024
Nome: Gabriel Peixoto
Versão: 0.0.2
Atualizações: Quando o usuário digita a quantidade comprada do que temos em estoque, retorna a quantidade que restou em estoque. Quando o usuário digita um produto fora do estoque, retorna os produtos em estoque.
'''


# Alocação de dados

estoque={ "tomate": [ 1000],
 "alface": [ 500],
 "batata": [ 2001],
 "feijão": [ 100] }
produto = 0
quantidade = 0

# Entrada de dados

produto = input(' Qual foi o produto adquirido? ')
quantidade = float(input('Qual foi a quantidade comprada? '))

# Processamento e saída de dados

if produto in estoque:
    estoque[produto] = estoque[produto][0]-quantidade
    print(f'''
    Nossos estoque foram atualizados.
    Agora possuímos em nossos estoques {estoque[produto]} de {produto}.
    ''')
else:
    print(f'''
    O produto não está em nosso estoque.
    Possuímos em nosso estoque os seguintes produtos: {list(estoque.keys())[:-1]} e {list(estoque.keys())[-1]}.
    ''')