'''
Pensamento Computacional
- Persitência de dados - decomposição em 3 etapas:
    1. Abrir o arquivo (leitura e escrita)
    2. Pocessar os dados - (escrever ou ler)
    3. Fechar o arquivo - salvar as informações

Em python, a função open() - lida com a etapa 1. e a função .close() lida com a etapa 3.

Modos de operação:
    - w - write - escrita (cria o arquivo se não existir, apaga o conteúdo se existir)
        obs: cuidado ao usar esse modo, pois apaga o conteúdo existente, Sobeescrita, diferente do append que só adiciona, isso se já tiver dados dentro
    - r - read - leitura (abre o arquivo para leitura, erro se o arquivo não existir)
    - a - (append - adicionar) (cria o arquivo se não existir, mantém o conteúdo se existir e acrescenta ao final)
'''
# Exemplo prático de persistência de dados em arquivo texto
# Cadastro de alunos

import os

ARQUIVO_TEXTO = "cadastro.txt"

def escrever(dados):
    """Escrever uma lista de Strings em um arquivo texto, sobrescrevebdo o conteúdo ('w')"""

    print("Escrevendo no arquivo...")

    try: 
        #with - permite que o arquivo seja fechado através da abstração
        with open(ARQUIVO_TEXTO, 'w') as arquivo:
            for item in dados:
                arquivo.write(f'{item}\n') # escreve cada item da lista em uma nova linha
        print(f'\n [SUCESSO] Dados escritos com sucesso no {ARQUIVO_TEXTO}')
    except Exception as e:
        print(f'\n [Erro] Occoreu um erro ao escrever no arquivo: {e}')

def ler():
    """Letirua de todas as linhas de um arquivos e retornando como uma Lista"""

    print('Lendo o arquivo...')

    try:
        with open(ARQUIVO_TEXTO, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in arquivo:
                linhas.append(linha.strip()) # strip() remove espaços em branco e quebras de linha
        return linhas
    except FileNotFoundError:
        print(f'\n [Erro] Arquivo {ARQUIVO_TEXTO} não encontrado.')
        return []
    except Exception as e:
        print(f'\n [Erro] Occoreu um erro ao ler o arquivo: {e}')
        return []
                
def adicionar(novo_dado):
    """Adiciona um nova string ao final do arquivo ('a')"""

    print('Adicionando um novo dado...')

    try:
        with open(ARQUIVO_TEXTO, 'a') as arquivo:
            arquivo.write(f'{novo_dado}\n')
        print(f'\n [SUCESSO] Dado adicionado com sucesso no {ARQUIVO_TEXTO}')
    except Exception as e:
        print(f'\n [Erro] Occoreu um erro ao adicionar {novo_dado} ao arquivo: {e}')

def menu():
    """Exibi o menu para o usuário escolher o processo de operação desejado"""
    print('>>> Menu de Operações <<<')
    while True:
        print('-- Persisntência de dados em arquivos --')
        print('1. Escrever uma nova lista de dados, (sobreescrevendo o arquivo)')
        print('2. Ler arquivo')
        print('3. Adicionar novo dado')
        print('4. Sair')
        escolha = input('Escolha uma opção (1-4): ')
        match escolha:
            case 1:
                dado_brutos = input('Digite os dados separados por vírgula (ex. Ana, Brenno, Leticia): ')
                dados = dado_brutos.split(',')
                dado_limpos = []
                for item in dados:
                    dado_limpos.append(item.strip())
            case 2:
                dados = ler()
                if dados:
                    print('\nConteúdo do Arquivo')
                    for item in dados:
                        print(item)
                else:
                    print('\nArquivo não existe, ou está vazio!')
            case 3:
                novo_dado = input('Digite o novo dado: ')
                adicionar(novo_dado)
            case 4:
                print('Saino do programa... até breve')
                break
            case _:
                print('\nOpção inválida')
# Programa principal
menu()