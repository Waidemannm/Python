n = 1
while(n <= 50):
    print(n)
    n += 1

num = int(input('Digite um numero: '))
contador = 1
somador = 0
while(contador < num):
    somador += contador
    contador += 1
print(somador)


for i in range(10, 1000 + 10, 10):
    print(i)
