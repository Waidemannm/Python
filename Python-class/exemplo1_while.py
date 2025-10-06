i = int(input('Me fale inicio: '))
f = int(input('Me fale o final: '))

if (i < f):
    while (i < f):
          if i % 2 == 0:
            print(f'i: {i}')
          i += 1
elif (i > f):
    while (i > f):
         if i % 2 != 0:
            print(f'i: {i}')
         i -= 1
else:
    print('inicio é igual ao fim')