def apresentacao(nome: str):
    print(f"Olá {nome}")

def pedir_nome():
    nome = input("Informe seu nome: ")
    return nome

nome = pedir_nome()
apresentacao(nome)

#quando voce determina o valor de um parametro ele se torna opcional, se nao for passado e assumido o valor default 
def calcular_velocidade_media(distancia: float, tempo:float, unidade_medida="km/h"):
    velocidade_media = distancia/tempo
    print(f"A velocidade média é {velocidade_media} {unidade_medida}")

calcular_velocidade_media(200, 10) #chamada omitindo o argumento unidade_medida
calcular_velocidade_media(200, 10, "m/s") #chamada passando o valor "m/s" para o argumento unidade_media

# o (*args)  passado no parametro de uma funcao indica que é um numero indeterminado de parametros
def exibe_promocao(*clientes):
    for cliente in clientes:
        print(f"Olá, {cliente}!\nQueremos te avisar que a nova X-WING está em promoção!")
exibe_promocao("Luke", "Princesa Leia", "Mestre Yoda")## ou passe uma colecao do tipo list ou tuple ex:lista = ["Luke", "Princesa Leia", "Mestre Yoda"] exibe_promocao(*lista)

#ja para dicionarios no caso de key:value usamos (**kwargs)

def exibe_ficha(**dados):
    print(dados)
    print("----FICHA----")
    for chave, valor in dados.items():
        print(f"{chave.upper()} -- {valor}")
ficha_cliente = {
    "nome":"Dino da Silva Sauro",
    "estado civil":"casado",
    "camisa":"xadrez",
    "filhos": True
}
exibe_ficha(**ficha_cliente)

#funcao que possui return sempre que for invocada deve ser usada dentro de uma variavel

#sempre devemos documentar cada funcao com a docstring, é uma explicao do que aquela funçao faz, deve conter quais parametros recebe, o que faz e o retorno, ele é criado com 3 aspas duplas no inicio da funcao, ele é visto toda vex que invocamos a funcao e passamos o mouse encima do nome dela, ou quando usamos o metodo .__doc__ apos a invocacao da funcao ou a funcao help(), retornara essa docstring
def somar(a:float, b:float):
    """Recebe dois argumentos, a e b, tipo float e realiza a soma.
     Retorna o resultado no formato float"""
    return a + b

print(f"Chamando o método doc para ler a documentação: {somar.__doc__}")
print(f"Chamando a função help para ler a documentação: {help(somar)}")


#Projeto
def exibir_menu():
    """
    PARAMÊTROS: nenhum
    FUNCIONALIDADE: mostrar menu de opções 
    RETORNO: opção escolhida
    """
    print("<--->MENU<--->")
    print("Opção 1: Calcular velocidade média \nOpção 2: Converter a temperatura \nSair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def aula_de_fisica(opcao):
    """
    PARAMÊTROS: opcao escolhida
    FUNCIONALIDADE: definir qual função será chamada
    RETORNO: nenhum
    """
    match opcao:
        case 1:
            distancia = float(input("Digite a distância percorrida: "))
            tempo = float(input("Digite o tempo: "))
            unidade_medida = input("Digite a unidade de medida desejada: ")
            media =calcular_velocidade_media(distancia, tempo, unidade_medida)
            print(f"Velocidade média é: {media}")
        case 2:
            temperatura = int(input("Digite a temperatura: "))
            unidade_medida = input("Qual a unidade de medida da temperatura: ") 
            temp_convertida = converter_temperatura(temperatura, unidade_medida)
            print(f"A temperatura convertida é: {temp_convertida}")
        case 3:
            print("Fim de programa, até a próxima!")
        case _:
            print("Opção inválida. Tente novamente! \n")
            opcao = exibir_menu()
            aula_de_fisica(opcao)
            
def calcular_velocidade_media(distancia: float, tempo: float, unidade_medida="km/h"):
    """
    PARAMÊTROS:
    FUNCIONALIDADE:
    RETORNO: uma string com a velocidade média
    """
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f"{velocidade_media} {unidade_medida}"

def converter_temperatura(temperatura: int, unidade_medida="Celsius"):
    """
    PARAMÊTROS:
    FUNCIONALIDADE:
    RETORNO: uma string com a temperatura convertida
    """
    if unidade_medida == "Celsius":
        return temperatura * 1.8 + 32
    elif unidade_medida == "Fahrenheit":
        return (temperatura - 32) / 1.8
    else:
        return 0

opcao = exibir_menu()
aula_de_fisica(opcao)