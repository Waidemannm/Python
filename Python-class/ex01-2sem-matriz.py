'''
1) Escreva uma função para criar e retornar uma matriz (lista dentro de lista) numérica, n x m (matriz quadrada, cada linha c a mesma quantidade de elementos das colunas)
2) Escreva uma função que receba uma matriz numérica por parâmetro e retorne a soma de todas os elementos contidos na matriz
3) Escreva uma função para imprimir a soma (resultado)
4) Escreva uma função main para testar o prorama
'''


def criar_matriz(n_linhas, n_colunas):
    matriz = [] #lista vazia
    for i in range(n_linhas):
        linha = [] #lista vazia
        for j in range(n_colunas):
            n =  int(input('Digite um numero: '))
            linha.append(n)
        matriz.append(linha)
    return matriz
 
def somar(matriz):
    soma = 0 #variavel acumuladora
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)[linha]):
            soma += matriz[linha][coluna]
    return soma

def imprimir(soma):
    print(f'Soma: {soma}')

def main():
    n_linhas = int(input('Digite o número de linhas'))
    n_colunas = int(input('Digite o número de colunas'))
    matriz = criar_matriz(n_linhas, n_colunas)
    soma= somar(matriz)
    imprimir(soma)

main()

