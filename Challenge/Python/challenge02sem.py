"""
Credenciais Moisés user:rm563719  pass:111206 host:oracle.fiap.com.br port:1521 service name:orcl
Credenciais Gabriel user:rm563650 pass:210706 host:oracle.fiap.com.br port:1521 service name:orcl
Credenciais Thiago user:rm565849 pass:190205 host:oracle.fiap.com.br port:1521 service name:orcl
*Coloque a opção de não possuir as tabelas no banco de dados, assim o sistema criará elas

Gerenciamento de Pacientes, Médicos e Consultas (CRUD)

MENU PRINCIPAL:

1- Pacientes
   Funções exigidas para CRUD de pacientes:
     • cpf_in_banco: verifica se CPF existe no banco de dados.
     • verificar_cpf: valida se o CPF contém somente dígitos, tem comprimento 11 e não está duplicado.
     • verificar_nome: verifica se nome não está vazio.
     • verificar_logradouro: verifica se nome do logradouro não está vazio.
     • verificar_estado: verifica se sigla de estado está entre aquelas permitidas (constraint do banco) e não está vazia.
     • verificar_cidade: verifica se NM_CIDADE não está vazio.
     • verificar_numero: verifica se número do logradouro é maior que zero; permite caracteres alfanuméricos (ex: “12A”).
     • verificar_ddd: verifica se DDD é um número entre 1 e 99.
     • verificar_telefone: verifica se telefone não está vazio, tem tamanho mínimo e máximo apropriados (ex: entre 6 e 9 dígitos).
     • validar_data_nascimento(DT_NASCIMENTO): valida se a data está no formato “dd/mm/aaaa”.

   Submenu “Pacientes”:
     • Create: pedir_cadastro_paciente() coleta inputs; cadastrar_paciente(...) insere histórico no banco.
     • Read: ler_paciente(NR_CPF) busca paciente pelo CPF e exibe seus dados.
     • Update: pedir_atualizacao_paciente() coleta novas informações; atualizar_paciente(...) atualiza os campos pertinentes.
     • Delete: deletar_paciente(NR_CPF) apaga registro do paciente dado seu CPF.

2- Consultas
   Funções exigidas para CRUD de consultas:
     • validar_data_consulta(DT_CONSULTA): valida formato “dd/mm/aaaa”.
     • id_paciente_in_banco(ID_PACIENTE): verifica se paciente com esse ID existe.
     • id_medico_in_banco(ID_MEDICO): verifica se médico com esse ID existe.
     • id_consulta_in_banco(ID_CONSULTA): verifica se consulta com esse ID existe.

   Submenu “Consultas”:
     • Create: pedir_cadastro_consulta() coleta inputs; cadastrar_consulta(...) insere nova consulta.
     • Read: ler_consulta(ID_CONSULTA) busca consulta por ID e exibe seus dados.
     • Update: pedir_atualizacao_consulta() coleta novas informações; atualizar_consulta(...) atualiza.
     • Delete: deletar_consulta(ID_CONSULTA) apaga consulta pelo ID.

3- Médicos
   Funções exigidas para CRUD de médicos:
     • crm_in_banco(NR_CRM): verifica se CRM já está cadastrado.
     • validar_crm(NR_CRM): verifica se CRM tem número de dígitos aceitável (ex: entre 5 e 8 dígitos) e não está duplicado.
     • id_medico_in_banco(ID_MEDICO): verifica se médico com esse ID existe.

   Submenu “Médicos”:
     • Create: pedir_cadastro_medico() coleta inputs; cadastrar_medico(...) insere novo médico.
     • Read: ler_medico(ID_MEDICO) busca médico por ID e mostra seus dados.
     • Update: pedir_atualizacao_medico() coleta novo dado(s); atualizar_medico(ID_MEDICO, NOVA_DS_ESPECIALIDADE) atualiza especialidade.
     • Delete: deletar_medico(ID_MEDICO) apaga médico pelo ID.

4- Apagar todos registros / Sair
   • apagar(): função que usa apagar_registro_consultas(), apagar_registro_pacientes(), apagar_registro_medicos() para deletar todos os dados do banco, se desejado.

Regras gerais:
- Usar docstrings nas funções com “descrição / parâmetros / retorno”.
- As credenciais são obtidas via pegar_credenciais(), que retorna (usuário, senha, host, porta, nome_do_serviço).
- getConnection(...) usa essas credenciais para conectar ao banco, para criar tabelas ou manipular dados.
- Funções de criar tabela só devem ser executadas quando as tabelas ainda não existirem.
"""

import oracledb

def verificar_user(USER):
    """
    DESCRIÇÃO
        Não permite o tamanho do USER ser igual a 0
    PARÂMETROS
        Recebe o USER 
    RETORNO
       Retorna True se o tamanho do USER for maior que 0 e false caso contrário
    """      
    if(len(USER) > 0):
        return True
    else:
        print('O USER não pode ser vazio')
        return False

def verificar_pass(PASS):
    """
    DESCRIÇÃO
        Não permite o tamanho do PASS ser igual a 0
    PARÂMETROS
        Recebe o PASS 
    RETORNO
       Retorna True se o tamanho do PASS for maior que 0 e false caso contrário
    """      
    if(len(PASS) > 0):
        return True
    else:
        print('O PASS não pode ser vazio')
        return False

def verificar_host(HOST):
    """
    DESCRIÇÃO
        Não permite o tamanho do HOST ser igual a 0
    PARÂMETROS
        Recebe o HOST 
    RETORNO
       Retorna True se o tamanho do HOST for maior que 0 e false caso contrário
    """      
    if(len(HOST) > 0):
        return True
    else:
        print('O HOST não pode ser vazio')
        return False

def verificar_port(PORT):
    """
    DESCRIÇÃO
        Não permite o tamanho da PORT ser igual a 0
    PARÂMETROS
        Recebe a PORT 
    RETORNO
       Retorna True se o tamanho da PORT for maior que 0 e false caso contrário
    """      
    if(len(PORT) > 0):
        return True
    else:
        print('A PORT não pode ser vazio')
        return False

def verificar_service_name(SERVICE_NAME):
    """
    DESCRIÇÃO
        Não permite o tamanho do SERVICE_NAME ser igual a 0
    PARÂMETROS
        Recebe o SERVICE_NAME 
    RETORNO
       Retorna True se o tamanho do SERVICE_NAME for maior que 0 e false caso contrário
    """      
    if(len(SERVICE_NAME) > 0):
        return True
    else:
        print('O SERVICE NAME não pode ser vazio')
        return False

def pegar_credenciais():
    """
    Obtém as credenciais de acesso ao banco.

    Retorna:
        tuple: (usuario, senha, host, porta, nome_do_serviço) se conseguir obter tudo,
        None caso contrário.
    """
    print('Credenciais para conectar ao Banco de Dados')
    while True:
            USER = input('User name: ') 
            if verificar_user(USER):
                break
    while True:
            PASS = input('Password: ')
            if verificar_pass(PASS):
                break       
    while True:
            HOST = input('Host: ')
            if verificar_host(HOST):
                break 
    while True:
            PORT = input('Port: ')
            if verificar_port(PORT):
                break             
    while True:
            SERVICE_NAME = input('Service name: ')
            if verificar_service_name(SERVICE_NAME):
                break                 

    return USER, PASS, HOST, PORT, SERVICE_NAME

