 


def entrada_dados():
    '''Pega 4 números digitados pelo usuário'''
    dados =[]
    indice = 1
    for i in range(0, 4):
        dado = float(input(f'Digite o {indice}º número: '))
        dados.append(dado)
        indice +=1      
    return dados

def calculo_media(numeros):
    soma = 0
    for numero in numeros:
        soma = numero + soma
    tamanho = len(numeros)
    media = soma/tamanho
    return media

def imprimir_media(media):
    print(f'A média dos 4 números é {media}')
    
    
def main():
    entrada = entrada_dados()
    media = calculo_media(entrada)
    imprimir_media(media)
    
main()