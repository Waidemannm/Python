#simulção de banco de dados
nomes_cadastrados = []
telefones_cadastrados = []
cpfs_cadastrados = []
senhas_cadastradas= []
emails_cadastrados = []
enderecos_cadastrados = []
rua_cadastradas = []
nr_cadastrados = []
bairros_cadastrados = []
siglas_cadastradas = []
ceps_cadastrados = []
meus_animais_perdidos = []
meus_animais_encontrados = []
tutores_cadastrados = []
dados_tutores = []
estados_brasil = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]
def exibir_menu():
    """
    DESCRIÇÃO
        Exibe o menu principal com as opções disponíveis para o usuário.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna opcao, a escolha desejada pelo usuário.
    """
    print('*-- PetSOS --*')
    print('------------------------------')
    print('Seja bem vindo(a) ao PetSOS')
    opcao = input('Selecione a opção desejada \n(1) Cadastrar Animal Perdido  \n(2) Cadastrar Animal Encontrado \n(3) Me Cadastrar \n(4) Ver Minhas Informações de Perfil \n(5) Ver meus animais perdidos \n(6) Ver meus animais encontrados \n(7) Sair \nOpção: ')
    return opcao

def pedir_nome():    
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o nome.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna nome
    """
    nome = input('Nome: ')
    while(len(nome) >= 80):
        print('O nome deve menor que 80 dígitos')
        nome = input('Nome: ')
    nomes_cadastrados.append(nome)
    print('Nome cadastrado com sucesso!')
    return nome

def pedir_cpf():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o cpf.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna cpf
    """
    cpf = input('CPF (somente números): ')
    while(len(cpf) != 11 or not cpf.isdigit()):
        print('CPF inválido')
        cpf = input('CPF (somente números): ')
    
    while(cpf in cpfs_cadastrados):
        print('Este CPF já está cadastrado.')
        cpf = input('CPF (somente números): ')
        while (len(cpf) != 11 or not cpf.isdigit()):
            print('CPF inválido!')
            cpf = input('CPF (somente números): ')
    cpfs_cadastrados.append(cpf)
    print('CPF cadastrado com sucesso!')
    return cpf

def pedir_telefone():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o telefone.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna telefone
    """    
    telefone = input('Telefone com DDD: ')
    while(len(telefone) != 11 or not telefone.isdigit()):
        print('Telefone inválido')
        telefone = input('Telefone com DDD: ')
    while(telefone in telefones_cadastrados):
        print('Este telefone já está cadastrado.')
        telefone = input('Telefone com DDD: ')
        while(len(telefone) != 11 or not telefone.isdigit()):
            print('Telefone inválido!')
            telefone = input('Telefone com DDD: ')   
    telefones_cadastrados.append(telefone)
    print('Telefone cadastrado com sucesso!')
    return telefone

def pedir_email():    
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o email.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna email
    """
    email = input('Email: ')
    while('@' not in email or '.' not in email):
        print('Informe um email válido!')
        email = input('Email: ')
    while email in emails_cadastrados:
        print('Este email já está cadastrado.')
        email = input('Email: ')
        while('@' not in email or '.' not in email):
            print('Informe um email válido!')
            email = input('Email: ')
    emails_cadastrados.append(email)
    return email

def pedir_rua():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo a rua.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna rua
    """
    print('Vamos cadastrar seu endereço agora')
    rua = input('Digite o nome da rua: ')
    while(len(rua) < 3 or verificar_rua(rua) ==  False):
        print('Informe uma rua existente!')
        rua = input('Digite o nome da rua: ')
    rua_cadastradas.append(rua)
    return rua

def pedir_numero():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o número.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna numero
    """
    numero = input('Digite o número do seu endereço: ')
    while(len(numero) > 7 or not numero.isdigit()):
        print('Número inválido!')
        numero = input('Digite o número do seu endereço: ')       
    nr_cadastrados.append(numero)
    return numero

def pedir_bairro():    
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o bairro.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna bairro
    """
    bairro = input('Digite o seu bairro: ')
    while(len(bairro) < 3 or verificar_bairro(bairro) == False):
        print('Informe um bairro existente!')
        bairro = input('Digite o seu bairro: ')
    bairros_cadastrados.append(bairro)
    return bairro

def pedir_sg_estados():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo a sigla do estado.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna sg_estados
    """
    sg_estados = input('Digite a sigla do estado: ')
    while(sg_estados not in estados_brasil):
        print('A sigla deve ser existente!')
        sg_estados = input('Digite a sigla do estado: ')
    siglas_cadastradas.append(sg_estados)
    return sg_estados

