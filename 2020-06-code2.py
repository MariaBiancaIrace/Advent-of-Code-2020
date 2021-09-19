import string

with open("2020-06-input.txt") as arquivo:
        lista_linhas = arquivo.read()

lista_linhas = lista_linhas.replace('\n\n','AAAAA')
lista_linhas = lista_linhas.replace('\n',' ')
lista_linhas = lista_linhas.replace('AAAAA','\n').strip().splitlines()


set_pessoa = set()
contador = 0

for linha in lista_linhas:
    lista_set_grupo = []
    lista_string_grupo = linha.split(' ')
    print(lista_string_grupo)
    ##['frpcbmnh', 'ohmwzj', 'hvtm']
    for string_pessoa in lista_string_grupo:
        set_pessoa = set(string_pessoa)
        #{'f','r','p'...}
        lista_set_grupo.append(set_pessoa)
    print(lista_set_grupo)
    #[{'f', 'r', 'p',...}, {'o', 'h', 'm',...}, {'h', 'v', 't',...}]
    set_intersec = set(string.ascii_lowercase)
    print(set_intersec)
    for set_pessoa in lista_set_grupo:
        set_intersec = set_intersec.intersection(set_pessoa)
    contador = contador + len(set_intersec)
    print(set_intersec, len(set_intersec),contador)

