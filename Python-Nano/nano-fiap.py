#tipo de coleções

#aceita varios tipo em uma tupla so, é mutavel, aceita valores repetidos

calorias = []
refs = int(input('Quantas refeições você fez? '))
for i in range(refs):
    calorias_ref = float(input(f'Quantas calorias na refeição {i+1}: '))
    calorias.append(calorias_ref)

total = 0

for i in calorias:
    total += i 

media = total/len(calorias)

# print(f'Você disse que consumiu essa caloria: {calorias[0:]}')
for i in calorias: 
    print(f'Você disse que consumiu essa caloria: {i}')

print(f'Total de calorias {total}')
print(f'Média de calorias {media}')


#tupla é imutavel depois de criada, aceita varios tipo em uma tupla so, aceita valores repetidos
#a tupla pode ser "desmontada" quando ele fornece valores a quantidade de varias corespondentes a quantidade de elementos dentro dela, é possivel fazer isso com list tambem, porem elas sao mutaveis isso pode causar erro

tupla = ("André", 88, 1.65)
print(f"A tupla é {tupla}")
nome, peso, altura = tupla

print(f"Após desempacotar a tupla, a variável nome contém {nome},  a variável peso contém {peso}, a variável altura contém {altura}")

#é possivel ter list de tupla
inimigos = [(10, 15), (30, 30), (15, 25), (7, 10)]
for x, y in inimigos:
    print(f"O inimigo está na posição X={x} e Y={y}")
x = int(input("Digite a posição X do inimigo que deseja acertar "))
y = int(input("Digite a posição Y do inimigo que deseja acertar "))
if (x, y) in inimigos:
    print("ACERTOU!!")
    inimigos.remove((x, y))
else:
    print("Não foi encontrado nenhum inimigo na posição indicada ")
print(f"Os inimigos ainda existentes são: {inimigos}")

#set aceita varios tipos em um so set, e mutavel, porem nao aceita valores repetidos, se houver valor repetido ele pega sempre o ultimo
# e possivel criar set apartir de uma list ou tupla
# set() cria um set vazio
#set([]) set de list
#set(()) set de tupla
#{1,2,3} isso tambem é um set, podem ser criado atravaes de {}, ou set()
#set(1,2,3) isso nao pode, pois esta esperado apenas um parametro


conjunto = set() #cria um set vazio
conjunto.add("Cebolinha")
conjunto.add("Cascão")
conjunto.add("Mônica")
conjunto.add("Cebolinha")
print(f"O conteúdo do set que foi recebendo elementos com o método add() é \n{conjunto}") #Note que não existe repetição de elementos
lista = ["Cebolinha", "Cascão", "Mônica", "Magali", "Cebolinha"]
novo_conjunto = set(lista)
print(f"\nPodemos criar um set a partir de uma lista de um outro set ou de qualquer estrutura iterável. A lista é \n{lista}")
print(f"O conteúdo do set construído a partir da lista é \n{novo_conjunto}") #Note que não existe repetição de elementos

op = 0
ficha = {} #criação do dicionário vazio
while op != 4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informação da ficha")
    print("3 - Exibir a ficha completa ")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))
    if op == 1:
        chave = input("\nEm qual campo deseja inserir dados? ")
        valor = input(f"Qual é o dado que deseja incluir no campo {chave}? ")
        ficha.update({chave:valor})
        #ficha[chave] = valor #esta notação também é muito utilizada e gera o mesmo efeito da linha acima
    elif op == 2:
        print(f"\nOs campos disponíveis na ficha são: {ficha.keys()}")
        chave = input("Você deseja obter dados de qual campo? ")
        if chave in ficha.keys():
            print(f"{chave} -> {ficha.get(chave)}")
            #print(f"{chave} -> {ficha[chave]}") #como o if já garante que a chave existe, poderíamos utilizar esta notação sem correr riscos
        else:
            print("O campo informado não existe na ficha cadastral.")
    elif op == 3:
        print("\n---FICHA---")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} -> {dado}")
        print("---------------------------")
    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break
    else:
        print("Por favor, escolha uma opção válida")