def getConnection(USER, PASS, HOST, PORT, SERVICE_NAME):
  """
    Estabelece conexão com o banco de dados Oracle.

    Parâmetros:
        usuario (str): nome de usuário.
        senha (str): senha do usuário.
        host (str): endereço do servidor de banco.
        porta (str): porta de acesso.
        service_name (str): identificador ou serviço Oracle.

    Retorno:
        conexão Oracle se conexão for bem-sucedida, None caso contrário.
    """
  try:
    conn = oracledb.connect(user = USER, password = PASS, host = HOST, port= PORT, service_name = SERVICE_NAME)
    return conn
  except Exception as e:
    print(f'Erro na conexão com o banco de dados: {e}')
    return None

def criar_tabela_pacientes(conn):
    """
    DESCRIÇÃO
        Cria a tabela de pacientes no banco de dados
    PARÂMETROS
        Recebe a conexão com o banco de dados
    RETORNO
       Essa função não retorna nada
    """
    #Obtendo objeto cursor
    cursor = conn.cursor()
    try:
        create_table_sql = '''
        CREATE TABLE PACIENTES(
            ID_PACIENTE NUMBER(9) GENERATED ALWAYS AS IDENTITY,
            NM_PACIENTE VARCHAR2(80) NOT NULL,
            NR_CPF VARCHAR2(11) NOT NULL,
            DT_NASCIMENTO DATE NOT NULL,
            NR_DDD NUMBER(3) NOT NULL,
            NR_TELEFONE NUMBER(10) NOT NULL,
            NM_LOGRADOURO VARCHAR2(80) NOT NULL,
            NR_LOGRADOURO NUMBER(6) NOT NULL,
            NM_CIDADE VARCHAR2(50) NOT NULL,
            SG_ESTADO CHAR(2) NOT NULL,
            PRIMARY KEY (ID_PACIENTE),
            CONSTRAINT CK_SG_ESTADO CHECK (SG_ESTADO IN (
                'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA',
                'MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN',
                'RS','RO','RR','SC','SP','SE','TO'))
        )'''
        cursor.execute(create_table_sql)

    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')
    else:
        print('Tabela Pacientes criada com sucesso!')


def cpf_in_banco(NR_CPF, conn):
    """
    Verifica se um CPF já está registrado na tabela PACIENTES.

    Parâmetros:
        NR_CPF (str): CPF do paciente.

    Retorno:
        bool: True se o CPF já existir, False caso contrário.
    """
    if not conn:
        print('Erro na conexão com o banco de dados')
        return False

    try:
        cursor = conn.cursor()
        select_sql = "SELECT 1 FROM PACIENTES WHERE NR_CPF = :cpf"
        cursor.execute(select_sql, cpf=NR_CPF)

        result = cursor.fetchone()  # retorna a primeira linha encontrada
        if result:
            return True   # CPF já existe
        else:
            return False  # CPF não encontrado

    except oracledb.Error as e:
        print(f'Erro ao verificar CPF: {e}')
        return False

def verificar_cpf(NR_CPF, conn):
    """
    Valida o formato do CPF.

    Parâmetros:
        NR_CPF (str): CPF informado pelo usuário.

    Retorno:
        bool: True se CPF tiver exatamente 11 dígitos, somente números, e não constar no banco;
              False caso contrário.
    """
    if(len(NR_CPF) == 11 and NR_CPF.isdigit() and cpf_in_banco(NR_CPF, conn) == False):
        return True
    else:
        print('CPF inválido, deve conter 11 dígitos, apenas números')
        return False
    
def verificar_cpf_main(NR_CPF, conn):
    """
    Solicita via terminal os dados necessários para cadastrar um novo paciente.

    Retorno:
        tuple: (NM_PACIENTE, NR_CPF, DT_NASCIMENTO, NR_DDD, NR_TELEFONE, NM_LOGRADOURO, NR_LOGRADOURO, NM_CIDADE, SG_ESTADO)
        ou None se algo falhar.
    """
    if(len(NR_CPF) == 11 and NR_CPF.isdigit() and cpf_in_banco(NR_CPF, conn) == True):
        return True
    else:
        print('CPF inválido, deve conter 11 dígitos, apenas números e já estar cadastrado')
        return False

def verificar_nome(NM_PACIENTE):
    """
    DESCRIÇÃO
        Não permite o tamanho do nome ser igual a 0
    PARÂMETROS
        Recebe o NM_PACIENTE 
    RETORNO
       Retorna True se o tamanho do nome for maior que 0 e false caso contrário
    """      
    if(len(NM_PACIENTE) > 0):
        return True
    else:
        print('O nome não pode ser vazio')
        return False

def verificar_logradouro(NM_LOGRADOURO):
    """
    DESCRIÇÃO
        Não permite o tamanho do nome de lograduro ser igual a 0
    PARÂMETROS
        Recebe o NM_LOGRADOURO 
    RETORNO
       Retorna True se o tamanho do nome de logradouro for maior que 0 e false caso contrário
    """      
    if(len(NM_LOGRADOURO) > 0):
        return True
    else:
        print('O logradouro não pode ser vazio')
        return False

def verificar_numero(NR_LOGRADOURO):
    """
    DESCRIÇÃO
        erifica se o número do logradouro é válido.
        O número é considerado válido se não for None e for maior que 0.
    PARÂMETROS
        Recebe o NR_LOGRADOURO 
    RETORNO
       Retorna True se o número for válido (não None e maior que 0), 
        retorna False caso contrário e exibe uma mensagem de erro.
    """  
    if(NR_LOGRADOURO is not None and NR_LOGRADOURO > 0):
        return True
    else:
        print('Número inválido, não pode ser vazio e deve ser maior que 0.')
        return False

def verificar_cidade(NM_CIDADE):
    """
    DESCRIÇÃO
        Não permite o tamanho da cidade ser menor que zero e não ser uma string
    PARÂMETROS
        Recebe o NM_CIDADE 
    RETORNO
       Retorna True se o tamanho da cidade for maior que 0 e for apenas letras, retorna false caso contrário
    """ 
    if(len(NM_CIDADE) > 0 and isinstance(NM_CIDADE, str)): #falar pq eu usei isinstance para o professor
        return True
    else:
        print('O nome da ciadade não pode ser vazio e nem um número')
        return False

def verificar_ddd(NR_DDD):
    """
    DESCRIÇÃO
        Verifica se o DDD é válido.
        Um DDD é considerado válido se for um número inteiro entre 1 e 99.

    PARÂMETROS
            recebe NR_DDD
    RETORNO
            Retorna True se o DDD for válido, False caso contrário,
            exibindo uma mensagem de erro.
    """
    if(NR_DDD is not None and NR_DDD <= 99 and NR_DDD > 0):
        return True
    else:
        print('O número não pode ser vazio e entre 0 e 99')
        return False

def verificar_telefone(NR_TELEFONE):
    if(NR_TELEFONE is not None and NR_TELEFONE >= 10000  and NR_TELEFONE <= 999999999):
        return True
    else:
        print('O número não pode ser vazio, deve ser um número válido')
        return False
    
def verificar_sg_estado(SG_ESTADO):
    """
    DESCRIÇÃO
        Verifica se é um estado contido no check do atributo sg_estado no banco de dados e se não é vazio
    PARÂMETROS
        Recebe o SG_ESTADO 
    RETORNO
       Retorna True se a sigla estiver contida nos valores da constraint check de SG_ESTADO e se não for vazio, caso contrário retorna False
    """
    siglas_validas = {
        'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA',
        'MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN',
        'RS','RO','RR','SC','SP','SE','TO'
    }

    if SG_ESTADO is not None and SG_ESTADO.upper() in siglas_validas:
        return True
    else:
        print('Sigla de estado inválida. Deve ser uma das siglas oficiais do Brasil.')
        return False

