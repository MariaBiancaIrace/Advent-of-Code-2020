with open("2020-06-input.txt") as arquivo:
        lista_linhas = arquivo.read()

lista_linhas = lista_linhas.replace('\n\n','AAAAA')
lista_linhas = lista_linhas.replace('\n',' ')
lista_linhas = lista_linhas.replace('AAAAA','\n').strip().splitlines()


set_pessoa = set()
set_grupo = set()

for linha in lista_linhas:
    lista_grupo = linha.split(' ')
    print(lista_grupo)
    for string_pessoa in lista_grupo:
        #print(string_pessoa)
        for letra in string_pessoa:
            #print(letra, string_pessoa)
            set_pessoa.add(letra)
        print(set_pessoa)
        set_grupo.update(set_pessoa)
        #print(linha, set_grupo)



''' 
set_pessoa = set()
set_grupo = set()

for letra in lista_linhas:
    set_pessoa.add(letra)
    
lista_linhas = lista_linhas.replace('\n\n','AAAAA')
        #lista_linhas = lista_linhas.replace('\n','')
        lista_linhas = lista_linhas.replace('AAAAA','\n').splitlines()

contador = 0

for linha in lista_linhas:
    set_perguntas = set()
    for letra in linha:
        set_perguntas.add(letra)
        
    contador = contador + len(set_perguntas)
    print(linha,set_perguntas,len(set_perguntas),contador) 

'''
