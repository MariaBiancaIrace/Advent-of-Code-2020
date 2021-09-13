with open("2020-06-input.txt") as arquivo:
        lista_linhas = arquivo.read()

        lista_linhas = lista_linhas.replace('\n\n','AAAAA')
        lista_linhas = lista_linhas.replace('\n','')
        lista_linhas = lista_linhas.replace('AAAAA','\n').splitlines()

contador = 0

for linha in lista_linhas:
    set_perguntas = set()
    for letra in linha:
        set_perguntas.add(letra)
        
    contador = contador + len(set_perguntas)
    print(linha,set_perguntas,len(set_perguntas),contador) 
