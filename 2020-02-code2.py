import re

input_file = '/home/bibi/python/2020-02-input.txt'
input1 = open(input_file,'r')
lista_linhas = input1.readlines()
resultado = 0

for linha in lista_linhas:
    linha = re.sub('-|:', ' ', linha)
    linha = re.sub('\n','', linha)
    linha = re.split('  | ', linha)

    min = int(linha[0])
    max = int(linha[1])
    letra = linha[2]
    senha = linha[3]
    contador = 0


    if senha[min-1] == letra:
        contador = contador+1
    if senha[max-1] == letra:
        contador = contador+1

    if contador == 1:
        resultado = resultado+1

    print(min, max, letra, senha, contador, resultado)


input1.close()
