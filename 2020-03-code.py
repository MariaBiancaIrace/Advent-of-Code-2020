with open("2020-03-input.txt") as file:
    lista_linhas = file.read().splitlines()

coluna = int('-3')
contador = 0

for linha in lista_linhas:
    #print(linha[0%31],linha[31%31])
    coluna +=3
    if(linha[coluna%31] == '#'):
        contador += 1
    print(coluna,linha[coluna%31],contador)



