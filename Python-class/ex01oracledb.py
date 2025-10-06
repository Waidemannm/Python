
'''
CRUD = Create, Read, Update, Delete
  -Operações de manipulação de dados em memória ou em banco de dados

oracledb
  -Biblioteca que faz a conexão do códgo python com o banco de dados

Strign de conexao(oracle)(Muda de banco para banco, sempre pesquisar) = credenciais para fazer conexão com o banco de dados
  - <user>/<pass>@<db_host_address>:<db_port>/<db_servce>
  connection = 'usuario/pass@localhost:1521/orcl'

Criar Tabela CEO_DETAILS(NM_PRIMEIRO VARCHAR2(40) NM_SEGUNDO VARCHAR2(40) DS_EMAIL VARCHAR2(60) NM_EMPRESA VARCHAR2(60) NR_IDADE NUMBER(3)

Cursor objeto  utilizado para executar comando SQL no código py
'''
import oracledb

def getConnection():
  try:
    conn = oracledb.connect(user = 'rm563719', password = '111206', host ='oracle.fiap.com.br', port='1521', service_name ='orcl')
  except Exception as e:
    print(f'Erro na conexão com o banco de dados: {e}')
  return conn

def criar_tabela(conn):
  #Obtendo objeto cursor
  cursor = conn.cursor()
  try:
    #criando table pelo py, mas é igual criar no developer
    create_table_sql = '''
    CREATE TABLE CEO_DETAILS(
      ID_CEO NUMBER GENERATED ALWAYS AS IDENTITY,
      NM_PRIMEIRO VARCHAR2(40) NOT NULL,
      NM_SEGUNDO VARCHAR2(40) NOT NULL,
      DS_EMAIL VARCHAR2(60) NOT NULL,
      NM_EMPRESA VARCHAR2(60) NOT NULL,
      NR_IDADE NUMBER(3) NOT NULL,
      PRIMARY KEY (ID_CEO)
    )'''

    cursor.execute(create_table_sql)

    print('Tabela criada com sucesso!')

  except oracledb.Error as e:
    print(f'Erro de conexão: {e}')

#Operações CRUD
#Create (insert)
def create_ceo(NM_PRIMEIRO, NM_SEGUNDO, DS_EMAIL, NM_EMPRESA, NR_IDADE): 
  print('** Inserindo um novo CEO na tabela CEO_DETAILS **') 
  conn = getConnection() #validação da conexão 
  if not conn: 
    print('Erro na conexão com o banco de dados') 
    return #retorna null 
  try: 
    cursor = conn.cursor() 
    insert_sql = """ 
    INSERT INTO CEO_DETAILS (NM_PRIMEIRO, NM_SEGUNDO, DS_EMAIL, NM_EMPRESA, NR_IDADE) 
    VALUES (:NM_PRIMEIRO, :NM_SEGUNDO, :DS_EMAIL, :NM_EMPRESA, :NR_IDADE)"""
    cursor.execute(insert_sql, {
        'NM_PRIMEIRO' : NM_PRIMEIRO,
        'NM_SEGUNDO' : NM_SEGUNDO,
        'DS_EMAIL' : DS_EMAIL,
        'NM_EMPRESA' : NM_EMPRESA,
        'NR_IDADE' : NR_IDADE
    })
    conn.commit() #salva o registro
    print(f'CEO {NM_PRIMEIRO} {NM_SEGUNDO} foi registrado com ucesso!')
  except oracledb.Error as e:
    print(f'Erro ao inserir CEO: {e}')
    conn.rollback() #volta para o estado de segurança, do ultimo commit
  finally:
    if (conn):
      conn.close()
      print('Conexão fechada com sucesso.')

