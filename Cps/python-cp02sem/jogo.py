'''
Caça ao Tesouro
Regras:
    - O tabuleiro é uma matriz 10x10 (com posições de 0 a 9);
    - Tesouros (T) e Armadilhas (A) são escondidos aleatoriamente nas posições (0 a 9, 0 a 9);
    - Os jogadores começam juntos na posição inicial (0, 0);
    - Cada jogador tem 10 pontos no início;
    - Em cada rodada, o jogador sorteado rola dois dados:
        - O primeiro define a linha (0 a 9);
        - O segundo define a coluna (0 a 9);
        - A posição sorteada define para onde o jogador se move;
    - Regras de pontuação:
        - Ao cair em um Tesouro (T): ganha +10 pontos;
        - Ao cair em uma Armadilha (A): perde -5 pontos;
    - São 20 rodadas no total (10 jogadas para cada jogador);
    - Ao final das rodadas, vence quem tiver a maior pontuação.

Funções do código:
    - criar_tabuleiro(): cria a matriz 10x10 preenchida com ".".
    - mostrar_tabuleiro(tabuleiro, posicao_atual, siglas_jogadores): imprime o tabuleiro com jogadores e elementos visuais.
    - definir_jogadores(): solicita os nomes dos dois jogadores, garantindo nomes únicos.
    - gerar_sigla(nome, siglas_usadas): gera uma sigla única para cada jogador com base no nome.
    - posicao_inicial(jogadores): inicializa todos os jogadores na posição (0, 0).
    - esconder_T(tabuleiro): solicita a quantidade de tesouros (5 a 20), sorteia posições e marca "T" no tabuleiro.
    - esconder_A(usadas, tabuleiro): solicita a quantidade de armadilhas (5 a 20), sorteia posições e marca "A" no tabuleiro.
    - verificar_posicao(usadas): sorteia uma posição que ainda não foi usada para T ou A.
    - exibir_regras(): imprime as regras do jogo no terminal.
    - start(): inicia o contador de rodadas com 0.
    - verificar_rodada(rodada): retorna True se ainda restam rodadas (menor que 20), False caso contrário.
    - dado(liberacao, rodada, jogadores): sorteia nova posição e alterna o jogador da vez.
    - atualizar_posicao(posicao_atual, nova_posicao, jogador, tabuleiro): atualiza a posição do jogador no dicionário.
    - contador(jogadores, liberacao): imprime a pontuação final e declara o vencedor.
    - main(): função principal que orquestra o jogo.
'''

import random

def criar_tabuleiro():
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append('.')
        tabuleiro.append(linha)
    return tabuleiro

def mostrar_tabuleiro(tabuleiro, posicao_atual, siglas_jogadores):
    # Cabeçalho das colunas
    print("   ", end="")
    for j in range(10):
        print(j, end="  ")
    print()

    # Linhas do tabuleiro
    for i in range(10):
        print(i, end="  ")  # índice da linha
        for j in range(10):
            ocupado = False
            for jogador, pos in posicao_atual.items():
                if pos == (i, j):
                    print(siglas_jogadores[jogador], end="  ")
                    ocupado = True
                    break
            if not ocupado:
                print(tabuleiro[i][j], end="  ")
        print()  # quebra de linha


def definir_jogadores():
    jogadores = {}

    for i in range(2):  
        # dois jogadores
        nome = ''
        while(nome.strip() == '' or nome in jogadores):        
            nome = input(f"Digite o nome do jogador {i+1}: ").strip()
            if(nome.strip() == ''):
                print('O nome não pode ser vazio')
            elif(nome in jogadores):
                     print('Esse nome já foi usado. Escolha outro.')
        jogadores[nome] = 0  # inicializa com 0 pontos    
    return jogadores
    
def posicao_inicial(jogadores):
    posicao_atual = {}
    for nome in jogadores.keys():
        posicao_atual[nome] = (0, 0)
    return posicao_atual

def esconder_T(tabuleiro):
    usadas = []
    qtd_T = 0
    while(qtd_T < 5 or qtd_T > 10):
        try:
            qtd_T = int(input('Digite a quantidade de tesouros que serão escondidos no tabuleiro (5 a 10): '))
            if qtd_T < 5 or qtd_T > 10:
                print('A quantidade de tesouros deve ser entre 5 e 10!')
        except ValueError:
            print('Você deve digitar um número válido!')


    for i in range(qtd_T):
        linha, coluna = verificar_posicao(usadas)
        tabuleiro[linha][coluna] = "T"
        usadas.append((linha, coluna))
    return usadas, tabuleiro

