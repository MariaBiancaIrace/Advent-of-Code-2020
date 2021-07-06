with open("2020-03-input.txt") as file:
    lista_linhas = file.read().splitlines()

coluna_regra1 = -1
coluna_regra2 = -3
coluna_regra3 = -5
coluna_regra4 = -7
coluna_regra5 = -1
contador_regra1 = 0
contador_regra2 = 0
contador_regra3 = 0
contador_regra4 = 0
contador_regra5 = 0
contador_linha = 0

for linha in lista_linhas:
    contador_linha +=1
    coluna_regra1 +=1
    coluna_regra2 +=3
    coluna_regra3 +=5
    coluna_regra4 +=7
    if(linha[coluna_regra1%31] == '#'):
        contador_regra1 += 1
    if(linha[coluna_regra2%31] == '#'):
        contador_regra2 += 1
    if(linha[coluna_regra3%31] == '#'):
        contador_regra3 += 1
    if(linha[coluna_regra4%31] == '#'):
        contador_regra4 += 1
    if(contador_linha % 2 == 1):
        coluna_regra5 += 1
        if(linha[coluna_regra5%31] == '#'):
            contador_regra5 += 1

    print(linha, contador_regra1,contador_regra2,contador_regra3,contador_regra4,contador_regra5)

print('Resultado:',contador_regra1*contador_regra2*contador_regra3*contador_regra4*contador_regra5)
