with open("2020-04-input.txt") as arquivo:
    lista_linhas = arquivo.read()

lista_linhas = lista_linhas.replace('\n\n','AAAAA')
lista_linhas = lista_linhas.replace('\n',' ')
lista_linhas = lista_linhas.replace('AAAAA','\n').splitlines()

contador_validos = 0



for linha in lista_linhas:
    linha = linha.split(' ')
    dicionario = {}
    for item in linha:
        chave = item.strip().split(':')[0]
        if item.strip().split(':')[1] is None:
            valor='0'
        else:
            valor = item.strip().split(':')[1]    
        #chave, valor = item.strip().split(':')
        dicionario[chave] = valor
    print(dicionario)
    #if ('byr','iyr','eyr') in dicionario.keys(): 
    #    if int(dicionario['byr']) in range(1920,2003) and int(dicionario['iyr']) in range(2010,2021) and int(dicionario['eyr'] in range(2020,2031)):
    #        print('byr, iyr and eyr ok')



    #if ('byr' in linha and 'iyr' in linha and 'eyr' in linha and 'hgt' in linha and 'hcl' in linha and 'ecl' in linha and 'pid' in linha):
    #    contador_validos += 1
    #    print(linha, contador_validos)


