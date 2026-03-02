#funcao open() serve para persistencia de dados ou leitura de arquivos de texto, ela recebe. tres parametros, (arquivo, modo, codificacao)
#arquivo: o nome do arquivo
#modo: indica se e leitura de arquivo ou se ira escrever ("w", "r")
#codificacao: indica a forma que o computador deve interpretar os caracteres ques estao no arquivo, o mais comum é "utf-8"
#sempre que utilizarmo a funcao open(), devemos usar o metodo .close() no final, para fechar o arquivo, ou podemos usar a combinacao da funcao with com open(), assim o arquivo sera fechado automaticamente
#sobre REST APIs o JSON é uma das maneiras de trafico de dados dela, usa o padrao key:value, igual ao dicionario

#metodo dumps(), nao é possivel escrever em um arquivo de texto colecoes, porem existe um metodo de JSON, que converte colecoes em str, ai sim podemos escrever essa colecao em uma arquivo de texto
#dumps() receber tres parametros, (colecao, indent=4, ensure_ascii=False)
#colecao: é literalmente a colecao, um dicionario por ex
#indent=4: indentacao para cada nivel do JSON
#ensure_ascii=False: usado para o computador entender caracteres especias latinos e acentos

#primeiro precisamos importar o módulo json
import json
#vamos criar um dicionário como exemplo
dicionario = {
    "nome":"Python",
    "missão":"Ser incrível!"
}
#Agora vamos utilizar a função dumps do módulo json para converter nosso dicionário
#O resultado será uma string com estrutura do JSON
texto = json.dumps(dicionario, indent=4, ensure_ascii=False)
print(f"O dicionário foi convertido para a str texto, e seu conteúdo é: {texto}")
#Já que o nosso JSON é só um texto, podemos gravá-lo normalmente
with open("arquivo.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)
    print("Pronto! O texto no formato json foi salvo dentro de um arquivo!")


#o caminho inverso, para ler um arquivo JSON e transforma ele em um dicionario, usamos o metodo .loads(), ele recebe o conteudo do arquivo como parametro

#Vamos ler o conteúdo do arquivo json como um texto normal
with open("arquivo.json", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
#Agora vamos colocar a nossa string na função loads para que o Python interprete e gere
#a estrutura adequada:
dicionario_2 = json.loads(conteudo)
print(f"O conteúdo do arquivo foi carredado e convertido: {dicionario_2}")

#pip ferramenta que armazena bibliotecas padrao do py

#PEP 8 é o guia oficial de estilo de código do Python.
#Ele define como escrever código Python de forma organizada, legível e consistente. Define as regras do py, https://peps.python.org/pep-0008/ url do site.