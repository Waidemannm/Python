nome = input('Digite seu nome')
n1 = float(input('Digite sua nota 1: '))
n2 = float(input('Digite sua nota 2: '))
n3 = float(input('Digite sua nota 3: '))
media = (n1 + n2 + n3)/3


if (media >= 9 and <= 10):
    status = 'aprovado'
    conceito 'A'
elif (media >= 8 and < 9):
    status = 'aprovado'
    conceito = 'B'
elif (media >= 7 and < 8):
    status = 'aprovado'
    conceito = 'C'
elif (media >= 6 and < 7):
    status 'aprovado'
    conceito = 'D'
else:
    status = 'reprovado'
    conceito = 'E'

match media:
    case 9 | 10:
        print(f'Seu status é {status}, e o conceito {conceito} {nome}, com a média de {media:.1f}')
    case 8:
        print(f'Seu status é {status}, e o conceito {conceito} {nome}, com a média de {media:.1f}')
    case 7:    
        print(f'Seu status é {status}, e o conceito {conceito} {nome}, com a média de {media:.1f}')
    case 6:
        print(f'Seu status é {status}, e o conceito {conceito} {nome}, com a média de {media:.1f}')
    case _:
        print(f'Seu status é {status}, e o conceito {conceito} {nome}, com a média de {media:.1f}')