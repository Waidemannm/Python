#list exemplo
#indice    0    1   2    3     4
lista0 = [3.1, 7.8, 1.0, 10.0, 9.5]
#        -5  -4    -3   -2   -1  indce negativo
print(lista0)
print(lista0[0])
print(len(lista0))
lista0[1] = 6.9
print(lista0)

i = 0 #indice 0 da lista, variavel de controle do while
while(i <= 4):
    print(lista0[i]) #i se torna indice da lista aq, pois ele é colocado no lugar do parametro
    i += 1


#str imutavel e homo
#construtor str() pode criar com o construtor "nome_sequencia = str('')" ou sem "nome_sequencia = ['']"

ling  = 'Linguagem Python' #sequencia str de caracteres, cada digito é um indice
print(len(ling))
print(ling[0])
print(ling[15])
# print(ling(16)) dá erro (IndexError), pois é um indice que nao existe na sequencia str ling, os indices vão até 15, pois contamos a partir de 0
#ling[0] = 'X' dá erro (TypeError) pois sequencia do tipo string é imutavel e homogenea (nao pode receber valor de outro tipo de dado, sem ser char)

#list mutavel e imutavel/ homo e hetero
#construto list() pode criar com o construtor "nome_sequencia = list(1, 1, 1,)" ou sem "nome_sequencia = [1, 1, 1,]"

lista = [3, True, 3.14, 'Python'] #lista hetero e mutavel
print(len(lista))
print(lista[3])
lista[2] = 3.16
print(lista[2])


#tuple Imutavel e hetero
#construtor tuple() pode criar com o construtor "nome_sequencia = tuple()" ou sem "nome_sequencia = ()" tuple sem construtor é criada com parenteses, diferentes de str e list, que usam chaver, mas os indices serão acessados por chaves na tuple, igual os outros 

nome_sequencia = (12, 34, 13) #imutavel
print(len(nome_sequencia))
nome_sequencia2 = (12, True, 5.0, 'Python') #imutavel
print(nome_sequencia2[2])
#nome_sequencia[2] = 4.2 da erro (TypeError), pois é imutavel

#range imutavel e homo
#intervalo, faixa de valores, usado no for
#construto range(), pode nao receber parametro ou 1 ou 2 ou 3 parametros. Com 3 parametro = parametro 1 onde começa(inicio), parametro 2 onde termina(fim),parametro 3 de enquanto enquanto pula a lista (passo). Com 2 parametros passo de 1 em 1, e parametro 1 será inicio e parametro 2 sera fim. Com 1 parametro, parametro 1 determinara apenas o fim a partir de 0 e passo de 1 em 1. 

intervalo = range(10, 100 + 1, 10) #some +1 ao parametro 2 pois o range vai até um numero anterior do parametro passado
print(range) #so mostra a class range, pois range nos temos que converter parra pode usar
lista2 = list(intervalo) #temos que converter o range para algum tipo de sequencia(poderia ser str, list ou tuple), temos que fazer isso para conseguir usar as funçoes de lista, como vimos acima algumas.
print(lista2)
# lista2[1] = 50 da erro (TyperError) pois o range é imutavel.
