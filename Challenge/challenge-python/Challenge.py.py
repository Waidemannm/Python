#simulção de banco de dados
nomes_cadastrados = []
telefones_cadastrados = []
cpfs_cadastrados = []
senhas_cadastradas= []
consultas = []

def qtd_especialidades():
    """
    DESCRIÇÃO
        Solicita para algum funcionário digitat a quantidade de especialidades que estão disponiveis.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna a quantidade (int) de especialidades informada pelo usuário.
    """
     
    print('*-- Quantidade de especialidades --*')
    qtd = int(input('Quantidade: '))
    return qtd


def criar_lista_especialidades(qtd):
    """
    DESCRIÇÃO
        Cria uma lista de especialidades a partir da quantidade fornecida.
    PARÂMETROS
        qtd (int): número de especialidades a cadastrar.
    RETORNO
        Retorna a lista de especialidades (list de str).
    """
    print(f'*-- Criando um lista com {qtd} de especialidades --*')
    especialidades = [] 
    i = 0 
    while(i < qtd):
        especialidade = input('Digite o nome da especialidade: ')
        especialidades.append(especialidade)
        i+=1
    return especialidades

def agendar_consulta(especialidades):
    """
    DESCRIÇÃO
        Permite ao usuário agendar uma consulta médica, verificando se está cadastrado
        e se a especialidade existe na lista.
    PARÂMETROS
        especialidades (list): lista de especialidades disponíveis.
    RETORNO
        Retorna None. Exibe mensagem de sucesso ou erro no agendamento.
    """
    escolha = 'sim'
    while escolha.lower() == 'sim':
        print('*-- Agendar Consulta --*')
        print('------------------------')
        nome = input('Nome completo: ')
        telefone = input('Telefone com DDD: ')
        dia = input('Digite o dia desejado: ')
        mes = input('Digite o mês desejado: ')
        especialidade = input('Especialidade: ')
        observacoes = input('Observações (opcional): ')
        if (nome in nomes_cadastrados and telefone in telefones_cadastrados and especialidade in especialidades):
            print(f'{nome}, sua consulta foi marcada com {especialidade}, com as observações: "{observacoes}", no dia {dia}/{mes}.')
            break
        else:
            print('Erro ao agendar consulta. Verifique se você está cadastrado e se a especialidade digitada está disponível.')
            escolha = input('Deseja tentar marcar de novo? (sim/não): ')

def exibir_menu():
    """
    DESCRIÇÃO
        Exibe o menu principal com as opções disponíveis para o usuário.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna opcao, a escolha desejada pelo usuário.
    """
    print('*-- Assistente Virtual - HC --*')
    print('------------------------------')
    print('Seja bem vindo(a) ao Assistente Virtual - HC')
    opcao = int(input('Selecione a opção desejada \n(1) Agendar Consulta \n(2) Enviar Lembrete \n(3) Cadastrar Paciente \n(4) Ver calendário \n(5) Guia \nOpção: '))
    return opcao


def guia():
    """
    DESCRIÇÃO
        Exibe instruções e orientações gerais sobre o uso da plataforma,
        incluindo a apresentação do robô assistente.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna None. Mostra na tela o guia de uso e apresentação do robô.
    """
    print('*-- GUIA --*')
    print('------------')
    print('Bem-vindo a nossa Plataforma! Aqui você pode marcar suas consultas médicas de forma rápida e fácil. Siga os passos na tela se precisar, peça ajuda. Nosso objetivo é cuidar e facilitar seu dia a dia.')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('*-- Robô Assistente --*')
    print('-----------------------')
    print('Olá! Eu sou seu robô assistente de consultas. Estou aqu  para te ajudar a marcar, lembrar e acompanhar suas consultas médicas. Pode me chamar quando tiver dúvidas ou precisar de ajuda.')

def ver_calendario():
    """
    DESCRIÇÃO
        Simula a exibição de um calendário de consultas ao usuário.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna None. Exibe na tela exemplo de calendário.
    """
    print('Exibindo calendário de consultas... [exemplo visual simples aqui]')

def cadastro():
    """
    DESCRIÇÃO
        Cadastra um novo paciente, solicitando nome, CPF, telefone e senha,
        e realiza validações básicas de formato e duplicidade.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna None. Atualiza as listas globais de pacientes.
    """
    print('*-- Cadastro --*')
    print('-----------------')
    nome = input('Nome completo: ')
    cpf = input('CPF (somente números): ')
    telefone = input('Telefone com DDD: ')
    senha = input('Crie uma senha: ')
    if(len(cpf) == 11 and cpf.isdigit):
        cpfs_cadastrados.append(cpf)
    else:
        print('CPF inválido')
    if(cpf in cpfs_cadastrados):
          print(' Este CPF já está cadastrado.')
    if(len(telefone) == 11 and telefone.isdigit):
        telefones_cadastrados.append(telefone)
    else:
        print('Telefone inválido')
    if(telefone in telefones_cadastrados):
      print(' Este telefone já está cadastrado.')
      
def lembretes():
    """
    DESCRIÇÃO
        Pergunta ao usuário se deseja receber lembretes e valida o número
        de telefone antes de confirmar o agendamento dos lembretes.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna None. Exibe mensagens sobre o envio de lembretes ou erro.
    """
    print('Deseja receber lembretes da sua consulta?')
    tentativas = 5
    i = 0
    while(i < tentativas):
        telefone = input('Digite seu número: ')
        if(telefone in  telefones_cadastrados):
            print(f'Vamos enviar um lembrete 1 dia antes da sua consulta, e 2 horas antes da consulta para o telefone {telefone}')
            break
        else:
            print('Esse telefone não esta cadastrado')
            i += 1
    if (i == tentativas):
        print('Número de tentativas excedido. Tente criar um cadastro!')

def login():
    """
    DESCRIÇÃO
        Solicita login por CPF e senha, permitindo até 5 tentativas
        antes de bloquear o acesso.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna None. Exibe sucesso ou falha no login.
    """
    print('*-- Login --*')
    print('--------------')
    tentativas = 5
    i = 0
    while(i < tentativas):
        cpf = input('Digite seu CPF: ')
        senha = input('Digite sua senha:')
        if(cpf in cpfs_cadastrados and senha in senhas_cadastradas):
            print('Login feito com sucesso!')
            break
        else:
            print('Senha ou CPF incorreto"')
            i += 1
    if (i == tentativas):
       print('Número de tentativas excedido. Tente criar um cadastro!')


def principal():
    """
    DESCRIÇÂO
        Executa tudo o que estaria no principal, é feito para limpar a memória alocada 
    PARAMETRO
        Essa função não recebe parametro
    RETORNO
        Retorna a execução de todo o programa
    """
    qtd = qtd_especialidades()
    especialidades = criar_lista_especialidades(qtd)
    escolha = 'sim'
    while escolha.lower() == 'sim':
        opcao = exibir_menu()
        match opcao:
            case 1:
                agendar_consulta(especialidades)
            case 2:
                lembretes()
            case 3:
                cadastro()
            case 4:
                ver_calendario()
            case 5:
                guia()
            case _:
                print('Opção inválida.') 
    escolha = input('Deseja voltar ao menu? (sim/não): ')

#Principal
principal()