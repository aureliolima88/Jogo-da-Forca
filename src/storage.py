#gerar e salvar o arquivo em json
#Tudo relacionado a arquivo
from pathlib import Path
import json

CAMINHO_PASTA = Path(__file__).parent.parent / 'data'
CAMINHO_ARQUIVO = CAMINHO_PASTA / 'palavra_chave.json'

palavra_chave = {
    'facil': {
        'Mesa': 'Tem quatro pernas',
        'Livro': 'Tem muitas páginas',
        'Azul': 'Cor do céu',
        'Bola': 'Usada no futebol',
        'Pato': 'Anda na água'
    },
    'medio': {
        'Farmacia': 'Vende remedio',
        'Trabalho': 'Atividade profissional',
        'Retangulo': 'Forma geometrica',
        'Aquario': 'Local com muitos peixes',
        'Amolador': 'Que afia facas'
    },
    'dificil': {
        'jazigo': 'Tumulo',
        'Psique': 'refere-se à mente humana',
        'Xilofone': 'É um instrumento musical',
        'Bacalhau': 'É um dos pilares da gastronomia portuguesa'
    }
}

# Se a pasta 'data' não existir, ele cria ela automaticamente
def criar_pasta(arquivo):
    if not arquivo.exists():
        arquivo.mkdir()

#cria o arquivo em json
def criar_arquivo():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(palavra_chave, arquivo, ensure_ascii=False, indent=2)

#faz a leitura do arquivo em json
def ler_arquivo():
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

if __name__ == '__main__':
    criar_pasta()
    criar_arquivo()
    ler_arquivo()