def validar_data_nascimento(DT_NASCIMENTO):
    """
    DESCRIÇÃO
        ""
    Valida se a data está no formato dd/mm/aaaa
    PARÂMETROS
        Recebe DT_CONSUDT_NASCIMENTOLTA
    RETORNO
       Essa função retorna True se a data for válida ou False se for inválida
    """
    try:
        partes = DT_NASCIMENTO.split("/")  # divide oque o usuáro digitou em 3 partes, separadas pela "/"
        if len(partes) != 3:
            return False

        dia, mes, ano = partes

        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            return False

        dia, mes, ano = int(dia), int(mes), int(ano)

        if not (1 <= dia <= 31):
            return False
        if not (1 <= mes <= 12):
            return False
        if not (ano <= 2025):
            return False
        return True
    except:
        return False

def pedir_cadastro_paciente(conn):
    """
    DESCRIÇÃO
        Obtém informações para o cadastro de um paciente
    PARÂMETROS
        Não recebe nada
    RETORNO
       Essa função retorna os valores das colunas da tabela
    """ 
    try: 
        while True:
            NM_PACIENTE = input('Nome: ')
            if verificar_nome(NM_PACIENTE):
                break

        while True: 
            NR_CPF = input('Cpf: ')
            if verificar_cpf(NR_CPF, conn):
                break

        while True:
            DT_NASCIMENTO = input('Digite a data de nascimento (dd/mm/aaaa): ')
            if validar_data_nascimento(DT_NASCIMENTO):
                print('Data válida:', DT_NASCIMENTO)
                break
            else:
                print('Data inválida, tente novamente.') 

        while True: 
            NM_LOGRADOURO = input('Nome de logradouro: ')
            if verificar_logradouro(NM_LOGRADOURO):
                break

        while True: 
            try:
                NR_LOGRADOURO = int(input('Número: '))
                if verificar_numero(NR_LOGRADOURO):
                    break
            except ValueError as e:
                print(f'Erro: deve ser apenas números \n{e}')

        while True: 
            NM_CIDADE = input('Cidade: ')
            if verificar_cidade(NM_CIDADE):
                break
        
        while True: 
            try:
                NR_DDD = int(input('DDD do telefone: '))
                if verificar_ddd(NR_DDD):
                    break
            except ValueError as e:
                print(f'Erro: deve ser apenas números \n{e}')
        
        while True: 
            try:
                NR_TELEFONE = int(input('Número do telefone: '))
                if verificar_telefone(NR_TELEFONE):
                    break
            except ValueError as e:
                print(f'Erro: deve ser apenas números \n{e}')

        while True: 
            SG_ESTADO = input('Sigla do estado: ').upper()
            if verificar_sg_estado(SG_ESTADO):
                break
        return NM_PACIENTE, NR_CPF, DT_NASCIMENTO, NR_DDD, NR_TELEFONE, NM_LOGRADOURO, NR_LOGRADOURO, NM_CIDADE, SG_ESTADO
    except Exception as e:
        print(f'Não foi possível obter informações para o cadastro! \n{e}')

def cadastrar_paciente(NM_PACIENTE, NR_CPF, DT_NASCIMENTO, NR_DDD, NR_TELEFONE, NM_LOGRADOURO, NR_LOGRADOURO, NM_CIDADE, SG_ESTADO, conn):
    """
    Insere um novo paciente na tabela PACIENTES.

    Parâmetros:
        NM_PACIENTE (str): nome do paciente.
        NR_CPF (str): CPF.
        DT_NASCIMENTO (str): data de nascimento (formato dd/mm/aaaa).
        NR_DDD (int): código DDD.
        NR_TELEFONE (int): telefone.
        NM_LOGRADOURO (str): nome do logradouro.
        NR_LOGRADOURO (int): número do logradouro.
        NM_CIDADE (str): cidade.
        SG_ESTADO (str): sigla do estado.

    Retorno:
        None
    """ 
    print('Cadastrando Paciente')
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null
    try:
        cursor = conn.cursor() 
        insert_sql = """ 
            INSERT INTO PACIENTES (NM_PACIENTE, NR_CPF, DT_NASCIMENTO, NR_DDD, NR_TELEFONE, NM_LOGRADOURO, NR_LOGRADOURO, NM_CIDADE, SG_ESTADO) 
            VALUES (:NM_PACIENTE, :NR_CPF, TO_DATE(:DT_NASCIMENTO, 'DD/MM/YYYY'), :NR_DDD, :NR_TELEFONE, :NM_LOGRADOURO, :NR_LOGRADOURO, :NM_CIDADE, :SG_ESTADO)
        """
        cursor.execute(insert_sql, {
            'NM_PACIENTE' : NM_PACIENTE,
            'NR_CPF' : NR_CPF,
            'DT_NASCIMENTO' : DT_NASCIMENTO,
            'NR_DDD' : NR_DDD,
            'NR_TELEFONE' : NR_TELEFONE,
            'NM_LOGRADOURO' : NM_LOGRADOURO,
            'NR_LOGRADOURO' :NR_LOGRADOURO,
            'NM_CIDADE' :NM_CIDADE,
            'SG_ESTADO' : SG_ESTADO
        })
        conn.commit() #salva o registro
        print(f'Paciente {NM_PACIENTE} foi registrado com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao inserir Paciente: {e}')
        conn.rollback() #volta para o estado de segurança, do ultimo commit

def  ler_paciente(NR_CPF, conn): 
    """
    Recupera e exibe dados do paciente cujo CPF é informado.

    Parâmetros:
        NR_CPF (str): CPF do paciente a ser buscado. E conn

    Retorno:
        None
    """
    print('Lendo Paciente')
    if(cpf_in_banco(NR_CPF, conn) == True):

        if not conn: 
            print('Erro na conexão com o banco de dados') 
            return #retorna null
        try: 
            cursor = conn.cursor() 
            select_sql = """
                SELECT * FROM PACIENTES WHERE NR_CPF = :NR_CPF
            """
            cursor.execute(select_sql, {'NR_CPF': NR_CPF})
            print('\n --- Informações do Paciente ---')
            row = cursor.fetchone() #falar pq eu usei o fetchone para o professor
            print(f'ID: {row[0]} \n Nome: {row[1]}\n CPF: {row[2]}, \nData nascimento: {row[3]}  \n Telefone: ({row[4]}-{row[5]}) \n Endereço: {row[6]} {row[7]}, {row[8]} - {row[9]}')
        except oracledb.Error as e:
            print(f'Erro ao ler e exibir registros do Paciente: {e}')
    else:
        print(f'Nenhum paciente cadastrado com o cpf: {NR_CPF}')

def pedir_atualizacao_paciente(conn):
    """
    DESCRIÇÃO
        Obtém informações para a atualizção de um paciente
    PARÂMETROS
        Não recebe nada
    RETORNO
       Essa função retorna os valores das colunas da tabela
    """ 
    while True: 
        NR_CPF = input('Cpf: ')
        if verificar_cpf_main(NR_CPF, conn):
            break

    while True: 
        NOVO_LOGRADOURO = input('Novo nome de logradouro: ')
        if verificar_logradouro(NOVO_LOGRADOURO):
            break

    while True: 
        try:
            NOVO_NUMERO = int(input('Novo número: '))
            if verificar_numero(NOVO_NUMERO):
                break
        except ValueError as e:
            print(f'Erro: deve ser apenas números \n{e}')

    while True: 
        NOVA_CIDADE = input('Nova cidade: ')
        if verificar_cidade(NOVA_CIDADE):
            break
        
    while True: 
        NOVA_SIGLA = input('Nova sigla do estado: ').upper()
        if verificar_sg_estado(NOVA_SIGLA):
            break
    
    while True: 
        try:
            NOVO_DDD = int(input('Novo DDD do telefone: '))
            if verificar_ddd(NOVO_DDD):
                break
        except ValueError as e:
            print(f'Erro: deve ser apenas números \n{e}')
    
    while True: 
        try:
            NOVO_TELEFONE = int(input('Novo número de telefone: '))
            if verificar_telefone(NOVO_TELEFONE):
                break
        except ValueError as e:
            print(f'Erro: deve ser apenas números \n{e}')
    return NR_CPF, NOVO_LOGRADOURO, NOVO_NUMERO, NOVA_CIDADE, NOVA_SIGLA, NOVO_DDD, NOVO_TELEFONE
                       
