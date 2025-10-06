
def menu():
    print('*--Menu--*')
    print('Operações: \n1.Adção \n2.Subtração \n3.Dvisão \n4.Multplicação')
    escolha =int(input('DIgite a operaçãp desejada: '))
    return escolha

def numeros():
    print('*--Numeros--*')
    num = int(input('Digite um numero: '))
    return num

def adicao(n1, n2):
    print('*--Adição--*')
    result = n1 + n2
    return result

def subtraca(n1, n2):
    print('*--Subtração--*')
    result = n1 - n2
    return result

def divisao(n1, n2):
    print('*--Divisão--*')
    result = n1/n2
    return result

def multiplicacao(n1, n2):
    print('*--Multiplicação--*')
    result = n1 * n2
    return result

def imprimir(resultado):
    print('*--Imprimindo Resultado--*')
    print(f'O resultado é {resultado}')

def controlador(escolha, n1, n2):
    print('*--Controlador--*')
    if escolha == 1:
        result = adicao(n1, n2)
    elif escolha == 2:
        result = subtraca(n1, n2)
    elif escolha == 3:
        result = divisao(n1, n2)
    elif escolha == 4:
        result = multiplicacao(n1, n2)
    return result

def main():
    print('**PRINCIPAL**')
    escolha = menu()
    n1 = numeros()
    n2 = numeros()
    ressultado = controlador(escolha, n1, n2) 
    imprimir(ressultado)

main()