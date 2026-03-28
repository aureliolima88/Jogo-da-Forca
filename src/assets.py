#Desenhos da Forca para apresentar no terminal

def forca():
    enforcado ="""
=====
x   |    
x        
x        
x        
============
"""
    return enforcado

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

def jogo_da_forca():
    cabecalho =r"""
#######################
#    JOGO DA FORCA    #
#######################
"""
    return cabecalho

if __name__ == '__main__':
    forca()
    campeao()
    derrota()
    jogo_da_forca()