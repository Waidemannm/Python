from flask import Flask, jsonify
import os
import json
app = Flask(__name__)

@app.route('/medico/<int:id_medico>')
def api_medico(id_medico):
    try:
        pasta = "./cuida_mais_hc"
        nm_arquivo = f"medico_{id_medico}.json"
        caminho_arquivo = os.path.join(pasta, nm_arquivo)
        if not os.path.exists(caminho_arquivo):
            return jsonify({"erro": f"Arquivo {nm_arquivo} não encontrado."}), 404
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
            medico = json.load(arquivo_json)

        # Retorna o conteúdo como JSON pela API
        return jsonify(medico), 200
    
    except FileNotFoundError:
        print(f'\n [Erro] Arquivo {nm_arquivo} não encontrado.')
    except Exception as e:
        print(f'\n [Erro] Occoreu um erro ao ler o arquivo: {e}')

if __name__ == '__main__':
    app.run()