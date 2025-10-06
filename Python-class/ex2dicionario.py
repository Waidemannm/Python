'''
Principais métodos (mais comuns)
- keys(): retorna uma "visão" de todas as chaves do dicionário
- values(): retorna uma "visão" de todos os valores do dicionário
- items(): retorna uma "visão" dos pares de chave-valor do dicionário
- get(): acessa um valor de forma segura (retornando um valor padrão quando não encontrar o elemento)
'''

carro = {
    "marca" : "Jeep",
    "modelo" : "Compass", 
    "ano" : 2025
}

#iterando sobre as chaves do dicionário - método keys()
#manipulação de dados na maioria das vezes usa métodos, usando sempre .
for chave in carro.keys():
    print(chave)

#iterando sobre os valores do dicionário - método values()
for valor in carro.values():
    print(valor)

#iterando sobre a chave e valor do dicionário - método items()
for chave, valor in carro.items():
    print(f'{chave}:{valor}')

#acesso a uma chave inexistente
#print(carro['motor'])

#acesso a uma chave com o método get()
#motor = carro.get('motor', 'não especificado!')
#print(f'motor: {motor}')

#Acesso a um elemento do dicionário com método .get() - evitar erros
cor = carro.get('Cor, não especificado!')
print(f'Cor: {cor}')
print(f'Marca: {carro.get("marca")}')