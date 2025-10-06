def qtd_salarios():
    print('*-- Quantidade de salários --*')
    qtd = int(input('Quantidade: '))
    return qtd

def criar_lista(qtd):
    print(f'*-- Criando um lista com {qtd} de salários --*')
    salarios = []
    i = 0 
    while(i < qtd):
        salario = float(input('Digite o salário: '))
        salarios.append(salario)
        i+=1
    return salarios

def media_salarial(salarios):
    print('*-- Calcular a Média --*')
    soma = 0
    for (salario in salarios):
        soma += salario
        media = soma / len(salarios)
    return media

def salario_abaixo_media(media, salarios):
    print('*-- Imprimindo os sálarios abaixo da média --*')
    for (salario in salarios):
        if(salario < media):
            print(f'Abaixo da média: {salario:.2f}')

def maior_salario(media, salarios):
    print('*-- Imprimindo o maior sálario --*')
    maior = 0
    for (salario in salarios):
        if(salario > maior):
            maior = salario
    return maior

#principal
qtd = qtd_salarios()
salarios = criar_lista(qtd)
media = media_salarial(salarios)
abaixo = salario_abaixo_media(media, salarios)
maior = maior_salario(media, salarios)
print(f'O Maior: {maior:.2f}')            
