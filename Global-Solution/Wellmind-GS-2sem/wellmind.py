"""
Gerenciamento de usuario, feedback, habito e resposta_usuario (CRUD)

Link deploy da API wellmind em Java https://wellmind-caqg.onrender.com
API usada para fazer o CRUD com o banco de dados

... (comentário de topo preservado)
"""

import requests
import os
import json

respostas_sim = ["SIM", "S", "SS", "YES", "Y", "CLARO", "COM CERTEZA", "POSITIVO", "AFIRMATIVO"]
respostas_nao = ["NAO", "NÃO", "N", "NO", "NEGATIVO", "NUNCA", "JAMAIS"]

###---Parte do CRUD de usuario---###

def verificar_nome(nome):
    if(len(nome) > 0):
        return True
    else:
        print('O nome não pode ser vazio')
        return False 
    
def verificar_idade(idade):
    if(idade <= 0):
        print('Idade inválida. A idade deve ser um número inteiro positivo.')
        return False
    else:
        return True
    
def verificar_genero(genero):
    generos = ['MASCULINO', 'FEMININO', 'OUTROS']
    if(generos.count(genero.strip().upper()) > 0):
        return True
    else:
        print('Gênero inválido. Os gêneros válidos são: Masculino, Feminino, Outro.')
        return False

def id_usuario_in_banco(id_usuario, api):
    try:
        resposta = requests.get(f"{api}/usuario/{id_usuario}")
        if resposta.status_code == 200:
            return True
        else:
            # não exibe stack trace aqui — apenas informa ao usuário
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False    

def verificar_email(email):
    if ("@" in email and ".com" in email):
        return True
    else:
        print('Email inválido. O email deve conter "@" e ".".')
        return False
    
def email_in_banco(email, api):
    try:
        usuarios = requests.get(f"{api}/usuario")
        if usuarios.status_code == 200:
            lista_usuarios = usuarios.json()
            for usuario in lista_usuarios:
                # compara pelo campo 'email' (como seu payload)
                if 'email' in usuario and usuario['email'].strip().upper() == email.strip().upper():
                    return True
            return False    
        else:
            return False    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False    

