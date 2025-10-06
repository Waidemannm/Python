'''
Sistema de notas de alunos

Contexto: Criar um programa em python para aramazenar  o nome de cada aluno e suas respectivas notas (Dicionário). O program deve ter funções que permitem (adicionar, remover, atualizar)(Operações de um Banco de Dados(CRUD)) e calcular a média das notas  

Requisitos:
 -Dicionário para armazenar os dados do aluno (Nome = chave), (Nota = Valor);
'''

#Dicionario simulando banco de dados
dados_alunos = {
    'João' : [7.5,8.0,9.0,5.5],
    'Maria' : [9.0,5.0,6.5,10.0],
    'Pedro' : [3.0,6.5,2.5,8.0]
}

#Funcoes
def adicionar_aluno(nome, notas):
    print('Adicionando um novo aluno no dicionário')
    if nome not in dados_alunos:
        dados_alunos[nome] = notas
        print(f'Aluno {nome} foi adiconado com sucesso! \nNotas: {notas}')
    else:
        print(f'Aluno {nome} já existe')

def remover_aluno(nome):
    print('Removendo um aluno do dicionário')
    if nome in dados_alunos:
        del dados_alunos[nome]
        print(f'Aluno {nome} removido com sucesso!')
    else:
        print(f'Erro ao deletar aluno! Aluno {nome} não está no dicionário')

#Essa funcao tem como objetivo adicionar um valor a uma chave (uma nota a um aluno)
def adicionar_nota(nome, nova_nota):
    print('Adicionando nota')
    if nome in dados_alunos:
        print(f'Nota {nova_nota} adicionada ao aluno {nome}')
        dados_alunos[nome].append(nova_nota)
    else:
        print(f'Erro ao adicionar nota! Aluno {nome} não está no dicionário')

def calcular_media(nome):
    print('Calculando média de notas')
    if nome in dados_alunos:
        notas = dados_alunos[nome] #pega a lista de notas
        soma = 0
        for nota in notas: #Percorrendo lista de notas com (for)
            soma += nota
        media = soma/len(notas)
        
        return f'Média do aluno {nome}: {media}'
    else:
       return f'Erro ao calcular média de notas do aluno! Aluno {nome} não está no dicionário'


def listas_alunos():
    print('Exibindo os dados dos alunos')
    print('\nLista de Alunos e Notas')
    for nome, notas in dados_alunos.items():
        print('---------------------------------')
        print(f'Aluno: {nome} - Notas: {notas}')


#funcao principal
def main():
    escolha = int(input('Digite a opereração desejada \n(1)Adicionar Aluno \n(2)Remover Aluno \n(3)Adicionar Nota a um Aluno \n(4)Calcular Média de Aluno \n(5)Mostra Lista de Alunos \nEscolha:'))
    match escolha:
        case 1:
            nome = input('Digite o nome do novo aluno: ')
            #map converte cada string separada pelo espaço para o tipo de dado passado como primeiro parametro, e como segundo parametro ele recebe os dados que irá converter, através do inpu
            notas = list(map(float, input(f'Digite as notas do aluno {nome}: ').split()))
            adicionar_aluno(nome, notas)
        case 2:
            nome = input('Digite o nome do aluno: ')
            remover_aluno(nome)
        case 3:
            nome = input('Digite o nome do aluno: ')
            nova_nota = float(input(f'Digite a nova nota do aluno {nome}'))
            adicionar_nota(nome, nova_nota)
        case 4:
            nome = input('Digite o nome do aluno: ')
            print(f'{calcular_media(nome):.2f}')
        case 5: 
            listas_alunos()
        case _:
            print('Opção inválida!')       

    