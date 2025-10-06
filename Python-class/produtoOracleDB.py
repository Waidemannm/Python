import oracledb

def getConnection():
    try:
        conn = oracledb.connect(
            user='rm563719',
            password='111206',
            host='oracle.fiap.com.br',
            port='1521',
            service_name='orcl'
        )
        return conn
    except Exception as e:
        print(f'Erro na conexão com o banco de dados: {e}')
        return None


def verificar_tabela(conn):
    cursor = conn.cursor()
    try:
        select_table_sql = "SELECT 1 FROM PRODUTOS WHERE ROWNUM = 1"
        cursor.execute(select_table_sql)
        return True
    except oracledb.Error as e:
        print(f'Tabela PRODUTOS não encontrada ou inacessível: {e}')
        return False
    finally:
        cursor.close()


def criar_tabela(conn):
    cursor = conn.cursor()
    try:
        if not verificar_tabela(conn):
            print('*-- Criando Tabela PRODUTOS --*')
            create_table_sql = """
                CREATE TABLE PRODUTOS (
                    ID_PRODUTO NUMBER(9) NOT NULL,
                    NM_PRODUTO VARCHAR2(80) NOT NULL,
                    DS_PRODUTO VARCHAR2(100) NOT NULL,
                    NM_FORNECEDOR VARCHAR2(80) NOT NULL,
                    VL_PRECO NUMBER(8) NOT NULL,
                    CONSTRAINT PRODUTOS_PK PRIMARY KEY (ID_PRODUTO)
                )
            """
            cursor.execute(create_table_sql)
            conn.commit()
            print('Tabela criada com sucesso!')
        else:
            print('Tabela já existe no seu banco')
    except oracledb.Error as e:
        print(f'Erro ao criar tabela: {e}')
        conn.rollback()
    finally:
        cursor.close()


def inserir_produto(ID_PRODUTO, NM_PRODUTO, DS_PRODUTO, NM_FORNECEDOR, VL_PRECO):
    print('*** Inserindo um novo produto na tabela PRODUTOS ***')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO PRODUTOS (ID_PRODUTO, NM_PRODUTO, DS_PRODUTO, NM_FORNECEDOR, VL_PRECO)
            VALUES (:ID_PRODUTO, :NM_PRODUTO, :DS_PRODUTO, :NM_FORNECEDOR, :VL_PRECO)
        """
        cursor.execute(sql, {
            'ID_PRODUTO': ID_PRODUTO,
            'NM_PRODUTO': NM_PRODUTO,
            'DS_PRODUTO': DS_PRODUTO,
            'NM_FORNECEDOR': NM_FORNECEDOR,
            'VL_PRECO': VL_PRECO
        })
        conn.commit()
        print(f'Produto {NM_PRODUTO} adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'\nErro ao inserir produto: {e}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def listar_produtos():
    print('*** Listando todos os produtos ***')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM PRODUTOS ORDER BY ID_PRODUTO"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\n --- Lista de Produtos ---")
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: {row[4]}')
            print('----------------------------------')
    except oracledb.Error as e:
        print(f'\nErro ao listar produtos: {e}')
    finally:
        cursor.close()
        conn.close()


def buscar_produto_por_id(ID_PRODUTO):
    print(f'*** Buscando produto com id: {ID_PRODUTO} ***')
    conn = getConnection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM PRODUTOS WHERE ID_PRODUTO = :ID_PRODUTO"
        cursor.execute(sql, {'ID_PRODUTO': ID_PRODUTO})
        row = cursor.fetchone()
        if row:
            print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: {row[4]}')
        else:
            print(f'Nenhum produto com id {ID_PRODUTO} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao buscar produto: {e}')
    finally:
        cursor.close()
        conn.close()


def atualizar_preco_produto(ID_PRODUTO, novo_preco):
    print(f'*** Atualizando preço do produto com id: {ID_PRODUTO} ***')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "UPDATE PRODUTOS SET VL_PRECO = :novo_preco WHERE ID_PRODUTO = :ID_PRODUTO"
        cursor.execute(sql, {'novo_preco': novo_preco, 'ID_PRODUTO': ID_PRODUTO})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Preço do produto com ID {ID_PRODUTO} foi atualizado!')
        else:
            print(f'Nenhum produto com ID {ID_PRODUTO} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao atualizar preço: {e}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def deletar_produto(ID_PRODUTO):
    print(f'*** Excluindo produto com id: {ID_PRODUTO} ***')
    conn = getConnection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM PRODUTOS WHERE ID_PRODUTO = :ID_PRODUTO"
        cursor.execute(sql, {'ID_PRODUTO': ID_PRODUTO})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Produto com ID {ID_PRODUTO} foi excluído com sucesso!')
        else:
            print(f'Nenhum produto com id {ID_PRODUTO} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao excluir produto: {e}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def main():
    print('*** MENU PRINCIPAL ***')
    print('----------------------')

    tabela = input('Você precisa criar a tabela PRODUTOS no seu Banco de Dados? (sim/não): ').strip().upper()
    if tabela == 'SIM':
        conn = getConnection()
        if conn:
            criar_tabela(conn)

    escolha = 'SIM'
    while escolha == 'SIM':
        print(f'\n --- Menu CRUD - PRODUTO ---')
        print('1. Inserir um novo produto')
        print('2. Listar todos os produtos')
        print('3. Buscar produto por ID')
        print('4. Atualizar preço de um produto')
        print('5. Excluir um produto')
        print('6. Sair')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Por favor, digite um número válido.')
            continue

        if opcao == 1:
            try:
                ID_PRODUTO = int(input('Insira um ID para o produto: '))
                NM_PRODUTO = input('Nome do produto: ').strip()
                DS_PRODUTO = input('Descrição do produto: ').strip()
                NM_FORNECEDOR = input('Fornecedor: ').strip()
                VL_PRECO = float(input('Preço: '))
                inserir_produto(ID_PRODUTO, NM_PRODUTO, DS_PRODUTO, NM_FORNECEDOR, VL_PRECO)
            except ValueError:
                print('Entrada inválida. Tente novamente.')
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            try:
                ID_PRODUTO = int(input('Digite o ID do produto para buscar: '))
                buscar_produto_por_id(ID_PRODUTO)
            except ValueError:
                print('ID inválido.')
        elif opcao == 4:
            listar_produtos()
            try:
                ID_PRODUTO = int(input('Digite o ID do produto para atualizar: '))
                novo_preco = float(input('Digite o novo preço: '))
                atualizar_preco_produto(ID_PRODUTO, novo_preco)
            except ValueError:
                print('Entrada inválida.')
        elif opcao == 5:
            listar_produtos()
            try:
                ID_PRODUTO = int(input('Digite o ID do produto para exclusão: '))
                deletar_produto(ID_PRODUTO)
            except ValueError:
                print('ID inválido.')
        elif opcao == 6:
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente!')
        escolha = input('Deseja voltar ao menu? (sim/não): ').strip().upper()

main()