def esconder_A(usadas, tabuleiro):      
    qtd_A = 0
    while(qtd_A < 5 or qtd_A > 10):
        try:
            qtd_A = int(input('Digite a quantidade de armadilhas que serão escondidas no tabuleiro (5 a 10): '))

            if qtd_A < 5 or qtd_A > 10:
                print('A quantidade de armadilhas deve ser entre 5 e 10!')
        except ValueError:
            print('Você deve digitar um número válido!')

    for i in range(qtd_A):
        linha, coluna = verificar_posicao(usadas)
        tabuleiro[linha][coluna] = "A"
        usadas.append((linha, coluna))
    return tabuleiro
         
def verificar_posicao(usadas):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        if (linha, coluna) not in usadas:
            return linha, coluna
        
def exibir_regras():
    print("\n*-- REGRAS DO JOGO: CAÇA AO TESOURO --*")
    print("- Tabuleiro 10x10. Jogadores começam na posição (0,0)")
    print("- Tesouros valem +10 pontos (símbolo: T)")
    print("- Armadilhas tiram -5 pontos (símbolo: A)")
    print("- Cada jogador começa com 10 pontos")
    print("- Serão 20 rodadas (10 para cada jogador)")
    print("- Em cada rodada, rola-se dois dados: define a posição")
    print("- Quem tiver mais pontos no final, vence!\n")

def start():
    rodada = 0
    return rodada


def verificar_rodada(rodada):
    if(rodada < 20):
        return True
    else:
        return False
    
def contador(jogadores, liberacao):
    if(liberacao == False):
        print('\n*-- FIM DO JOGO --*')
        for jogador, pontos in jogadores.items():
            print(f'{jogador}: {pontos} pontos')

        maior_pontuacao = -9999  # valor inicial bem baixo
        for jogador, pontos in jogadores.items():
            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                vencedor = jogador
        print(f'\nVencedor: {vencedor} com {maior_pontuacao} pontos!')
            
def dado(liberacao, rodada, jogadores):
    if liberacao:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        nova_posicao = (linha, coluna)

        # alterna entre os jogadores
        nomes = list(jogadores.keys())
        jogador = nomes[rodada % 2]

        rodada += 1
        return nova_posicao, rodada, jogador

def atualizar_posicao(posicao_atual, nova_posicao, jogador, tabuleiro):
    # Posição antiga do jogador (volta a ser ".")
    linha_antiga, coluna_antiga = posicao_atual[jogador]
    tabuleiro[linha_antiga][coluna_antiga] = "."

    # Nova posição
    posicao_atual[jogador] = nova_posicao

    return posicao_atual, tabuleiro

def gerar_sigla(nome, siglas_usadas ):
    for letra in nome.upper():
        if letra not in siglas_usadas:
            return letra

    
def main():
    repetir = 'SIM'
    while(repetir == 'SIM'):
        exibir_regras()
        tabuleiro = criar_tabuleiro()
        jogadores = definir_jogadores()
        siglas_jogadores = {}
        siglas_usadas = []
        for nome in jogadores:
            sigla = gerar_sigla(nome, siglas_usadas)
            siglas_usadas.append(sigla)
            siglas_jogadores[nome] = sigla

        posicao_atual = posicao_inicial(jogadores)

        usadas, tabuleiro = esconder_T(tabuleiro)
        tabuleiro = esconder_A(usadas, tabuleiro)

        rodada = start()

        while verificar_rodada(rodada):
            mostrar_tabuleiro(tabuleiro, posicao_atual, siglas_jogadores)

            input(f"\nRodada {rodada+1} - Pressione ENTER para jogar os dados...")
            
            nova_posicao, rodada, jogador = dado(True, rodada, jogadores)
            posicao_atual, tabuleiro = atualizar_posicao(posicao_atual, nova_posicao, jogador, tabuleiro)

            # verifica se caiu em T ou A
            linha, coluna = nova_posicao
            if tabuleiro[linha][coluna] == "T":
                jogadores[jogador] += 10
                print(f"{jogador} encontrou um TESOURO! +10 pontos")
            elif tabuleiro[linha][coluna] == "A":
                jogadores[jogador] -= 5
                print(f"{jogador} caiu em uma ARMADILHA! -5 pontos")

        contador(jogadores, False)
        repetir = input('Jogar denovo? \n').upper()
    print('\nObrigado por jogar!\n')

#Principal
main()