def atualizar_paciente(NR_CPF, NOVO_LOGRADOURO, NOVO_NUMERO, NOVA_CIDADE, NOVA_SIGLA, NOVO_DDD, NOVO_TELEFONE, conn):
    """
    Atualiza endereço e telefone de paciente.

    Parâmetros:
        NR_CPF (str): CPF que identifica o paciente.
        NOVO_LOGRADOURO (str): novo nome de logradouro.
        NOVO_NUMERO (int): novo número.
        NOVA_CIDADE (str): nova cidade.
        NOVA_SIGLA (str): nova sigla de estado.
        NOVO_DDD (int): novo DDD.
        NOVO_TELEFONE (int): novo número de telefone.

    Retorno:
        None
    """ 
    print('** Atualizando registro **') 

    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        update_sql = """
                    UPDATE PACIENTES 
                    SET NM_LOGRADOURO = :NOVO_LOGRADOURO, 
                    NR_LOGRADOURO = :NOVO_NUMERO, 
                    NM_CIDADE = :NOVA_CIDADE, 
                    SG_ESTADO = :NOVA_SIGLA, 
                    NR_DDD = :NOVO_DDD, 
                    NR_TELEFONE = :NOVO_TELEFONE 
                    WHERE NR_CPF = :NR_CPF
                """
        cursor.execute(update_sql, {'NOVO_LOGRADOURO' : NOVO_LOGRADOURO, 
                                    'NOVO_NUMERO' : NOVO_NUMERO,
                                    'NOVA_CIDADE' : NOVA_CIDADE,
                                    'NOVA_SIGLA' : NOVA_SIGLA,
                                    'NOVO_DDD' : NOVO_DDD,
                                    'NOVO_TELEFONE' : NOVO_TELEFONE,
                                    'NR_CPF' : NR_CPF})
        conn.commit() #salva o update
        if (cursor.rowcount > 0):  
            print(f'Registro do Paciente alterado com sucesso!')
        else:
            print(f'Nenhum Paciente encontrado com cpf: {NR_CPF}')
    except oracledb.Error as e:
        print(f'Erro ao atualizar paciente: {e}')


def deletar_paciente(NR_CPF, conn):
    """
    DESCRIÇÃO
        Deleta um registro na tabela de Pacientes
    PARÂMETROS
        Recebe o NR_CPF para identificar a linha da tabela a ser excluida
    RETORNO
       Essa função não retorna nada
    """ 
    print('** Apagando um registro **') 
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        delete_sql = """
                    DELETE FROM PACIENTES WHERE NR_CPF = :NR_CPF 
                """
        cursor.execute(delete_sql, {'NR_CPF' : NR_CPF})
        conn.commit() #salva o delete
        if (cursor.rowcount > 0):  
            print(f'Registro do Paciente deletado com sucesso!')
        else:
            print(f'Nenhum Paciente encontrado com cpf: {NR_CPF}')
    except oracledb.Error as e:
        print(f'Erro ao deletar registros de pacientes, o paciente só pode ser deletado se não tiver nenhuma consulta marcada {e}')

def criar_tabela_medicos(conn):
    """
    DESCRIÇÃO
        Cria a tabela de médicos no banco de dados
    PARÂMETROS
        Recebe a conexão com o banco de dados
    RETORNO
       Essa função não retorna nada
    """
    #Obtendo objeto cursor
    cursor = conn.cursor()
    try:
        create_table_sql = '''
        CREATE TABLE MEDICOS(
            ID_MEDICO NUMBER(9) GENERATED ALWAYS AS IDENTITY,
            NM_MEDICO VARCHAR2(80) NOT NULL,
            NR_CPF NUMBER(12) NOT NULL,
            DT_NASCIMENTO DATE NOT NULL,
            NR_CRM NUMBER(10) NOT NULL,
            DS_ESPECIALIDADE VARCHAR2(50) NOT NULL,
            PRIMARY KEY (ID_MEDICO)
        )'''
        cursor.execute(create_table_sql)

    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')
    else:
        print('Tabela Medicos criada com sucesso!')

def crm_in_banco(NR_CRM, conn):
    """
    DESCRIÇÃO
        Não permite registrar um crm já registrado no banco de dados
    PARÂMETROS
        Recebe o NR_CRM e conn
    RETORNO
       Retorna True se o crm já existir no banco, False caso contrário.
    """ 
    if not conn:
        print('Erro na conexão com o banco de dados')
        return False
    try:
        cursor = conn.cursor()
        select_sql = "SELECT 1 FROM MEDICOS WHERE NR_CRM = :NR_CRM"
        cursor.execute(select_sql, NR_CRM=NR_CRM)

        result = cursor.fetchone()  # retorna a primeira linha encontrada
        if result:
            return True   # CPF já existe
        else:
            return False  # CPF não encontrado

    except oracledb.Error as e:
        print(f'Erro ao verificar CRM: {e}')
        return False

def validar_crm(NR_CRM, conn):
    """
    DESCRIÇÃO
        Não permite o CRM ser menor que 9999 e maior que 99999999
    PARÂMETROS
        Recebe o NR_CRM e conn
    RETORNO
       Retorna True se o NR_CRM  não for menor que 9999 e maior que 99999999 e não estiver registra no banco de dados, ou False caso contrário
    """ 
    if(NR_CRM > 9999 and NR_CRM < 100000000 and crm_in_banco(NR_CRM, conn) == False):
        return True
    else:
        print('CRM inválido, não pode ser menor que 9999 e maior que 99999999')
        return False

def pedir_cadastro_medico(conn):
    """
    DESCRIÇÃO
        Obtém informações para o cadastro de um medico
    PARÂMETROS
        Recebe conn
    RETORNO
       Essa função retorna uma tupla com os valores das colunas da tabela
    """
    try: 
        while True:
            NM_MEDICO = input('Nome: ')
            if verificar_nome(NM_MEDICO):
                break

        while True: 
            NR_CPF = input('Cpf: ')
            if verificar_cpf(NR_CPF, conn):
                break

        while True:
            DT_NASCIMENTO = input('Digite a data de nascimento (dd/mm/aaaa): ')
            if validar_data_nascimento(DT_NASCIMENTO):
                print('Data válida:', DT_NASCIMENTO)
                break
            else:
                print('Data inválida, tente novamente.') 
        
        while True: 
            try:
                NR_CRM = int(input('Crm: '))
                if validar_crm(NR_CRM, conn):
                    break
            except ValueError as e:
                print(f'O CRM deve ser um número! \n{e}')

        DS_ESPECIALIDADE = input('Qual a especialidade do médico: ')

        return NM_MEDICO, NR_CPF, DT_NASCIMENTO, NR_CRM, DS_ESPECIALIDADE
    
    except Exception as e:
        print(f'Não foi possível obter informações para o cadastro! \n{e}')

