#toda estrutura do jogo
from functions import criar_matriz, desenhar_matriz
import os

palavra_secreta = 'Python'.upper()
letras_secreta = []
matriz = []
erro = 0
texto ="""
=====
x   |    
x        
x        
x        
============
"""
minha_matriz = criar_matriz(texto)

while True:

   desenhar_matriz(minha_matriz)

   opcao = input('digite uma letra: ').strip().upper()
   os.system('cls')
   
   if len(opcao)>1 or isinstance(int, float):
      print('Opção Invalida! Tente novamente.')
      continue

   if opcao in palavra_secreta:
      letras_secreta.append(opcao)
   else:
      erro += 1

   palavra_correta = ''   
   for letra in palavra_secreta:
      if letra in letras_secreta:
         palavra_correta += letra
      else:
         palavra_correta += '*'

   print(palavra_correta)

   if erro == 1:
      minha_matriz[3][4] = 'O'
      
   if erro == 2:
      minha_matriz[4][3]= '/'
      
   if erro == 3:
      minha_matriz[4][4]= '|'

   if erro == 4:
      minha_matriz[4][5]= '\\'
      
   if erro == 5:
      minha_matriz[5][3]= '/'
   
   if erro == 6:
      minha_matriz[5][5]= '\\'
      desenhar_matriz(minha_matriz)
      print('Que pena! Você perdeu, a palavra correta é:', palavra_secreta)
      break
   if palavra_correta in palavra_secreta:
      desenhar_matriz(minha_matriz)
      print('PARABÉNS! você acertou a palavra secreta')
      break