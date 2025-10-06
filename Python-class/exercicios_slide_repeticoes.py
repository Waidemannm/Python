#exercicios while
num = 100
while (num <= 200):
    print(num)
    num += 1

num = int(input('Me informe um número: '))
qnt_par = 0 #quantidade de numeros pares que ira mostrar
par = 0 #numeros mostrads a partir de zero
while (qnt_par < num): #a quantidade de numeros pares sera mostrada enquanto ela for menor q o numero digitado
    print(par)
    qnt_par += 1 #soma mais um a quantidade de pares, para que sai do loop quando nao for menor que o numero digitado
    par += 2 #soma dois aao numero zero

num = int(input('Digite um numero: '))
qnt_repeticao = 0
fator = 1
while (qnt_repeticao < 10):
    resultado = num * fator
    print(f'{num} X {fator} = {resultado}')
    fator += 1
    qnt_repeticao += 1

num1 = int(input('Me informe um número: '))
num2 = int(input('Me informe outro número: '))
quociente = 0
while (num1 >= num2):
    num1 -= num2
    quociente += 1
print(quociente)

#exercicio variavel contadora
letra = input('Acerte a letra: ')
chances = 1
while (letra != 'X' and letra != 'x'):
    letra = input('Acerte a letra: ')
    chances += 1
print(f'Voce acertou a letra X, com {chances} chances!')

#variiavel acumuladora
preco = float(input('Me informe o  valor do outro produto: '))
total = 0
while(preco != -1):
    total += preco
    preco = float(input('Me informe o  valor do outro produto: '))
print(f'O valor total da compra é: {total:.2f}')

credits = int(input('Me infrome quantos créditos voce tem: '))
preco = float(input('Me informe o  valor do produto: '))
total = 0
while(credits > total):
    total += preco
    if(credits > total):
        preco = float(input('Me informe o  valor do outro produto: '))
print(f'O total a ser pago é : {total}, e os créditos são: {credits}')