def cadastrar_medico(NM_MEDICO, NR_CPF, DT_NASCIMENTO, NR_CRM, DS_ESPECIALIDADE, conn):
    """
    DESCRIÇÃO
        Registra um medico na tabela de medicos
    PARÂMETROS
        Recebe os valores das colunas que serão registradas e a conexão
    RETORNO
       Essa função não retorna nada
    """ 
    print('Cadastrando Médico')
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null
    try:
        cursor = conn.cursor() 
        insert_sql = """ 
            INSERT INTO MEDICOS (NM_MEDICO, NR_CPF, DT_NASCIMENTO, NR_CRM, DS_ESPECIALIDADE) 
            VALUES (:NM_MEDICO, :NR_CPF, TO_DATE(:DT_NASCIMENTO, 'DD/MM/YYYY'), :NR_CRM, :DS_ESPECIALIDADE)
        """
        cursor.execute(insert_sql, {
            'NM_MEDICO' : NM_MEDICO,
            'NR_CPF' : NR_CPF,
            'DT_NASCIMENTO' : DT_NASCIMENTO,
            'NR_CRM' : NR_CRM,
            'DS_ESPECIALIDADE' : DS_ESPECIALIDADE
        })
        conn.commit() #salva o registro
        print(f'Médico {NM_MEDICO} foi registrado com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao inserir Médico: {e}')
        conn.rollback() #volta para o estado de segurança, do ultimo commit


def ler_medico(ID_MEDICO, conn):
    """
    DESCRIÇÃO
        Lê uma médico da tabela de medicos
    PARÂMETROS
        Recebe ID_MEDICO para identificar apenas um registro e a conn
    RETORNO
       Essa função não retorna nada
    """ 
    print('Lendo Médico')
    if(id_medico_in_banco(ID_MEDICO, conn) == True):
        if not conn: 
            print('Erro na conexão com o banco de dados') 
            return #retorna null
        try: 
            cursor = conn.cursor() 
            select_sql = """
                SELECT * FROM MEDICOS WHERE ID_MEDICO = :ID_MEDICO
            """
            cursor.execute(select_sql, {'ID_MEDICO': ID_MEDICO})
            print('\n --- Informações do Médico ---')
            row = cursor.fetchone() #falar pq eu usei o fetchone para o professor
            print(f'ID: {row[0]} \nNome: {row[1]} \nCPF: {row[2]} \nData de nascimento: {row[3]} \nCRM: {row[4]} \nEspecialidade: {row[5]}')
        except oracledb.Error as e:
            print(f'Erro ao ler e exibir registros da Consulta: {e}')
    else:
        print(f'Nenhum Médico cadastrado com o ID: {ID_MEDICO}')

def atualizar_medico(ID_MEDICO, NOVA_DS_ESPECIALIDADE, conn):
    """
    DESCRIÇÃO
        Atualiza as informações de um registro de médico
    PARÂMETROS
        Recebe os novos valores de endereço (ID_MEDICO, DS_ESPECIALIDADE), e o ID_MEDICO para identificar o medico a ser modificado e a conn
    RETORNO
       Essa função não retorna nada
    """ 
    print('** Atualizando médico **') 
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        update_sql = """
                    UPDATE MEDICOS 
                    SET DS_ESPECIALIDADE = :NOVA_DS_ESPECIALIDADE
                    WHERE ID_MEDICO = :ID_MEDICO
                """
        cursor.execute(update_sql, {'NOVA_DS_ESPECIALIDADE' : NOVA_DS_ESPECIALIDADE, 
                                    'ID_MEDICO' : ID_MEDICO})
        conn.commit() #salva o update
        if (cursor.rowcount > 0):  
            print(f'Registro de médico alterado com sucesso!')
        else:
            print(f'Nenhum médico encontrado com ID: {ID_MEDICO}')
    except oracledb.Error as e:
        print(f'Erro ao atualizar médico" \n{e}')


def pedir_atualizacao_medico(conn):
    """
    DESCRIÇÃO
        Obtém informações para a atualização de um médico
    PARÂMETROS
        Recebe a conn
    RETORNO
       Essa função retorna os valores das colunas da tabela
    """
    while True:
            try:
                ID_MEDICO = int(input('ID do médico: '))
                if id_medico_in_banco(ID_MEDICO, conn):  
                    break
                else:
                    print("ID não encontrado no banco, tente novamente.")
            except ValueError as e:
                print(f'O ID deve ser um  número! \n{e}')

    NOVA_DS_ESPECIALIDADE = input('Digite uma nova nova especialidade do médico, ou a mesma: ')
    
    return ID_MEDICO, NOVA_DS_ESPECIALIDADE

def deletar_medico(ID_MEDICO, conn):
    """
    DESCRIÇÃO
        Deleta um registro na tabela de Medicos
    PARÂMETROS
        Recebe o ID_MEDICO para identificar a linha da tabela a ser excluida e a conn
    RETORNO
       Essa função não retorna nada
    """ 
    print('** Apagando um registro **') 

    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        delete_sql = """
                    DELETE FROM MEDICOS WHERE ID_MEDICO = :ID_MEDICO 
                """
        cursor.execute(delete_sql, {'ID_MEDICO' : ID_MEDICO})
        conn.commit() #salva o delete
        if (cursor.rowcount > 0):  
            print(f'Registro do médico deletado com sucesso!')
        else:
            print(f'Nenhum médico encontrado com ID: {ID_MEDICO}')
    except oracledb.Error as e:
        print(f'Erro ao deletar registros do médico, o médico só pode ser deletado se não tiver nenhuma consulta marcada! \n{e}')


def criar_tabela_consultas(conn):
    """
    DESCRIÇÃO
        Cria a tabela de consultas no banco de dados
    PARÂMETROS
        Recebe a conexão com o banco de dados
    RETORNO
       Essa função não retorna nada
    """
    #Obtendo objeto cursor
    cursor = conn.cursor()
    try:
        create_table_sql = '''
        CREATE TABLE CONSULTAS(
            ID_CONSULTA NUMBER(9) GENERATED ALWAYS AS IDENTITY,
            ID_PACIENTE NUMBER(9) NOT NULL,
            ID_MEDICO NUMBER(9) NOT NULL,
            DT_CONSULTA DATE NOT NULL,
            DS_CONSULTA VARCHAR2(50) NOT NULL,
            PRIMARY KEY (ID_CONSULTA),
            FOREIGN KEY (ID_MEDICO) REFERENCES MEDICOS(ID_MEDICO),
            FOREIGN KEY (ID_PACIENTE) REFERENCES PACIENTES(ID_PACIENTE)
        )'''
        cursor.execute(create_table_sql)

    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')
    else:
        print('Tabela Medicos criada com sucesso!')


def validar_data_consulta(DT_CONSULTA):
    """
    DESCRIÇÃO
        ""
    Valida se a data está no formato dd/mm/aaaa
    PARÂMETROS
        Recebe DT_CONSULTA
    RETORNO
       Essa função retorna True se a data for válida ou False se for inválida
    """
    try:
        partes = DT_CONSULTA.split("/")  # divide oque o usuáro digitou em 3 partes, separadas pela "/"
        if len(partes) != 3:
            return False

        dia, mes, ano = partes

        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            return False

        dia, mes, ano = int(dia), int(mes), int(ano)

        if not (1 <= dia <= 31):
            return False
        if not (1 <= mes <= 12):
            return False
        if not (ano <= 2025):
            return False
        return True
    except:
        return False

def id_medico_in_banco(ID_MEDICO, conn):
    """
    DESCRIÇÃO
        Verifica se existe um ID_MEDICO já está cadastrado
    PARÂMETROS
        Recebe o ID_MEDICO e a conn
    RETORNO
       Retorna True se o ID_MEDICO já existir no banco, False caso contrário
    """ 
    if not conn:
        print('Erro na conexão com o banco de dados')
        return False

    try:
        cursor = conn.cursor()
        select_sql = "SELECT 1 FROM MEDICOS WHERE ID_MEDICO = :ID_MEDICO"
        cursor.execute(select_sql, ID_MEDICO=ID_MEDICO)

        result = cursor.fetchone()  # retorna a primeira linha encontrada
        if result:
            return True   # CPF já existe
        else:
            return False  # CPF não encontrado

    except oracledb.Error as e:
        print(f'Erro ao verificar Id do medico: {e}')
        return False