#defaultdict nao gera exceção ao procurar por uma chave que nao existe no dicionario, ele cria essa chave com um valor padrao
#map funcao que permite aplicar funcoes a cada elemento de uma colecao, recebe dois parametros (funcao, colecao)
#importação do defaultdict

from collections import defaultdict
#criação de um default dict com uma lista como valor padrão

dicionario_lista = defaultdict(list)
dicionario_lista["PRODUTO"] = "Macbook Pro"
dicionario_lista["MARCA"] = "Apple"

print(f"Exibindo a chave PRODUTO do dicionario criado com uma lista: {dicionario_lista['PRODUTO']}")

print(f"Exibindo a chave PREÇO, que não existe no dicionario criado com uma lista: {dicionario_lista['PREÇO']}")

#Criação de função que retorna a frase "INEXISTENTE"
def funcao_exemplo():
    return "INEXISTENTE"

dicionario_funcao = defaultdict(funcao_exemplo)
dicionario_funcao["PRODUTO"] = "Macbook Pro"
dicionario_funcao["MARCA"] = "Apple"

print(f"\nExibindo a chave PRODUTO do dicionario criado com uma função: {dicionario_funcao['PRODUTO']}")

print(f"Exibindo a chave PREÇO, que não existe no dicionario criado com uma função: {dicionario_funcao['PREÇO']}")

#Criação de dicionário com uma função lambda
dicionario_lambda = defaultdict(lambda: "Não disponível")
dicionario_lambda["PRODUTO"] = "Macbook Pro"
dicionario_lambda["MARCA"] = "Apple"

print(f"\nExibindo a chave PRODUTO do dicionario criado com uma função lamda: {dicionario_lambda['PRODUTO']}")

print(f"Exibindo a chave PREÇO, que não existe no dicionario criado com uma função lambda: {dicionario_lambda['PREÇO']}")

#OrderedDict ordena o dicionario sempre da mesma forma que ele foi inserido items, mesmo que alteramos valaores de chaves, a ordem sempre sera a mesma
#importação do OrderedDict
from collections import OrderedDict

dicionario_ordenado = OrderedDict()

print(f"O dicionario foi criado e ainda não contém nenhum valor: \n{OrderedDict}. Adicionaremos os seguintes valores e chaves: Nome:Iphone, Marca:Apple, Modelo:14 Pro Max")

#Adicionando chaves e valores
dicionario_ordenado["NOME"] = "Iphone"
dicionario_ordenado["MARCA"] = "Apple"
dicionario_ordenado["MODELO"] = "14 Pro Max"

print("\nPercorrendo o dicionario verificamos as seguintes chaves e valores: ")

for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")

dicionario_ordenado["MARCA"] = "Maçã"
print("\nAo alterar o valor da chave MARCA, percebemos que a ordem se mantém ")

for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")

dicionario_ordenado.pop("MARCA")
print("\nAo removermos a chave MARCA e percorrermos o dicionario, obtemos: ")

for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")

dicionario_ordenado["MARCA"] = "Apple"

print("\nAo reinserir a chave MARCA, notamos que passou a ser colocada na última posição ")

for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")

#namedtuple em tupla nos podemo acessar os valores pelo indice deles, o namdtuple permite dar valores para esses indices
from collections import namedtuple
Produto = namedtuple("Produto", ["nome", "marca", "preco"]) #Criação do novo tipo
novo_produto = Produto("Ipad", "Apple", 2499.99)
print(f"Criamos o objeto chamado novo_produto, usando como tipo Produto. Ao exibirmos este objeto temos: \n{novo_produto}")

#deque estrutura baseada em list, melhora o desempenho em relacao a list, em opercaoes de append e pop

from collections import deque
nova_deque = deque([elemento1, elemento2, elemento3])