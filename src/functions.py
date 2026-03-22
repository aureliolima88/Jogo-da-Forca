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


if __name__ == '__main__':
    criar_matriz()
    desenhar_matriz()