def id_paciente_in_banco(ID_PACIENTE, conn):
    """
    DESCRIÇÃO
        Verifica se existe um ID_PACIENTE já está cadastrado
    PARÂMETROS
        Recebe o ID_PACIENTE e a conn
    RETORNO
       Retorna True se o ID_PACIENTE já existir no banco, False caso contrário
    """ 
    if not conn:
        print('Erro na conexão com o banco de dados')
        return False

    try:
        cursor = conn.cursor()
        select_sql = "SELECT 1 FROM PACIENTES WHERE ID_PACIENTE = :ID_PACIENTE"
        cursor.execute(select_sql, ID_PACIENTE=ID_PACIENTE)

        result = cursor.fetchone()  # retorna a primeira linha encontrada
        if result:
            return True   # CPF já existe
        else:
            return False  # CPF não encontrado

    except oracledb.Error as e:
        print(f'Erro ao verificar CPF: {e}')
        return False


def pedir_cadastro_consulta(conn):
    """
    DESCRIÇÃO
        Obtém informações para o cadastro de uma consulta
    PARÂMETROS
        Recebe a conn
    RETORNO
       Essa função retorna uma tupla com os valores das colunas da tabela
    """ 
    try:    
        while True:
            try:
                ID_PACIENTE = int(input('ID do paciente: '))
                if id_paciente_in_banco(ID_PACIENTE, conn):  
                    break
                else:
                    print("ID não encontrado no banco, tente novamente.")
            except ValueError as e:
                print(f'O ID deve ser um  número! \n{e}')
            
        while True:
            try:
                ID_MEDICO = int(input('ID do médico: '))
                if id_medico_in_banco(ID_MEDICO, conn):  
                    break
                else:
                    print("ID não encontrado no banco, tente novamente.")
            except ValueError as e:
                print(f'O ID deve ser um  número! \n{e}')

        while True:
            DT_CONSULTA = input('Digite a data da consulta (dd/mm/aaaa): ')
            if validar_data_consulta(DT_CONSULTA):
                print('Data válida:', DT_CONSULTA)
                break
            else:
                print('Data inválida, tente novamente.')

        DS_CONSULTA = input('Digite uma descrição sobre o que é a consulta: ')

        return ID_PACIENTE,ID_MEDICO,DT_CONSULTA,DS_CONSULTA
    except ValueError as e:
        print(f'Não foi possível obter informações para o cadastro! \n{e}')

def cadastrar_consulta(ID_PACIENTE,ID_MEDICO,DT_CONSULTA,DS_CONSULTA, conn):
    """
    DESCRIÇÃO
        Registra uma consulta ligada á um paciente
    PARÂMETROS
        Recebe os valores das colunas que serão registradas e a conn
    RETORNO
       Essa função não retorna nada
    """ 
    print('Cadastrando Consulta')
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null
    try: 

        cursor = conn.cursor() 
        insert_sql = """ 
            INSERT INTO CONSULTAS (ID_PACIENTE, ID_MEDICO, DT_CONSULTA, DS_CONSULTA) 
            VALUES (:ID_PACIENTE, :ID_MEDICO, TO_DATE(:DT_CONSULTA, 'DD/MM/YYYY'), :DS_CONSULTA)
        """
        cursor.execute(insert_sql, {
            'ID_PACIENTE' : ID_PACIENTE,
            'ID_MEDICO' : ID_MEDICO,
            'DT_CONSULTA' : DT_CONSULTA,
            'DS_CONSULTA' : DS_CONSULTA
        })
        conn.commit() #salva o registro
        print(f'Consulta com descrição: {DS_CONSULTA} \nID médico da consulta: {ID_MEDICO} \nID paciente da consulta: {ID_PACIENTE}  \nRegistrada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao inserir Paciente: {e}')
        conn.rollback() #volta para o estado de segurança, do ultimo commit


def id_consulta_in_banco(ID_CONSULTA, conn):
    """
    DESCRIÇÃO
        Verifica se um ID_CONSULTA está registrado
    PARÂMETROS
        Recebe o ID_CONSULTA e a conn
    RETORNO
       Retorna True se o ID_CONSULTA já existir no banco, False caso contrário.
    """ 

    if not conn:
        print('Erro na conexão com o banco de dados')
        return False

    try:
        cursor = conn.cursor()
        select_sql = "SELECT 1 FROM CONSULTAS WHERE ID_CONSULTA = :ID_CONSULTA"
        cursor.execute(select_sql, ID_CONSULTA=ID_CONSULTA)

        result = cursor.fetchone()  # retorna a primeira linha encontrada
        if result:
            return True   # CPF já existe
        else:
            return False  # CPF não encontrado

    except oracledb.Error as e:
        print(f'Erro ao verificar ID da consulta: {e}')


def ler_consulta(ID_CONSULTA, conn):
    """
    DESCRIÇÃO
        Lê uma consulta da tabela de consultas
    PARÂMETROS
        Recebe ID_CONSULTA para identificar apenas um registro e a conn
    RETORNO
       Essa função não retorna nada
    """ 
    print('Lendo Consulta')
    if(id_consulta_in_banco(ID_CONSULTA, conn) == True):

        if not conn: 
            print('Erro na conexão com o banco de dados') 
            return #retorna null
        try: 
            cursor = conn.cursor() 
            select_sql = """
                SELECT * FROM CONSULTAS WHERE ID_CONSULTA = :ID_CONSULTA
            """
            cursor.execute(select_sql, {'ID_CONSULTA': ID_CONSULTA})
            print('\n --- Informações da Consulta ---')
            row = cursor.fetchone() #falar pq eu usei o fetchone para o professor
            print(f'ID da consulta: {row[0]} \nID do paciente: {row[1]} \nID do médico: {row[2]} \nData da consulta: {row[3]} \nDescrição: {row[4]}')
        except oracledb.Error as e:
            print(f'Erro ao ler e exibir registros da Consulta: {e}')
    else:
        print(f'Nenhuma consulta cadastrada com o ID: {ID_CONSULTA}')

def pedir_atualizacao_consulta(conn):
    """
    DESCRIÇÃO
        Obtém informações para a atualização de uma consulta
    PARÂMETROS
        Recebe a conn
    RETORNO
       Essa função retorna uma tupla com  os valores das colunas da tabela
    """
    while True:
            try:
                ID_CONSULTA = int(input('ID da consulta: '))
                if id_consulta_in_banco(ID_CONSULTA, conn):  
                    break
                else:
                    print("ID não encontrado no banco, tente novamente.")
            except ValueError as e:
                print(f'O ID deve ser um  número! \n{e}')
            
    while True:
        try:
            NOVO_ID_MEDICO = int(input('ID do novo médico (ou do mesmo): '))
            if id_medico_in_banco(NOVO_ID_MEDICO, conn):  
                break
            else:
                print("ID não encontrado no banco, tente novamente.")
        except ValueError as e:
            print(f'O ID deve ser um  número! \n{e}')

    while True:
        NOVA_DT_CONSULTA = input('Digite a nova data da consulta (dd/mm/aaaa) (ou a mesma): ')
        if validar_data_consulta(NOVA_DT_CONSULTA):
            print('Data válida:', NOVA_DT_CONSULTA)
            break
        else:
            print('Data inválida, tente novamente.')

    NOVA_DS_CONSULTA = input('Digite uma nova descrição sobre o que é a consulta (ou a mesma): ')
    
    return ID_CONSULTA, NOVO_ID_MEDICO, NOVA_DT_CONSULTA, NOVA_DS_CONSULTA

