nomes = []
nomes_vogais = []
qtd = 0
for i in range(5):
    nome = input('Nome de uma pessoa: ')
    nomes.append(nome)

for nome in nomes:
    if(nome[0] == 'A' or nome[0] == "E" or nome[0] == "I" or nome[0] == "O" or nome[0] == "U"):
        qtd += 1
        nomes_vogais.append(nome) 

print(f'A quantidade de nomes que se inciam com vogal: {qtd}')
print(f'A lista de nomes que iniciam com vogal {nomes_vogais}')
print( '-------------------------------------------')
for nome in nomes_vogais:
    print('Nomes iniciados com vogal')
    print(f'{nomes_vogais}')

