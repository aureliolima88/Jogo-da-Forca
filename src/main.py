#toda estrutura do jogo
from pathlib import Path
import storage
import functions
import assets
import os

CAMINHO_PASTA = Path(__file__).parent.parent / 'data'
# CAMINHO_ARQUIVO = CAMINHO_PASTA / 'palavra_chave.json'

pasta = storage.criar_pasta(CAMINHO_PASTA)
arquivo = storage.criar_arquivo()
letras_secreta = []
erro = 0
acertou = assets.campeao()
game_over = assets.derrota()
texto = assets.forca()
minha_matriz = functions.criar_matriz(texto)
dados = storage.ler_arquivo()


if not CAMINHO_PASTA:
   pasta
   arquivo

while True:
   functions.menu()
   escolha_nivel = input('Digite um Nivel: ').lower()
   if escolha_nivel.isnumeric() or escolha_nivel not in dados:
      os.system('cls')
      print('Opção Invalida! Tente novamente')
      continue
   else:
      os.system('cls')
      break
palavra_secreta = functions.palavra_chave(escolha_nivel)
dica = functions.dica(escolha_nivel, palavra_secreta)
print(f'A dica para a palavra secreta é {dica}')

while True:
   print(assets.jogo_da_forca())
   print(f'TOTAL DE ERROS: {erro}')
   functions.desenhar_matriz(minha_matriz)

   opcao = input('digite uma letra: ').strip().upper()
   os.system('cls')
   
   if len(opcao)>1 or isinstance(int, float):
      print('Opção Invalida! Tente novamente.')
      continue

   if opcao in letras_secreta and opcao in palavra_secreta:
      print('Letra já encontrada, Tente Novamente!')
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
      print(game_over)
      print('Que pena! Você perdeu, a palavra correta é:', palavra_secreta)
      break
   if palavra_correta in palavra_secreta:
      print(acertou)
      print('PARABÉNS! você acertou a palavra secreta')
      break
   