def atualizar_consulta(ID_CONSULTA, NOVO_ID_MEDICO, NOVA_DT_CONSULTA, NOVA_DS_CONSULTA, conn):
    """
    DESCRIÇÃO
        Atualiza as informações de um registro de consulta
    PARÂMETROS
        Recebe os novos valores de endereço (ID_CONSULTA, NOVO_ID_MEDICO, NOVA_DT_CONSULTA, NOVA_DS_CONSULTA), e o ID_CONULTA para identificar a consulta a ser modificado e a conn
    RETORNOat
       Essa função não retorna nada
    """ 
    print('** Atualizando consulta **') 

    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 


        update_sql = """
                    UPDATE CONSULTAS 
                    SET ID_MEDICO = :NOVO_ID_MEDICO, 
                    DT_CONSULTA = TO_DATE(:NOVA_DT_CONSULTA, 'DD/MM/YYYY'),
                    DS_CONSULTA = :NOVA_DS_CONSULTA
                    WHERE ID_CONSULTA = :ID_CONSULTA
                """
        cursor.execute(update_sql, {'NOVO_ID_MEDICO' : NOVO_ID_MEDICO, 
                                    'NOVA_DT_CONSULTA' : NOVA_DT_CONSULTA,
                                    'NOVA_DS_CONSULTA' : NOVA_DS_CONSULTA,
                                    'ID_CONSULTA' : ID_CONSULTA})
        conn.commit() #salva o update
        if (cursor.rowcount > 0):  
            print(f'Registro da consulta alterado com sucesso!')
        else:
            print(f'Nenhuma Consulta encontrada com ID: {ID_CONSULTA}')
    except oracledb.Error as e:
        print(f'Erro ao atualizar consulta \n{e}')


def deletar_consulta(ID_CONSULTA, conn):
    """
    DESCRIÇÃO
        Deleta um registro na tabela de Consultas
    PARÂMETROS
        Recebe o ID_CONSULTA para identificar a linha da tabela a ser excluida e a conn
    RETORNO
       Essa função não retorna nada
    """ 
    print('** Apagando um registro **')  
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        delete_sql = """
                    DELETE FROM CONSULTAS WHERE ID_CONSULTA = :ID_CONSULTA 
                """
        cursor.execute(delete_sql, {'ID_CONSULTA' : ID_CONSULTA})
        conn.commit() #salva o delete
        if (cursor.rowcount > 0):  
            print(f'Registro da Consulta deletado com sucesso!')
        else:
            print(f'Nenhuma consulta encontrado com ID: {ID_CONSULTA}')
    except oracledb.Error as e:
        print(f'Erro ao deletar registros de Consultas: {e}')

def exibir_submenu_pacientes():
    """
    DESCRIÇÃO
        Exibe o submenu pacientes com as opções disponíveis para o usuário.
    PARÂMETROS
        Essa função recebe não parâmetro.
    RETORNO
        Retorna opcao_paciente, a escolha desejada pelo usuário.
    """
    print('*--Submenu Paciente--*')
    print('------------------------------')
    try:
        opcao_paciente = int(input('Selecione a opção desejada \n(1) Cadastrar Pacientes\n(2) Listar Paciente \n(3) Atualizar Pacientes\n(4) Deletar Pacientes\nOpção: '))
    except ValueError as e:
        print(f'Você deve inserir um número entre (1 e 4). {e}')
    return opcao_paciente

def exibir_submenu_consultas():
    """
    DESCRIÇÃO
        Exibe o submenu consultas com as opções disponíveis para o usuário.
    PARÂMETROS
        Essa função recebe não parâmetro.
    RETORNO
        Retorna opcao_consulta, a escolha desejada pelo usuário.
    """
    print('*--Submenu Consultas--*')
    print('------------------------------')
    try:
        opcao_consulta = int(input('Selecione a opção desejada \n(1) Cadastrar Consulta \n(2) Listar Consultas \n(3) Atualizar Consulta\n(4) Deletar Consulta \nOpção: '))
    except ValueError as e:
        print(f'Você deve inserir um número entre (1 e 4). {e}')
    return opcao_consulta

def exibir_submenu_medicos():
    """
    DESCRIÇÃO
        Exibe o submenu médicos com as opções disponíveis para o usuário.
    PARÂMETROS
        Essa função recebe não parâmetro.
    RETORNO
        Retorna opcao_medico, a escolha desejada pelo usuário.
    """
    print('*--Submenu Consultas--*')
    print('------------------------------')
    try:
        opcao_medico = int(input('Selecione a opção desejada \n(1) Cadastrar Médico \n(2) Listar Médico \n(3) Atualizar Médico\n(4) Deletar Médico \nOpção: '))
    except ValueError as e:
        print(f'Você deve inserir um número entre (1 e 4). {e}')
    return opcao_medico

def apagar(conn):
    """
    DESCRIÇÃO
        Apaga todos os registros do banco de dados de todas as tabelas
    PARÂMETROS
        Recebe a conn
    RETORNO
        Não retorna nada
    """
    print('** Apagando todos os registro **') 
    apagar_registro_consultas(conn)
    apagar_registro_medicos(conn)
    apagar_registro_pacientes(conn)
    
    
def apagar_registro_consultas(conn):
    """
    DESCRIÇÃO
        Apaga todos os registros de consultas
    PARÂMETROS
        Não recebe parametros 
    RETORNO
        Não retorna nada
    """
    print('-- Apagando registros de consultas --') 
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        delete_sql = """
                    DELETE FROM CONSULTAS 
                """
        cursor.execute(delete_sql)
        conn.commit() #salva o delete
        if (cursor.rowcount > 0):  
            print(f'Todos os registros foram deletado com sucesso!')
        else:
            print(f'Não havia registros')
    except oracledb.Error as e:
        print(f'Erro ao deletar registros de Consultas: {e}')


def apagar_registro_pacientes(conn):
    """
    DESCRIÇÃO
        Apaga todos os registros de pacientes
    PARÂMETROS
        Recebe a conn
    RETORNO
        Não retorna nada
    """
    print('-- Apagando registros de pacientes --') 
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        delete_sql = """
                    DELETE FROM PACIENTES 
                """
        cursor.execute(delete_sql)
        conn.commit() #salva o delete
        if (cursor.rowcount > 0):  
            print(f'Todos os registros foram deletado com sucesso!')
        else:
            print(f'Não havia registros')
    except oracledb.Error as e:
        print(f'Erro ao deletar registros de Pacientes: {e}')


def apagar_registro_medicos(conn):
    """
    DESCRIÇÃO
        Apaga todos os registros de medicos
    PARÂMETROS
        Recebe a conn
    RETORNO
        Não retorna nada
    """
    print('-- Apagando registros de médicos --') 
    if not conn: 
        print('Erro na conexão com o banco de dados') 
        return #retorna null 
    try: 
        cursor = conn.cursor() 
        delete_sql = """
                    DELETE FROM MEDICOS 
                """
        cursor.execute(delete_sql)
        conn.commit() #salva o delete
        if (cursor.rowcount > 0):  
            print(f'Todos os registros foram deletado com sucesso!')
        else:
            print(f'Não havia registros')
    except oracledb.Error as e:
        print(f'Erro ao deletar registros de Médicos: {e}')


