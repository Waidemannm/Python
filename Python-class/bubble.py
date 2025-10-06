#algoritmo Bubble sort
#Complexidade: O(n²)

def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1):# se nao fizer menos um ela ira comparar com elemento que nao existe, pois as posicoes sao contadadas apartir de 0...
        troca = False
        for j in range(0, tam - i - 1):
            if lista[j] > lista[j + 1]:
                troca = True
                #atribuicao paralela
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #invertendo os valores das variaveis, so é possivel fazer isso em python, em Java teremos que usar uma variavel auxiliar para fazer essa troca
        if not troca: #se nao for necessario realizar a troca de posicao dos elementos, o programa irá sair do loop
            return 

#Programa Principal
lista = [39, 10, 18, 85, 9, 2, 1, 85]
print(f'Lista Original: {lista}')
bubble_sort(lista)
print(f'Lista Ordenada: {lista}')