#Read (select)
def read_ceos():
   print('** Lendo e exibindo todos os CEOs da tabela CEO_DETAILS **') 
   conn = getConnection() #validação da conexão 
   if not conn: 
    print('Erro na conexão com o banco de dados') 
    return #retorna null 
   try: 
     cursor = conn.cursor() 
     select_sql = """
        SELECT * FROM CEO_DETAILS ORDER BY NM_PRIMEIRO 
     """
     cursor.execute(select_sql)
     print(f'\n --- Lista de CEOs ---')
     rows = cursor.fetchall()
     for row in rows:
       print(f'ID: {row[0]} \n Nome: {row[1]} {row[2]} \n Email: {row[3]} \n Empresa: {row[4]} \n Idade: {row[5]}')
       print('----------------------------------------------------------------------------------------------------')
   except oracledb.Error as e:
     print(f'Erro ao ler e exibir registros de CEOs: {e}')
     conn.rollback()
   finally:
     if (conn):
       conn.close()
       print('Conexão fechada com sucesso.')

#Update (update)
def update_ceo(ID_CEO, NOVA_IDADE):
   print('** Atualizando registro **') 
   conn = getConnection() #validação da conexão 
   if not conn: 
      print('Erro na conexão com o banco de dados') 
      return #retorna null 
   try: 
      cursor = conn.cursor() 
      update_sql = """
         UPDATE CEO_DETAILS SET NR_IDADE = :NOVA_IDADE WHERE ID_CEO = :ID_CEO
      """
      cursor.execute(update_sql, {'NOVA_IDADE' : NOVA_IDADE, 
                                  'ID_CEO' : ID_CEO})
      conn.commit() #salva o registro
      if (cursor.rowcount > 0):  
        print(f'Idade do CEO com ID {ID_CEO} foi atualizada com sucesso!')
      else:
        print(f'Nenhum CEO com ID {ID_CEO} foi encontrado!')
   except oracledb.Error as e:
      print(f'Erro ao ler e exibir registros de CEOs: {e}')
      conn.rollback()
   finally:
      if (conn):
        conn.close()
        print('Conexão fechada com sucesso.')


#Delete (delete)
def delete_ceo(ID_CEO):
  print(f'** Excluindo CEO com id {ID_CEO} **') 
  conn = getConnection()
  if not conn:
    return 
  try:
    cursor = conn.cursor()
    delete_sql = """
      DELETE FROM CEO_DETAILS WHERE ID_CEO = :ID_CEO
    """
    cursor.execute(delete_sql, {'ID_CEO': ID_CEO} )
    conn.commit()
    if(cursor.rowcount > 0):
      print(f'O CEO com ID: {ID_CEO} foi excluído com sucesso!')
    else:
      print(f'Não foi possível encontrar um CEO com ID: {ID_CEO}!')
  except oracledb.Erros as e:
    print(f'Erro ao exluir CEO com ID: {ID_CEO}: {e}')
    conn.rollback()
  finally:
    conn.close()
    print('Conxão fechada com sucesso!')

def main():
    print('*** MENU PRINCIPAL ***')
    print('----------------------')

    while True:
        print(f'\n --- Menu CRUD - CEO Details ---')
        print('1. Inserir um novo CEO')
        print('2. Listar todos os CEOs')
        print('3. Atualizar a idade de um CEO')
        print('4. Excluir um CEO')
        print('5. Sair')

        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            NM_PRIMEIRO = input('Primeiro nome: ')
            NM_SEGUNDO = input('Último nome: ')
            NM_EMPRESA = input('Empresa: ')
            DS_EMAIL = input('Digite o email: ')
            NR_IDADE = int(input('Idade: '))
            create_ceo(NM_PRIMEIRO, NM_SEGUNDO, DS_EMAIL, NM_EMPRESA, NR_IDADE)
        elif opcao == 2:
            read_ceos()
        elif opcao == 3:
            read_ceos()
            ID_CEO =int(input('Digite o ID do CEO para atualizar: '))
            NOVA_IDADE = int(input('Digite a nova idade: '))
            update_ceo(ID_CEO, NOVA_IDADE)
        elif opcao == 4:
            read_ceos()
            ID_CEO = int(input('Digite o ID do CEO para exclusão: '))
            delete_ceo(ID_CEO)   
        elif opcao == 5:
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente!')
#programa principal
conn = getConnection() #Testando conexão
print(f'Conexão: {conn.version}')
main()