def exibir_menu():
    """
    DESCRIÇÃO
        Exibe o menu principal com as opções disponíveis para o usuário.
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Retorna opcao, a escolha desejada pelo usuário.
    """
    print('*-- Cuida + HC --*')
    print('------------------------------')
    print('Seja bem vindo(a) ao Cuida + HC')
    try:
        opcao = int(input('Selecione a opção desejada \n(1) Pacientes \n(2) Consultas \n(3) Médicos \n(4) Apagar Tudo \nOpção: '))
    except ValueError as e:
        print(f'Você deve inserir um número entre (1 e 4). {e}')
    return opcao


def principal(conn):
    """
    DESCRIÇÃO
        Função que exibe o fluxo do sistema
    PARÂMETROS
        Recebe a conn
    RETORNO
        Não possui retorno
    """
    escolha = 'SIM'
    while escolha.upper() == 'SIM':
        opcao = exibir_menu()
        match opcao:
            case 1:
                escolha_paciente = 'SIM'
                while escolha_paciente.upper() == 'SIM':
                    opcao_paciente = exibir_submenu_pacientes()
                    match opcao_paciente:
                        case 1:
                            dados = pedir_cadastro_paciente(conn)
                            if dados: 
                                NM_PACIENTE, NR_CPF, DT_NASCIMENTO, NR_DDD, NR_TELEFONE, NM_LOGRADOURO, NR_LOGRADOURO, NM_CIDADE, SG_ESTADO = dados #separando os valores do retorno da tupla
                                cadastrar_paciente(NM_PACIENTE, NR_CPF, DT_NASCIMENTO, NR_DDD, NR_TELEFONE, NM_LOGRADOURO, NR_LOGRADOURO, NM_CIDADE, SG_ESTADO, conn)
                        case 2:
                            while True: 
                                NR_CPF = input('Cpf: ')
                                if verificar_cpf_main(NR_CPF, conn):
                                    break
                            ler_paciente(NR_CPF, conn)
                        case 3:
                            atualizacao = pedir_atualizacao_paciente(conn)
                            if atualizacao:
                                NR_CPF, NOVO_LOGRADOURO, NOVO_NUMERO, NOVA_CIDADE, NOVA_SIGLA, NOVO_DDD, NOVO_TELEFONE = atualizacao #separando os valores do retorno da tupla
                                atualizar_paciente(NR_CPF, NOVO_LOGRADOURO, NOVO_NUMERO, NOVA_CIDADE, NOVA_SIGLA, NOVO_DDD, NOVO_TELEFONE, conn)
                        case 4:
                            while True: 
                                NR_CPF = input('Cpf: ')
                                if verificar_cpf_main(NR_CPF, conn):
                                    deletar_paciente(NR_CPF, conn)
                                    break
                        case _:
                            print('Opção inválida.') 
                    escolha_paciente = input('Deseja voltar ao submenu? (sim/não): ')

            case 2:
                escolha_consulta = 'SIM'
                while escolha_consulta.upper() == 'SIM':
                    opcao_consulta = exibir_submenu_consultas()
                    match opcao_consulta:
                        case 1:
                            dados = pedir_cadastro_consulta(conn)
                            if dados: 
                                ID_PACIENTE,ID_MEDICO,DT_CONSULTA,DS_CONSULTA = dados #separando os valores do retorno da tupla
                                cadastrar_consulta(ID_PACIENTE,ID_MEDICO,DT_CONSULTA,DS_CONSULTA, conn)
                        case 2:
                            try: 
                                ID_CONSULTA = int(input('ID da consulta: '))
                                ler_consulta(ID_CONSULTA, conn)
                            except ValueError as e:
                                print(f'O Id deve ser um número" \n{e}')
                        case 3:
                            atualizacao = pedir_atualizacao_consulta(conn)
                            ID_CONSULTA, NOVO_ID_MEDICO, NOVA_DT_CONSULTA, NOVA_DS_CONSULTA = atualizacao
                            atualizar_consulta(ID_CONSULTA, NOVO_ID_MEDICO, NOVA_DT_CONSULTA, NOVA_DS_CONSULTA, conn)                    
                        case 4:
                            while True: 
                                try:
                                    ID_CONSULTA = int(input('ID da consulta: '))
                                    if id_consulta_in_banco(ID_CONSULTA, conn):
                                        deletar_consulta(ID_CONSULTA, conn)
                                        break
                                except ValueError as e:
                                    print(f'O Id deve ser um número! \n{e}')
                        case _:
                            print('Opção inválida.') 
                    escolha_consulta = input('Deseja voltar ao submenu? (sim/não): ')
               
            case 3:
                escolha_medico = 'SIM'
                while escolha_medico.upper() == 'SIM':
                    opcao_medico = exibir_submenu_medicos()
                    match opcao_medico:
                        case 1:
                            dados = pedir_cadastro_medico(conn)
                            if dados: 
                                NM_MEDICO, NR_CPF, DT_NASCIMENTO, NR_CRM, DS_ESPECIALIDADE = dados #separando os valores do retorno da tupla
                                cadastrar_medico(NM_MEDICO, NR_CPF, DT_NASCIMENTO, NR_CRM, DS_ESPECIALIDADE, conn)
                        case 2:
                            try: 
                                ID_MEDICO = int(input('ID do médico: '))
                                ler_medico(ID_MEDICO, conn)
                            except ValueError as e:
                                print(f'O Id deve ser um número" \n{e}')
                        case 3:
                            atualizacao = pedir_atualizacao_medico(conn)
                            ID_MEDICO, NOVA_DS_ESPECIALIDADE = atualizacao
                            atualizar_medico(ID_MEDICO, NOVA_DS_ESPECIALIDADE, conn)    
                        case 4:
                            while True: 
                                try:
                                    ID_MEDICO = int(input('ID do médico: '))
                                    if id_medico_in_banco(ID_MEDICO, conn):
                                        deletar_medico(ID_MEDICO, conn)
                                        break
                                except ValueError as e:
                                    print(f'O Id deve ser um número! \n{e}')
                        case _:
                            print('Opção inválida.') 
                    escolha_medico = input('Deseja voltar ao submenu? (sim/não): ')

            case 4:
                apagar(conn)

            case _:
                print('Opção inválida.') 
                escolha = input('Deseja voltar ao menu? (sim/não): ')


def main():
    """
    DESCRIÇÃO
        Função principal que comanda o programa
    PARÂMETROS
        Essa função não recebe parâmetros.
    RETORNO
        Não possui retorno
    """
    respostas_sim = ["SIM", "S", "SS", "YES", "Y", "CLARO", "COM CERTEZA", "POSITIVO", "AFIRMATIVO"]
    respostas_nao = ["NAO", "NÃO", "N", "NO", "NEGATIVO", "NUNCA", "JAMAIS"]
    
    conn = None

    while not conn:
        credenciais = pegar_credenciais()
        USER, PASS, HOST, PORT, SERVICE_NAME = credenciais
        conn = getConnection(USER, PASS, HOST, PORT, SERVICE_NAME)


    while True:
        possui_tabela = input("Você possui as tabelas (PACIENTES, MEDICOS e CONSULTAS) no seu Banco de Dados (SIM/NÃO): ").strip().upper()
        if possui_tabela in respostas_sim:
            principal(conn)
            break
        elif possui_tabela in respostas_nao:
            criar_tabela_pacientes(conn)
            criar_tabela_medicos(conn)
            criar_tabela_consultas(conn)
            principal(conn)
            break
        else:
            print('Informe (SIM) se você já possui as tabelas (PACIENTES, MEDICOS e CONSULTAS) no seu Banco de Dados as tabelas, ou (NÂO) caso você não possui as tabelas') 
    conn.close()
    print('Conexão fechada com sucesso.')
   
main()