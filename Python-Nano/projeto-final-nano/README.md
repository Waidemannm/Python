## Ideia do Projeto

Temos o arquivo manipulacao_agenda.py.
A agenda será um dicionário, onde as keys são os nome de contato, e o value, será outro dicionário entro do dicionário agenda. Esse dicionário interno contará com as seguintes keys (telefone, email e endereco), essas keys serão listas, o usuário só vai poder adicionar um novo contato, se conter ao menos uma dessas 3 formas de contato.

## Exemplo: 

````

//os values são list, entao podem receber um ou mais valores

contatos_suportados = ("telefone", "email", "endereco")

agenda = {
    "Pessoa 1":{
        "telefone":["11 1234-5678"],
        "email":["pessoa@email.com", "email@profissional.com"],
        "endereco":["Rua 123"]
    },
    "Pessoa 2":{
        "telefone":["11 9874-5678"],
        "email":["pessoa2@email.com", "pessoa2@profissional.com"], 
        "endereco":["Rua 345"]
    }
}

````

## Manipulações:

- Inserir um contato;
- Inserir uma nova forma de contato a um contato já existente;
- Alterar um contato, ou uma das formas de contato;
- Excluir contato;
- Exibir o dicionário em forma de texto;
- Exibir apenas um contato em forma de texto;
- Exportar todos o contatos em forma de .txt;
- Exportar todos o contatos em forma de .json;
- Carregar contatos a partir de um JSON;


## Funções:

exibir_menu(): ira mostrar as opcoes, opções que existiram no menu 
( 
1- Inserir um contato;
2- Inserir uma nova forma de contato a um contato já existente;
3- Alterar o nome de contato, 
4- Alterar uma das formas de contato;
5- Excluir contato;
6- Exibir o dicionário em forma de texto;
7- Exibir apenas um contato em forma de texto;
8- Exportar todos o contatos em forma de .txt;
9- Exportar todos o contatos em forma de .json;
10- Carregar contatos a partir de um JSON;
11- Sair 
);

pedir_opcao(): ira pedir a opcao desejada e retorna-la

main(opcao): ira receber a opcao e controlar o fluxo com um match case;

############################

