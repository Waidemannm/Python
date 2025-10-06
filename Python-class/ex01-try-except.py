'''
Tratamento de exceções em Python
try-except
Sintaxe:
try:
    #Código que pode gerar uma exceção
except tipo_de_exceção
    #Código para lidar com a exceção
else: (Opcional, quse nunca usado)

finally: (Opcional, mais usado que o else) 

'''
#Exemplo sem tratamento de erro (quebra o programa)
num = int(input('Digite um número: '))
print(f' Você digitou o número {num}')

#Exemplo com tratamento de erro
while teste !=0: 
    try:
        num = int(input("Digite um número: "))
        print(f' Você digitou o número {num}')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número')
    teste = input('Digite 0 para encerrar')