def pedir_cadastro_usuario(api):
    try:
        while True:
            email = input("Digite o email do usuário: ")
            if verificar_email(email) and not email_in_banco(email, api):
                break
            else:
                # se email já existe ou inválido, repete
                continue

        while True:
            nome = input("Digite o nome do usuário: ")
            if verificar_nome(nome):
                break

        while True:
            try:
                idade = int(input("Digite a idade do usuário: "))
                if verificar_idade(idade):
                    break
            except ValueError:
                print("Digite um número válido para a idade.")

        while True:
            genero = input("Digite o gênero do usuário (Masculino, Feminino, Outro): ")
            if verificar_genero(genero):
                break

        return email, nome, idade, genero
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def cadastrar_usuario(email, nome, idade, genero, api):
    print("Cadastrando usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return 
        url = f"{api}/usuario"
        string_sql = {
            "email" : email,
            "nome": nome,
            "idade": idade,
            "genero": genero
        }
        response = requests.post(url, json=string_sql)
        if response.status_code == 201:
            print(f'[SUCESSO] Usuário {nome} cadastrado com sucesso.')
        else:   
            print(f'[ERRO] Não é possível cadastrar esse usuário. Código: {response.status_code}, Mensagem: {response.text}')
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao cadastrar o usuário: {e}')

def ler_usuario(id_usuario, api):
    print("Lendo usuário...")
    if not id_usuario_in_banco(id_usuario, api):
        print(f'[ERRO] Usuário com ID {id_usuario} não encontrado.')
        return None
    try:
        if not api:
            print("API não está disponível.")
            return None
        url = f'{api}/usuario/{id_usuario}'
        response = requests.get(url)
        if response.status_code == 200:
            usuario = response.json()
            # usa as chaves esperadas pelo seu backend (camelCase)
            print("Dados do usuário:")
            print(f'ID Usuário: {usuario.get("idUsuario")}\nEmail: {usuario.get("email")}\nNome: {usuario.get("nome")}\nIdade: {usuario.get("idade")}\nGênero: {usuario.get("genero")}')
            return usuario.get("idUsuario"), usuario.get("email"), usuario.get("nome"), usuario.get("idade"), usuario.get("genero")
        else:
            print(f'[ERRO] Não foi possível encontrar o usuário. Código: {response.status_code}')
            return None
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao ler o usuário: {e}')
        return None
        
def pedir_atualizacao_usuario(api):
    try:
        while True:
            id_usuario = input("Digite o ID do usuário: ")
            if id_usuario_in_banco(id_usuario, api):
                break
        
        while True:
            email = input("Digite o email do usuário: ")
            if verificar_email(email) and not email_in_banco(email, api):
                break

        while True:
            nome = input("Digite o nome do usuário: ")
            if verificar_nome(nome):
                break

        while True:
            try:
                idade = int(input("Digite a idade do usuário: "))
                if verificar_idade(idade):
                    break
            except ValueError:
                print("Digite um número válido para a idade.")

        while True:
            genero = input("Digite o gênero do usuário (Masculino, Feminino, Outro): ")
            if verificar_genero(genero):
                break

        return id_usuario, email, nome, idade, genero
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def atualizar_usuario(id_usuario, email, nome, idade, genero, api):
    print("Atualizando usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/usuario/{id_usuario}'
        string_sql = {
                "email" : email,
                "nome": nome,
                "idade": idade,
                "genero": genero
            }
        response = requests.put(url, json=string_sql)
        # aceita 201 se seu backend usar Response.created em update; caso contrário pode retornar 200/204
        if response.status_code in (200, 201, 204):
            print(f"[SUCESSO] Usuário com ID {id_usuario} atualizado com sucesso.")
        else:
            print(f"[ERRO] Não é possível atualizar esse usuário. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao atualizar o usuário: {e}')

def deletar_usuario(id_usuario, api):
    print("Deletando usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/usuario/{id_usuario}'
        response = requests.delete(url)
        if response.status_code == 204:
            print(f"[SUCESSO] Usuário com ID {id_usuario} deletado com sucesso.")
        else:
            print(f"[ERRO] Não é possível deletar esse usuário. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao deletar o usuário: {e}')
###---Fim da parte do CRUD de usuario---###


###---Parte do CRUD de feedback---###
def id_feedback_in_banco(id_feedback, api):
    try:
        resposta = requests.get(f"{api}/feedback/{id_feedback}")
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False    

def verificar_mensagem(mensagem):
    if(len(mensagem) > 0 and len(mensagem) <= 1000):
        return True
    else:
        print('A mensagem não pode ser vazia')
        return False

def pedir_cadastro_feedback(api):
    try:
        while True:
            id_usuario = input("Digite o ID do usuário: ")
            if id_usuario_in_banco(id_usuario, api):
                break

        while True:
            mensagem = input("Digite a mensagem do feedback: ")
            if verificar_mensagem(mensagem):
                break

        return id_usuario, mensagem
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def cadastrar_feedback(id_usuario, mensagem, api):
    print("Cadastrando feedback...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/feedback'
        string_sql = {
                "idUsuario": id_usuario,
                "mensagem": mensagem
            }
        response = requests.post(url, json=string_sql)
        if response.status_code == 201:
            print(f"[SUCESSO] Feedback cadastrado com sucesso.")
        else:
            print(f"[ERRO] Não é possível cadastrar esse feedback. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao cadastrar o feedback: {e}')

def ler_feedback(id_feedback, api):
    if not id_feedback_in_banco(id_feedback, api):
        print(f'[ERRO] Feedback com ID {id_feedback} não encontrado.')
        return None
    print("Lendo feedback...")
    try:
        if not api:
            print("API não está disponível.")
            return None
        url = f'{api}/feedback/{id_feedback}'
        response = requests.get(url)
        if response.status_code == 200:
            feedback = response.json()
            print("Dados do feedback:")
            print(f'ID Feedback: {feedback.get("idFeedback")}\nID Usuário: {feedback.get("idUsuario")}\nMensagem: {feedback.get("mensagem")}')
            return feedback.get("idFeedback"), feedback.get("idUsuario"), feedback.get("mensagem")
        else:
            print(f'[ERRO] Não possível encontrar o feedback. Código: {response.status_code}')
            return None
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao ler o feedback: {e}')
        return None

def pedir_atualizacao_feedback(api):
    try:
        while True:
            id_feedback = input("Digite o ID do feedback: ")
            if id_feedback_in_banco(id_feedback, api):
                break
        
        while True:
            id_usuario = input("Digite o ID do usuário: ")
            if id_usuario_in_banco(id_usuario, api):
                break

        while True:
            mensagem = input("Digite a mensagem do feedback: ")
            if verificar_mensagem(mensagem):
                break

        return id_feedback, id_usuario, id_resposta, mensagem
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def atualizar_feedback(id_feedback, id_usuario, id_resposta, mensagem, api):
    print("Atualizando feedback...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/feedback/{id_feedback}'
        string_sql = {
                "idUsuario": id_usuario,
                "mensagem": mensagem
            }
        response = requests.put(url, json=string_sql)
        if response.status_code in (200, 201, 204):
            print(f"[SUCESSO] Feedback com ID {id_feedback} atualizado com sucesso.")  
        else:
            print(f"[ERRO] Não é possível atualizar esse feedback. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao atualizar o feedback: {e}')

def deletar_feedback(id_feedback, api):
    print("Deletando feedback...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/feedback/{id_feedback}'
        response = requests.delete(url)
        if response.status_code == 204:
            print(f"[SUCESSO] Feedback com ID {id_feedback} deletado com sucesso.")
        else:
            print(f"[ERRO] Não é possível deletar esse feedback. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao deletar o feedback: {e}')
###---Fim da parte do CRUD de feedback---###


###---Parte do CRUD de habito---###
def id_habito_in_banco(id_habito, api):
    try:
        resposta = requests.get(f"{api}/habito/{id_habito}")
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False
    
def verificar_tipo(tipo):
    tipos_validos = ['ESTRESSE E FOCO', 'HIDRATAÇÃO', 'HUMOR E ENERGIA', 'ALIMENTAÇÃO', 'OBSERVAÇÕES', 'SONO', 'ALIMENTAÇAO', 'OBSERVAÇOES', 'ALIMENTACAO', 'OBSERVACOES']
    if(tipos_validos.count(tipo.strip().upper()) > 0):
        return True
    else:
        print('Tipo inválido. Os tipos válidos são: ESTRESSE E FOCO, HIDRATAÇÃO, HUMOR E ENERGIA, ALIMENTAÇÂO, OBSERVAÇÕES, SONO.')
        return False

def verificar_descricao(descricao):
    if(len(descricao) > 0 and len(descricao) <= 200):
        return True
    else:
        print('Descrição inválida. A descrição deve ter no máximo 200 caracteres.')
        return False

def verificar_unidade(unidade):
    unidades_validas = ['ESCALA', 'HORAS', 'REFEIÇÕES', 'TEXTO LIVRE', 'LITROS']
    if(unidades_validas.count(unidade.strip().upper()) > 0):
        return True
    else:
        print('Unidade inválida. As unidades válidas são: Escala, Horas, Refeições, Texto Livre, Litros.')
        return False

def nome_tipo_in_habito(tipo, api):
    try:
        habitos = requests.get(f"{api}/habito")
        if habitos.status_code == 200:
            lista_habitos = habitos.json()
            for habito in lista_habitos:
                # se existe, retorna True
                if 'tipo' in habito and habito['tipo'].strip().upper() == tipo.strip().upper():
                    print(f'O hábito do tipo {tipo} já existe no banco de dados.')
                    return True
            return False    
        else:
            return False    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False
    
def pedir_cadastro_habito(api):
    try:
        while True:
            tipo = input("Digite o tipo do hábito (Estresse e Foco, Hidratação, Humor e Energia, Alimentação, Observações, Sono): ")
            if verificar_tipo(tipo) and not nome_tipo_in_habito(tipo, api):
                break

        while True:
            descricao = input("Digite a descrição do hábito: ")
            if verificar_descricao(descricao):
                break

        while True: 
            unidade = input("Digite a unidade do hábito (Escala, Horas, Refeições, Texto Livre, Litros): ")
            if verificar_unidade(unidade):
                break

        return tipo, descricao, unidade
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def cadastrar_habito(tipo, descricao, unidade ,api):
    print("Cadastrando hábito...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/habito'
        string_sql = {
                "tipo": tipo,
                "descricao": descricao,
                "unidade": unidade
                }
        response = requests.post(url, json=string_sql)
        if response.status_code == 201:
            print(f"[SUCESSO] Hábito {tipo} cadastrado com sucesso.")
        else:
            print(f"[ERRO] Não é possível cadastrar esse hábito. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao cadastrar o hábito: {e}')

def ler_habito(id_habito, api):
    if not id_habito_in_banco(id_habito, api):
        print(f'[ERRO] Hábito com ID {id_habito} não encontrado.')
        return None
    print("Lendo hábito...")
    try:
        if not api:
            print("API não está disponível.")
            return None
        url = f'{api}/habito/{id_habito}'
        response = requests.get(url)
        if response.status_code == 200:
            habito = response.json()
            print("Dados do hábito:")
            print(f'ID Hábito: {habito.get("idHabito")}\nTipo: {habito.get("tipo")}\nDescrição: {habito.get("descricao")}\nUnidade: {habito.get("unidade")}')
            return habito.get("idHabito"), habito.get("tipo"), habito.get("descricao"), habito.get("unidade")
        else:
            print(f'[ERRO] Não possível encontrar o hábito. Código: {response.status_code}')
            return None
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao ler o hábito: {e}')
        return None

def pedir_atualizacao_habito(api):
    try:
        while True:
            id_habito = input("Digite o ID do hábito: ")
            if id_habito_in_banco(id_habito, api):
                break
        
        while True:
            tipo = input("Digite o tipo do hábito (Estresse e Foco, Hidratação, Humor e Energia, Alimentação Observações, Sono): ")
            if verificar_tipo(tipo): 
                break

        while True:
            descricao = input("Digite a descrição do hábito: ")
            if verificar_descricao(descricao):
                break

        while True: 
            unidade = input("Digite a unidade do hábito (Escala, Horas, Refeições, Texto Livre, Litros): ")
            if verificar_unidade(unidade):
                break

        return id_habito, tipo, descricao, unidade
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def atualizar_habito(id_habito, tipo, descricao, unidade, api):
    print("Atualizando hábito...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/habito/{id_habito}'
        string_sql = {
                "tipo": tipo,
                "descricao": descricao,
                "unidade": unidade
            }
        response = requests.put(url, json=string_sql)
        # aceita 201 (se seu Java retornar 201 no update), 200 ou 204
        if response.status_code in (200, 201, 204):
            print(f"[SUCESSO] Hábito com ID {id_habito} atualizado com sucesso.")
        else:
            print(f"[ERRO] Não é possível atualizar esse hábito. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao atualizar o habito: {e}')

def deletar_habito(id_habito, api): 
    print("Deletando hábito...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/habito/{id_habito}'
        response = requests.delete(url)
        if response.status_code == 204:
            print(f"[SUCESSO] Hábito com ID {id_habito} deletado com sucesso.")
        else:
            print(f"[ERRO] Não é possível deletar esse hábito. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao deletar o habito: {e}')
###---Fim da parte do CRUD de habito---###


###---Parte do CRUD de resposta_usuario---###
def id_resposta_in_banco(id_resposta, api):
    try:
        resposta = requests.get(f"{api}/resposta_usuario/{id_resposta}")
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False
    
def verificar_resposta_escala_1_a_5(resposta):
    if(resposta >= 1 and resposta <= 5):
        return True
    else:
        print('Resposta inválida. A resposta deve estar entre 1 e 5.')
        return False
    
def verificar_resposta_escala_1_a_10(resposta):
    if(resposta >= 1 and resposta <= 10):
        return True
    else:
        print('Resposta inválida. A resposta deve estar entre 1 e 10.')
        return False
    
def verificar_observacoes(observacoes):   
    if(len(observacoes) <= 500):
        return True
    else:
        print('Observações inválidas. As observações devem ter no máximo 500 caracteres.')
        return False

def pedir_cadastro_resposta_usuario(api):
    try:
        while True:
            id_usuario = input("Digite o ID do usuário: ")
            if id_usuario_in_banco(id_usuario, api):
                break
        while True:
            id_habito = input("Digite o ID do hábito: ")
            if id_habito_in_banco(id_habito, api):
                break
        while True: 
            try:
                resposta = int(input("Digite a resposta (1-5 ou 1-10 dependendo do hábito): "))
                if verificar_resposta_escala_1_a_5(resposta) or verificar_resposta_escala_1_a_10(resposta):
                    break
            except ValueError:
                print("Digite um número válido para a resposta.")
        while True:
            observacoes = input("Digite as observações (máximo 500 caracteres): ")
            if verificar_observacoes(observacoes):
                break
        return id_usuario, id_habito, resposta, observacoes
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def cadastrar_resposta_usuario(id_usuario, id_habito, resposta, obervacoes, api):
    print("Cadastrando resposta do usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/resposta_usuario'
        string_sql = {
                "idUsuario": id_usuario,
                "idHabito": id_habito,
                "resposta": resposta,
                "observacoes": obervacoes
            }
        response = requests.post(url, json=string_sql)
        if response.status_code == 201:
            print(f'[SUCESSO] Resposta do usuário cadastrada com sucesso.')
        else:
            print(f'[ERRO] Não é possível cadastrar essa resposta do usuário. Código: {response.status_code}, Mensagem: {response.text}')
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao cadastrar a resposta do usuário: {e}')

def ler_resposta_usuario(id_resposta_usuario, api):
    if not id_resposta_in_banco(id_resposta_usuario, api):
        print(f'[ERRO] Resposta do usuário com ID {id_resposta_usuario} não encontrada.')
        return None
    print("Lendo resposta do usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return None
        url = f'{api}/resposta_usuario/{id_resposta_usuario}'
        response = requests.get(url)
        if response.status_code == 200:
            resposta_usuario = response.json()
            print("Dados da resposta do usuário:")
            print(f'ID Resposta: {resposta_usuario.get("idResposta")}\nID Usuário: {resposta_usuario.get("idUsuario")}\nID Hábito: {resposta_usuario.get("idHabito")}\nResposta: {resposta_usuario.get("resposta")}\nObservações: {resposta_usuario.get("observacoes")}')
            return resposta_usuario.get("idResposta"), resposta_usuario.get("idUsuario"), resposta_usuario.get("idHabito"), resposta_usuario.get("resposta"), resposta_usuario.get("observacoes")
        else:
            print(f'[ERRO] Não possível encontrar a resposta do usuário. Código: {response.status_code}')
            return None
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao ler a resposta do usuário: {e}')
        return None

def pedir_atualizacao_resposta_usuario(api):
    try:
        while True:
            id_resposta = input("Digite o ID da resposta do usuário: ")
            if id_resposta_in_banco(id_resposta, api):
                break
        while True:
            id_usuario = input("Digite o ID do usuário: ")
            if id_usuario_in_banco(id_usuario, api):
                break
        while True:
            id_habito = input("Digite o ID do hábito: ")
            if id_habito_in_banco(id_habito, api):
                break
        while True: 
            try:
                resposta = int(input("Digite a resposta (1-5 ou 1-10 dependendo do hábito): "))
                if verificar_resposta_escala_1_a_5(resposta) or verificar_resposta_escala_1_a_10(resposta):
                    break
            except ValueError:
                print("Digite um número válido para a resposta.")
        while True:
            observacoes = input("Digite as observações (máximo 500 caracteres): ")
            if verificar_observacoes(observacoes):
                break
        return id_resposta, id_usuario, id_habito, resposta, observacoes
    except Exception:
        print("Entrada inválida. Certifique-se de inserir os dados corretamente.")
        return None

def atualizar_resposta_usuario(id_resposta, id_usuario, id_habito, resposta, obervacoes, api):
    print("Atualizando resposta do usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/resposta_usuario/{id_resposta}'
        string_sql = {
                "idUsuario": id_usuario,
                "idHabito": id_habito,
                "resposta": resposta,
                "observacoes": obervacoes
            }
        response = requests.put(url, json=string_sql)
        if response.status_code in (200, 201, 204):
            print(f"[SUCESSO] Resposta do usuário com ID {id_resposta} atualizado com sucesso.")
        else:
            print(f"[ERRO] Não é possível atualizar essa resposta do usuário. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao atualizar a respota de usuário: {e}')

def deletar_resposta_usuario(id_resposta, api):
    print("Deletando resposta do usuário...")
    try:
        if not api:
            print("API não está disponível.")
            return
        url = f'{api}/resposta_usuario/{id_resposta}'
        response = requests.delete(url)
        if response.status_code == 204:
            print(f"[SUCESSO] Resposta do usuário com ID {id_resposta} deletado com sucesso.")
        else:
            print(f"[ERRO] Não é possível deletar essa resposta do usuário. Código: {response.status_code}, Mensagem: {response.text}")
    except requests.RequestException as e:
        print(f'[ERRO] Falha ao deletar a resposta de usuário: {e}')
###---Fim da parte do CRUD de resposta_usuario---###


###---Parte de salvamento de arquivos JSON---###
def deseja_salvar_json():
    resposta = input("Deseja salvar os dados em um arquivo JSON? (sim/não): ")
    if respostas_sim.count(resposta.strip().upper()) > 0:
        return True 
    else:
        return False
    
def salvar_json_usuario(id_usuario, email, nome, idade, genero):
    nm_arquivo = f"usuario_{id_usuario}.json"
    medico = {
        "id_usuario": id_usuario,
        "nm_email": email,
        "nm_usuario": nome,
        "nr_idade": idade,
        "nm_genero": genero
    }
    try:
        pasta = "./" 
        os.makedirs(pasta, exist_ok=True)
        arquivo = os.path.join(pasta, nm_arquivo)
        with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(medico, arquivo_json, ensure_ascii=False, indent=4, default=str)
        print(f'\n[SUCESSO] Dados escritos com sucesso no {nm_arquivo}')
    except Exception as e:
        print(f'\n[Erro] Ocorreu um erro ao escrever no arquivo: {e}')

def salvar_json_resposta_usuario(id_resposta, id_usuario, id_habito, resposta, obervacoes):
    nm_arquivo = f"resposta_usuario_{id_resposta}.json"
    medico = {
        "id_resposta": id_resposta,
        "id_usuario": id_usuario,
        "id_habito": id_habito,
        "vl_resposta": resposta,
        "ds_observacoes": obervacoes
    }
    try:
        pasta = "./" 
        os.makedirs(pasta, exist_ok=True)
        arquivo = os.path.join(pasta, nm_arquivo)
        with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(medico, arquivo_json, ensure_ascii=False, indent=4, default=str)
        print(f'\n[SUCESSO] Dados escritos com sucesso no {nm_arquivo}')
    except Exception as e:
        print(f'\n[Erro] Ocorreu um erro ao escrever no arquivo: {e}')

def salvar_json_habito(id_habito, tipo, descricao, unidade):
    nm_arquivo = f"habito_{id_habito}.json"
    medico = {
        "id_habito": id_habito,
        "nm_tipo": tipo,
        "ds_habito": descricao,
        "vl_unidade": unidade,
    }
    try:
        pasta = "./" 
        os.makedirs(pasta, exist_ok=True)
        arquivo = os.path.join(pasta, nm_arquivo)
        with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(medico, arquivo_json, ensure_ascii=False, indent=4, default=str)
        print(f'\n[SUCESSO] Dados escritos com sucesso no {nm_arquivo}')
    except Exception as e:
        print(f'\n[Erro] Ocorreu um erro ao escrever no arquivo: {e}')

def salvar_json_feedback(id_feedback, id_usuario, id_resposta, mensagem):
    nm_arquivo = f"feedback_{id_feedback}.json"
    medico = {
        "id_feedback": id_feedback,
        "id_usuario": id_usuario,
        "ds_mensagem": mensagem,
    }
    try:
        pasta = "./" 
        os.makedirs(pasta, exist_ok=True)
        arquivo = os.path.join(pasta, nm_arquivo)
        with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(medico, arquivo_json, ensure_ascii=False, indent=4, default=str)
        print(f'\n[SUCESSO] Dados escritos com sucesso no {nm_arquivo}')
    except Exception as e:
        print(f'\n[Erro] Ocorreu um erro ao escrever no arquivo: {e}')
###---Fim da parte de salvamento de arquivos JSON---###


###---Parte dos menus---###
def exibir_menu():
    print('*-- WellMind - Bem estar Inteligente --*')
    print('------------------------------')
    print('Seja bem vindo(a) ao WellMind')
    try:
        opcao = int(input('Selecione a opção desejada \n(1) Usuário \n(2) Feedback \n(3) Hábito \n(4) Resposta Usuário \nOpção: '))
        return opcao
    except ValueError:
        print('Você deve inserir um número entre (1 e 4).')
        return -1

def exibir_submenu_usuario():
    print('\n-- Menu Usuário --')
    try:
        opcao_usuario = int(input('Selecione a opção desejada \n(1) Cadastrar Usuário \n(2) Ler Usuário \n(3) Atualizar Usuário \n(4) Deletar Usuário \nOpção: '))
        return opcao_usuario
    except ValueError:
        print('Você deve inserir um número entre (1 e 4).')
        return -1

def exibir_submenu_feedback():
    print('\n-- Menu Feedback --')
    try:
        opcao_feedback = int(input('Selecione a opção desejada \n(1) Cadastrar Feedback \n(2) Ler Feedback \n(3) Atualizar Feedback \n(4) Deletar Feedback \nOpção: '))
        return opcao_feedback
    except ValueError:
        print('Você deve inserir um número entre (1 e 4).')
        return -1

def exibir_submenu_habito():
    print('\n-- Menu Hábito --')
    try:
        opcao_habito = int(input('Selecione a opção desejada \n(1) Cadastrar Hábito \n(2) Ler Hábito \n(3) Atualizar Hábito \n(4) Deletar Hábito \nOpção: '))
        return opcao_habito
    except ValueError:
        print('Você deve inserir um número entre (1 e 4).')
        return -1

def exibir_submenu_resposta_usuario():
    print('\n-- Menu Resposta Usuário --')
    try:
        opcao_resposta_usuario = int(input('Selecione a opção desejada \n(1) Cadastrar Resposta Usuário \n(2) Ler Resposta Usuário \n(3) Atualizar Resposta Usuário \n(4) Deletar Resposta Usuário \nOpção: '))
        return opcao_resposta_usuario
    except ValueError:
        print('Você deve inserir um número entre (1 e 4).')
        return -1

def principal(api):
    escolha = 'SIM'
    while escolha.upper() == 'SIM':
        opcao = exibir_menu()
        match opcao:
            case 1:
                escolha_usuario = 'SIM'
                while escolha_usuario.upper() == 'SIM':
                    opcao_usuario = exibir_submenu_usuario()
                    match opcao_usuario:
                        case 1:
                            dados = pedir_cadastro_usuario(api)
                            if dados:
                                email, nome, idade, genero = dados
                                cadastrar_usuario(email, nome, idade, genero, api)
                        case 2:
                            id_usuario = input("Digite o ID do usuário que deseja ler: ")
                            resultado = ler_usuario(id_usuario, api)
                            if resultado:
                                id_usuario, email, nome, idade, genero = resultado
                                resposta = deseja_salvar_json()
                                if resposta:
                                    salvar_json_usuario(id_usuario, email, nome, idade, genero)
                        case 3:
                            dados = pedir_atualizacao_usuario(api)
                            if dados:
                                id_usuario, email, nome, idade, genero = dados
                                atualizar_usuario(id_usuario, email, nome, idade, genero, api)
                        case 4:
                            id_usuario = input("Digite o ID do usuário que deseja deletar: ")
                            deletar_usuario(id_usuario, api)
                        case _:
                            print('Opção inválida. Por favor, selecione uma opção válida.')
                    escolha_usuario = input('Deseja voltar ao menu de usuário? (sim/não): ')

            case 2:
                escolha_feedback = 'SIM'
                while escolha_feedback.upper() == 'SIM':
                    opcao_feedback = exibir_submenu_feedback()
                    match opcao_feedback:
                        case 1:
                            dados = pedir_cadastro_feedback(api)
                            if dados:
                                id_usuario, mensagem = dados
                                cadastrar_feedback(id_usuario, mensagem, api)
                        case 2:
                            id_feedback = input("Digite o ID do feedback que deseja ler: ")
                            resultado = ler_feedback(id_feedback, api)
                            if resultado:
                                id_feedback, id_usuario, mensagem = resultado
                                resposta = deseja_salvar_json()
                                if resposta:
                                    salvar_json_feedback(id_feedback, id_usuario, mensagem)
                        case 3:
                            dados = pedir_atualizacao_feedback(api)
                            if dados:
                                id_feedback, id_usuario, id_resposta, mensagem = dados
                                atualizar_feedback(id_feedback, id_usuario, mensagem, api)
                        case 4:
                            id_feedback = input("Digite o ID do feedback que deseja deletar: ")
                            deletar_feedback(id_feedback, api)
                        case _:
                            print('Opção inválida. Por favor, selecione uma opção válida.')
                    escolha_feedback = input('Deseja voltar ao menu de feedback? (sim/não): ')

            case 3:
                escolha_habito = 'SIM'
                while escolha_habito.upper() == 'SIM':
                    opcao_habito = exibir_submenu_habito()
                    match opcao_habito:
                        case 1:
                            dados = pedir_cadastro_habito(api)
                            if dados:
                                tipo, descricao, unidade = dados
                                cadastrar_habito(tipo, descricao, unidade, api)
                        case 2:
                            id_habito = input("Digite o ID do hábito que deseja ler: ")
                            resultado = ler_habito(id_habito, api)
                            if resultado:
                                id_habito, tipo, descricao, unidade = resultado
                                resposta = deseja_salvar_json()
                                if resposta:
                                    salvar_json_habito(id_habito, tipo, descricao, unidade)
                        case 3:
                            dados = pedir_atualizacao_habito(api)
                            if dados:
                                id_habito, tipo, descricao, unidade = dados
                                atualizar_habito(id_habito, tipo, descricao, unidade, api)
                        case 4:
                            id_habito = input("Digite o ID do hábito que deseja deletar: ")
                            deletar_habito(id_habito, api)
                        case _:
                            print('Opção inválida. Por favor, selecione uma opção válida.')
                    escolha_habito = input('Deseja voltar ao menu de hábito? (sim/não): ')

            case 4:
                escolha_resposta_usuario = 'SIM'
                while escolha_resposta_usuario.upper() == 'SIM':
                    opcao_resposta_usuario = exibir_submenu_resposta_usuario()
                    match opcao_resposta_usuario:
                        case 1:
                            dados = pedir_cadastro_resposta_usuario(api)
                            if dados:
                                id_usuario, id_habito, resposta, obervacoes = dados
                                cadastrar_resposta_usuario(id_usuario, id_habito, resposta, obervacoes, api)
                        case 2:
                            id_resposta_usuario = input("Digite o ID da resposta do usuário que deseja ler: ")
                            resultado = ler_resposta_usuario(id_resposta_usuario, api)
                            if resultado:
                                id_resposta, id_usuario, id_habito, resposta, obervacoes = resultado
                                resposta_salvar = deseja_salvar_json()
                                if resposta_salvar:
                                    salvar_json_resposta_usuario(id_resposta, id_usuario, id_habito, resposta, obervacoes)
                        case 3:
                            dados = pedir_atualizacao_resposta_usuario(api)
                            if dados:
                                id_resposta, id_usuario, id_habito, resposta, obervacoes = dados
                                atualizar_resposta_usuario(id_resposta, id_usuario, id_habito, resposta, obervacoes, api)
                        case 4:
                            id_resposta = input("Digite o ID da resposta do usuário que deseja deletar: ")
                            deletar_resposta_usuario(id_resposta, api)
                        case _:
                            print('Opção inválida. Por favor, selecione uma opção válida.')
                    escolha_resposta_usuario = input('Deseja voltar ao menu de resposta do usuário? (sim/não): ')

            case _:
                print('Opção inválida. Por favor, selecione uma opção válida.')
        escolha = input('Deseja voltar ao menu principal? (sim/não): ')
    print('Obrigado por usar o WellMind! Até a próxima.')


# Programa Principal
api = "https://wellmind-caqg.onrender.com"
principal(api)