def pedir_cep():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo o cep.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna cep
    """
    cep = input('Digite o CEP (apenas números): ')
    while(len(cep) != 8 or not cep.isdigit()):
        print('Cep inválido!')  
        cep = input('Digite o CEP (apenas números): ')
    ceps_cadastrados.append(cep)
    return cep

def pedir_senha():
    """
    DESCRIÇÃO
        Esta função faz parte do cadastro do tutor, pedindo a senha.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna senha
    """
    senha = input('Crie uma senha: ')
    while(len(senha) < 5 or verificar_senha(senha) == False):
        print('A senha de ser maior que 5 dígitos e ter números e caractéres')
        senha = input('Crie uma senha: ')
    senhas_cadastradas.append(senha)
    print('Senha cadastrada com sucesso!')  
    return senha

def verificar_senha(senha):
    """
    DESCRIÇÃO
        Esta função verifica se a senha possui a combinação entre números e letras.
    PARÂMETROS
        Essa função recebe senha como parâmetros.
    RETORNO
        Retorna True ou False
    """
    tem_letra = False
    tem_numero = False
    for i in senha:
        if(i.isalpha()):
            tem_letra = True
        
        if(i.isdigit()):
            tem_numero = True
    if (tem_letra and tem_numero):
        return True
    else:
        return False

def verificar_bairro(bairro):
    """
    DESCRIÇÃO
        Esta função verifica se o bairro é composto de apenas letras.
    PARÂMETROS
        Essa função recebe bairro como parâmetros.
    RETORNO
        Retorna True ou False
    """ 
    apenas_letra = False
    for i in bairro:
        if(i.isalpha()):
            apenas_letra = True
    if(apenas_letra):
        return True
    else:
        return False
    
def verificar_rua(rua):
    """
    DESCRIÇÃO
        Esta função verifica se a rua é composta de apenas letras.
    PARÂMETROS
        Essa função recebe rua como parâmetros.
    RETORNO
        Retorna True ou False
    """ 
    apenas_letra = False
    for i in rua:
        if(i.isalpha()):
            apenas_letra = True
    if(apenas_letra):
        return True
    else:
        return False
    
def cadastrar_animal_perdido():
    """
    DESCRIÇÃO
        Esta função cadastra animal perdido.
    PARÂMETROS
        Essa função recebe nada como parâmetros.
    RETORNO
        Não possui retorno
    """ 
    nome_animal = input('Digite o nome do animal: ')
    data_desaparecimento = input('Data do desaparecimento (dia/mes/ano): ')
    descricao = input('Descrição sobre o pet: ')
    animal_perdido = nome_animal + " " + data_desaparecimento + " " + descricao
    if(animal_perdido not in meus_animais_perdidos):
        print(f'{nome_animal} foi cadastrado com status de perdido na data {data_desaparecimento}, com essa descrição "{descricao}"')
        meus_animais_perdidos.append(animal_perdido)
        return animal_perdido
    else:
        print('Este animal já está cadastrado como perdido!')

def cadastrar_animal_encontrado():
    """
    DESCRIÇÃO
        Esta função cadastra animal encontrado.
    PARÂMETROS
        Essa função recebe nada como parâmetros.
    RETORNO
        Não possui retorno
    """ 
    nome_animal_encontrado = input('Digite o nome do animal: ')
    data_desaparecimento_encontrado = input('Data do desaparecimento (dia/mes/ano): ')
    descricao = input('Descrição sobre o pet: ')
    animal_encontrado = nome_animal_encontrado + " " + data_desaparecimento_encontrado + " "  + descricao
    if(animal_encontrado in meus_animais_perdidos):
        print(f'{nome_animal_encontrado} desaparecido na data {data_desaparecimento_encontrado}, com a descrição "{descricao}", está com o status de encontrado agora')
        meus_animais_encontrados.append(animal_encontrado)  
    else:
        print('Este animal não foi cadastrado!')

def criando_usuario(nome, telefone, email, rua, bairro, numero, cep, sigla, cpf, senha):
    """
    DESCRIÇÃO
        Esta função cria um objeto para lista dados_tutores, salvando dados de usuário.
    PARÂMETROS
        Essa função recebe nome, telefone, email, rua, bairro, numero, cep, sigla, cpf, senha como parâmetros.
    RETORNO
        Retorn dados_tutor
    """ 
    endereco = rua + ', ' + bairro + ', ' + numero + ', ' + cep + ' - ' + sigla
    dados_tutor = 'Nome: ' + nome + '\nCPF: ' + cpf + '\nTelefone: ' + telefone + '\nEmail: ' + email + '\nEndereço: ' + endereco + '\nSenha: ' + senha
    dados_tutores.append(dados_tutor)
    return dados_tutor

def login_tutor(cpf, senha):
    """
    DESCRIÇÃO
        Esta função cria um objeto para lista tutores_cadastrados, para verificar logins.
    PARÂMETROS
        Essa função recebe cpf e senha como parâmetros.
    RETORNO
        Não possui retorno
    """ 
    tutor_login = cpf + senha    
    tutores_cadastrados.append(tutor_login)

def exibir_perfil(dados_tutor):
    """
    DESCRIÇÃO
        Esta função exixi os dados do usuário.
    PARÂMETROS
        Essa função recebe dados_tutor como parâmetros.
    RETORNO
        Não possui retorno
    """ 
    contator = 0
    limite_tentativas = 5
    print('Para ver seus dado Informe seu')
    insira_cpf = input('CPF: ')
    insira_senha =  input('Senha: ')
    usuario = insira_cpf + insira_senha
    while(usuario not in tutores_cadastrados and contator < limite_tentativas):
        contator += 1
        print('Dados inválidos')
        insira_cpf = input('CPF: ')
        insira_senha =  input('Senha: ')
    if(contator == limite_tentativas):
        print('Limite de tentativas exedido!')
    else:
        print(f'{dados_tutor}')

def resetar_dados():
    """
    DESCRIÇÃO
        Esta função limpa todos os dados cadastrados, resetando o banco de dados simulado.
    PARÂMETROS
        Nenhum.
    RETORNO
        Nenhum.
    """
    nomes_cadastrados.clear()
    telefones_cadastrados.clear()
    cpfs_cadastrados.clear()
    senhas_cadastradas.clear()
    emails_cadastrados.clear()
    enderecos_cadastrados.clear()
    rua_cadastradas.clear()
    nr_cadastrados.clear()
    bairros_cadastrados.clear()
    siglas_cadastradas.clear()
    ceps_cadastrados.clear()
    meus_animais_perdidos.clear()
    meus_animais_encontrados.clear()
    tutores_cadastrados.clear()
    dados_tutores.clear()
    print('Todos os dados foram resetados com sucesso!')


def principal():
    """
    DESCRIÇÂO
        Executa tudo o que estaria no principal, é feito para limpar a memória alocada.
    PARAMETRO
        Essa função recebe a opção escolhida pelo usuário como parametros.
    RETORNO
        Retorna a execução de todo o programa
    """
    escolha = 'sim'
    contador = 0
    dados_tutor = ''
    while escolha.lower() == 'sim':
        opcao = exibir_menu()
        match opcao:
            case '1':
                print('*-- Cadastrar animal perdido --*')
                cadastrar_animal_perdido()
            case '2':
                print('*-- Cadastrar animal encontrado --*')
                cadastrar_animal_encontrado()                
            case '3':
                if(contador == 0):
                    print('*-- Cadastro --*')
                    nome = pedir_nome()
                    cpf = pedir_cpf()
                    telefone = pedir_telefone()
                    email = pedir_email()
                    rua = pedir_rua()
                    numero = pedir_numero()
                    bairro = pedir_bairro()
                    sigla = pedir_sg_estados()
                    cep = pedir_cep()
                    senha = pedir_senha()
                    verificar_senha(senha)
                    verificar_bairro(bairro)
                    verificar_rua(rua)
                    login_tutor(cpf, senha)
                    dados_tutor = criando_usuario(nome, telefone, email, rua, bairro, numero, cep, sigla, cpf, senha)
                    print('Cadastro feito com sucesso!')
                    contador += 1
                elif(contador > 0):
                    print('*-- Mudando dados de cadastro --*')
                    nome = pedir_nome()
                    cpf = pedir_cpf()
                    telefone = pedir_telefone()
                    email = pedir_email()
                    rua = pedir_rua()
                    numero = pedir_numero()
                    bairro = pedir_bairro()
                    sigla = pedir_sg_estados()
                    cep = pedir_cep()
                    senha = pedir_senha()
                    verificar_senha(senha)
                    verificar_bairro(bairro)
                    verificar_rua(rua)
                    login_tutor(cpf, senha)
                    dados_tutor = criando_usuario(nome, telefone, email, rua, bairro, numero, cep, sigla, cpf, senha)
                    print('Mudança feita com sucesso!')
                    contador += 1               
            case '4':
                if dados_tutor == '':
                    print('Nenhum perfil cadastrado ainda. Por favor, faça seu cadastro, escolhendo a opção (3) primeiro.')
                else:
                    exibir_perfil(dados_tutor)
            case '5':
                print('*-- Lista de animais PERDIDOS --*')
                if len(meus_animais_perdidos) == 0:
                    print('Nenhum animal perdido cadastrado.')
                else:
                    for i in meus_animais_perdidos:
                        print(i)
            case '6':
                print('*-- Lista de animais ENCONTRADOS --*')
                if len(meus_animais_encontrados) == 0:
                    print('Nenhum animal encontrado.')
                else:
                    for i in meus_animais_encontrados:
                        print(i)
            case '7':
                resetar_dados()
            case _:
                print('Opção inválida.') 
    escolha = input('Deseja voltar ao menu? (sim/não): ')
print('Obrigado por usar o PetSOS! Até logo.')

#Principal
principal()      