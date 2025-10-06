try:
    arquivo = ('meu_arquivo.txt,' 'r')
    conteudo = arquivo.read()
    print('arquivo foi lido com sucesso!')
except FileNotFoundError:
    print('Arquivo inexistente')
else:
    print('Nenhum erro ocorreu')
finally:
    arquivo.close()