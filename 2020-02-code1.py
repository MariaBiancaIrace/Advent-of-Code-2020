import re

input_file = '/home/bibi/python/2020-02-input.txt'
input1 = open(input_file,'r')
lista_linhas = input1.readlines()
resultado = 0

for linha in lista_linhas:
    linha = re.sub('-|:', ' ', linha)
    linha = re.sub('\n','', linha)
    linha = re.split('  | ', linha)

    min = linha[0]
    max = linha[1]
    letra = linha[2]
    senha = linha[3]
    contador = 0

    for caractere in senha:
        if caractere == letra: 
            contador = contador+1
    
    if contador >=int(min) and contador <= int(max):
        resultado = resultado + 1


    print(min, max, letra, senha, contador, resultado)



input1.close()
