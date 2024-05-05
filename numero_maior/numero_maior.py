'''
Programa: Número Maior
Função: Returna o maior de número de uma série de dois.
Nome: Gabriel Peixoto
Versão:0.0.1



'''

def num_maior(a, b):
    '''Essa função retorna o maior de dois números.'''
    if a > b:
        return f'O número {a} é o maior!'
    if a < b:
        return f'O número {b} é o maior!'
    if a == b:
        return 'Os números são iguais'