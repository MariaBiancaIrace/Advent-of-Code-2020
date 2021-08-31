import re

with open("2020-05-input.txt") as arquivo:
    lista_linhas = arquivo.read().splitlines()

maxID = 0
lista_IDs = []

for linha in lista_linhas:
    #linha = linha.replace('F','0')
    #linha = linha.replace('L','0')
    #linha = linha.replace('B','1')
    #linha = linha.replace('R','1')
    linha = re.sub('[FL]','0',linha)
    linha = re.sub('[BR]','1',linha)
    valor_linha = linha[:7]
    valor_coluna = linha[-3:]
    ID = int(valor_linha,2)*8+int(valor_coluna,2)
    lista_IDs.append(ID)
    if(maxID < ID): 
        maxID = ID
    print(maxID, linha,valor_linha,int(valor_linha,2),valor_coluna,int(valor_coluna,2),ID)
    

print(lista_IDs)

valor_min = min(lista_IDs) 
valor_max = max(lista_IDs)

for i in range(valor_min,valor_max+1):
    if i not in lista_IDs:
        print(i)
