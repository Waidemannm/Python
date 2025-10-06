'''
Manipulação de lista com funções
Documentação  docstrings
'''
def tamanho_lista():
    """
    DESCRIÇÂO
    Obter e retornar o tamanho da lista (número inteiro)
    PARAMETRO

    Essa função não tem passagem de parametros
    RETORNO

    Papel de retornar o valor do tamanho da lista
    """
    print('*-- TAMANHO DA LISTA --*')
    print('------------------------')
    tamanho = int(input('Digite o tamanho da lista: '))
    return tamanho

def criar_lista(tamanho):
    """
    DESCRIÇÂO
    Criar a lista com laço de repetição while
    PARAMETRO

    Essa função recebe o tamanho da lista obtido na função tamanho_lista
    RETORNO

    Retorna a lista pronta
    """
       
    print(f'*-- CRIAR UMA LISTA COM {tamanho} ELEMENTOS --*')
    print('------------------------------------------------')
    lista = []
    i = 0
    while i < tamanho:
        n = int(input('Digite um número: '))
        lista.append(n)
        i += 1
    return lista

def imprimir_lista(lista):
    """
    DESCRIÇÂO
    Imprimir cada elemento da lista
    PARAMETRO

    Essa função recebe a lista já criada na função criar_lista
    RETORNO

    Retorna a lista pronta
    """
    print(f'*-- IMPRIMIR OS ELEMENTOS DA LISTA --*')
    print('---------------------------------------')
    for n in lista:
        print(f'Número: {n}')

def somar_items(lista):
    """
    DESCRIÇÂO
    Soma cada elemento da lista
    PARAMETRO

    Essa função recebe a lista já criada na função criar_lista
    RETORNO

    Retorna a soma dos elementos
    """
    print(f'*-- SOMANDO ELEMENTOS --*')
    print('--------------------------')
    soma = 0
    for n in lista:
        soma += n
    return soma

def imprimir_par(lista):
    """
    DESCRIÇÂO
    Imprimi os números pares da lista
    PARAMETRO
    
    Essa função recebe a lista já criada na função criar_lista
    RETORNO

    Retorna apenas os valores pares da lista
    """
    print(f'*-- IMPRIMINDO PAR --*')
    print('---------------------------')
    for n in lista:
        if(n% 2 == 0):
            print(f'Número {n} é par!')


def imprimir_impar(lista):
    """
    DESCRIÇÂO
    Imprimi os números ímpares da lista
    PARAMETRO
    
    Essa função recebe a lista já criada na função criar_lista
    RETORNO

    Retorna apenas os valores ímparess da lista
    """
    print(f'*-- IMPRIMINDO ÍMPARES --*')
    print('---------------------------')
    for n in lista:
        if(n% 2 != 0):
            print(f'Número {n} é ímpar!')

def principal():
    """
    DESCRIÇÂO
    Executa tudo o que estaria no principal, é feito para limpar a memória alocada 
    PARAMETRO
    
    Essa função não recebe parametro
    RETORNO

    Retorna a execução de todo o programa
    """
    print('------------------------')
    print(f'*-- PROGRAMA PRINCIPAL --*')
    print('------------------------')
    tamanho = tamanho_lista()
    lista = criar_lista(tamanho)
    imprimir_lista(lista)
    print(f'A soma de todos os números é: {somar_items(lista)}')
    imprimir_par(lista)
    imprimir_impar(lista)


#Principal
principal()