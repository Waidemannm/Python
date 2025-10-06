try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    result = n1/n2


    lista = [1, 2, 3] 
    for n in lista:
        print(f'Elemento: {n}')

    num = int(input('Insira um número: '))
    lista.append(num)
    #indexError, indice que não existe na lista
    print(f'{lista[4]}')
except ValueError:
    print('Caractér inválido')
except IndexError:
    print('Índice não existente nalista')
except ZeroDivisionError:
    print('Erro divisão por zero') 
except Exception:
    print('Algum erro ocorreu')
finally:
    print('Fim de programa')