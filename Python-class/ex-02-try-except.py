'''
Exemplo múltiplicas except
'''

#Código sem tratamento de erro (quebra o programa)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
result = n1/n2
print(f'O resultado da divisão é: {result}')

#Código com tratamento de erro
while teste !=0:
    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: ')) 
        result = n1/n2
        print(f'O resultado da divisão é: {result}')
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
    except ValueError:
        print('Caractér inválido') 
    teste = input('Digite 0 para encerrar')
