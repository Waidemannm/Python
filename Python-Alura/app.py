print('SABOR EXPRESS\n')
print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
print(f'Você escolheu a opção {opcao_escolhida}\n')

if (opcao_escolhida == 1):
    print('Cadastras restaurante')
elif (opcao_escolhida == 2):
    print('Listar restaurantes')
elif(opcao_escolhida == 3):
    print('Ativar restaurante')
else:
    print('Encerrando programa')
