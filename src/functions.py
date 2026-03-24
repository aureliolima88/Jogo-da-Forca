#funções responsaveis por transformar um instring em lista e retornar como matriz para
#fazer o desenho do boneco do jogo

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

def menu():
    print(f'{'':=^20}')
    print('JOGO DA FORCA'.center(20))
    print(f'{'':=^20}')

def campeao():
    trofeu = r"""
       ___________
      '._==_==_=_.'
      .-\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \::.    /
         '::. .'
           ) (
         _.' '._
        '-------'
"""
    return trofeu

def derrota():
    caveira = r"""
          ______
       .-"      "-.
      /            \
     |  GAME  OVER  |
     |,  .-.  .-.  ,|
     | )(__/  \__)( |
     |/     /\     \|
     (_     ^^     _)
      \__|IIIIII|__/
       | \IIIIII/ |
       J          L
"""
    return caveira

if __name__ == '__main__':
    criar_matriz()
    desenhar_matriz()
    menu()
    campeao()
    derrota()