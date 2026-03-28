#funções responsaveis por transformar um instring em lista e retornar como matriz para
#fazer o desenho do boneco do jogo
import os
import storage
from random import choice

#responsável por transformar o texto em uma lista aninhada
def criar_matriz(matriz_local):
    matriz = []
    
    for forca in matriz_local.splitlines():
        matriz.append(list(forca))
        
    return matriz

# função que desenha o que estiver na matriz na tela
def desenhar_matriz(matriz_atual):
    for linha in matriz_atual:
      print(''.join(linha))

#cabeçalho
def head():
    print(f'{'':=^20}')
    print('JOGO DA FORCA'.center(20))
    print(f'{'':=^20}')

#menu
def menu():
    print('=' * 20)
    print('MENU'.center(20))
    print('=' * 20)
    print('- FACIL')
    print('- MEDIO')
    print('- DIFICIL')
    print('=' * 20)
    print()


def palavra_chave(opcao):
    global dados
    dados = storage.ler_arquivo()
    if opcao in dados:
        nivel = choice(list(dados[opcao]))
    return nivel.upper()

def dica(informacao, chave):
    for item in dados[informacao]:
        if item.upper() == chave:
            dica = dados[informacao][item]
    return dica.upper()

# def palavra_chave():
#     global dados
#     dados = storage.ler_arquivo()
#     menu()
#     while True:
#         opcao = input('Digite um Nivel: ').lower().strip()
#         if opcao.isnumeric() or opcao not in dados:
#             print('opção invalida, tente novamente')
#         else:
#             nivel = choice(list(dados[opcao])) #retorna a palavras referente ao nivel escolhido
#             os.system('cls')
#             break
#     return nivel.upper()

if __name__ == '__main__':
    criar_matriz()
    desenhar_matriz()
    head()
    menu()
    palavra_chave()
    dica()
