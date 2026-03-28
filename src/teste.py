import storage
import random
import functions

dados = storage.ler_arquivo() #puxando o arquivo em json
palavra_secreta = functions.palavra_chave('facil')

# nivel = ''
# for chave in dados.values():
#     for item in chave.values():
#         item = item.upper()
#         print(item)

print(palavra_secreta)

# for palavra in dados[palavra_secreta]:
#     if palavra.upper() == palavra_secreta:
#         dica_encontrada = dados[palavra_secreta][palavra]
#         break


