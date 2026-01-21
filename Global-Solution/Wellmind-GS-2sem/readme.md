📌 Sobre o Projeto
WellMind é um sistema de bem-estar inteligente que permite gerenciar Usuários, Feedback, Hábitos e Respostas do Usuário através de um CRUD completo desenvolvido em Python.
A aplicação consome uma API Java (Spring Boot) já hospedada no Render:
https://wellmind-caqg.onrender.com

O usuário navega por menus interativos e realiza operações de Create, Read, Update e Delete diretamente no banco de dados da API.
Após operações de leitura, o sistema permite exportar os dados lidos em arquivos JSON, atendendo ao requisito da disciplina.

📁 Estrutura do Sistema (Python)
O arquivo principal é:
wellmind.py

Ele contém:
Validações de entrada (email, idade, gênero, tipo de hábito, etc.)
Módulos completos de CRUD:

usuário

feedback

hábito

resposta_usuario

Funções auxiliares para checagem de existência no banco via API

Funções de exportação de JSON

Menus e submenus interativos

Loop principal principal() para navegação


⚙️ Tecnologias Utilizadas
O código usa apenas bibliotecas nativas do Python + requests.
Bibliotecas usadas:
BibliotecaNativa?Finalidaderequests❌ ExternaComunicação HTTP com a APIos✔️ SimManipulação de diretórios/pathsjson✔️ SimGeração de arquivos JSON

📦 Instalação
1. Instalar Python 3.10+
Baixe em:
https://www.python.org/downloads/
Durante a instalação, marque:
Add Python to PATH

2. Instalar a única biblioteca externa
No terminal (cmd ou PowerShell):
pip install requests

3. Baixar o arquivo wellmind.py
Coloque-o em uma pasta acessível (ex: C:\GS-WellMind)

▶️ Como Executar o Sistema
No terminal, navegue até a pasta do projeto:
cd C:\GS-WellMind

Execute:
python wellmind.py

A aplicação abrirá o menu principal:
*-- WellMind - Bem estar Inteligente --*
(1) Usuário
(2) Feedback
(3) Hábito
(4) Resposta Usuário


🌐 Comunicação com a API
O CRUD conversa com estes endpoints:
EntidadeEndpoints usadosUsuárioGET /usuario, GET /usuario/{id}, POST /usuario, PUT /usuario/{id}, DELETE /usuario/{id}FeedbackGET /feedback, GET /feedback/{id}, POST /feedback, PUT /feedback/{id}, DELETE /feedback/{id}HábitoGET /habito, GET /habito/{id}, POST /habito, PUT /habito/{id}, DELETE /habito/{id}Resposta UsuárioGET /resposta_usuario/{id}, POST /resposta_usuario, PUT /resposta_usuario/{id}, DELETE /resposta_usuario/{id}
O código valida IDs consultando diretamente os endpoints antes de qualquer operação.

📝 Exportação de JSON
Após cada operação Read, aparece:
Deseja salvar os dados em um arquivo JSON? (sim/não)

Se aceitar, o sistema salva um arquivo em:
./Python/

Com nomes como:

usuario_5.json

feedback_12.json

habito_3.json

resposta_usuario7.json

🔧 Requisitos da Entrega (FIAP — Python)
Este README atende ao item:
Instruções de Instalação (README)

Como instalar dependências ✔️

Como executar o sistema ✔️

Como a aplicação funciona ✔️

Dependências externas ✔️

🎬 Como o usuário deve navegar no sistema

Execute o sistema

Escolha uma categoria (Usuário / Feedback / Hábito / Resposta)

Escolha entre criar, ler, atualizar ou deletar

Informe os dados solicitados

Após leituras, escolha se deseja gerar um JSON

Continue navegando até optar por sair

📎 Observação sobre a API
Como o sistema depende totalmente da API Java hospedada, o Python não acessa diretamente o Oracle; todas as operações usam requisições HTTP.