'''
Programa: buscador_string
Nome: Gabriel Peixoto
Função: Procura se uma string está contida dentro de outra.
Versão: 0.0.1




'''

# entrada de dados

string_1 = 'AAABBBBEEEEEEJJJJJJ'
string_2 = 'BE'
posicao = 0


# Processamento dos dados
if string_2 in string_1:
    posicao = string_1.find(string_2)
else:
    print('A string 2 não está dentro da string 1')
    
# saída de dados
print(f'''
{string_2} foi encontrada na posição {posicao} de {string_1}
''')