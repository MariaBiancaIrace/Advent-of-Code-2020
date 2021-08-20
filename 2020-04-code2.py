with open("2020-04-input.txt") as arquivo:
    lista_linhas = arquivo.read()

lista_linhas = lista_linhas.replace('\n\n','AAAAA')
lista_linhas = lista_linhas.replace('\n',' ')
lista_linhas = lista_linhas.replace('AAAAA','\n').splitlines()

contador_validos = 0



for linha in lista_linhas:
    total_itens = len(linha.split(' '))
    if total_itens in range(7,9):
        lista_itens = linha.strip().split(' ')
        dicionario = {}
        lista_itens_validar = ['byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']
        for itens in lista_itens:
            chave,valor = itens.strip().split(':')
            dicionario[chave] = valor
        
        check = all(item in dicionario.keys() for item in lista_itens_validar)
        if check is True:
            if (int(dicionario['byr']) in range(1920,2003)) and (int(dicionario['iyr']) in range(2010,2021)) and (int(dicionario['eyr'] in range(2020,2031))):
                print(dicionario, 'OK')
            else:
                print(dicionario,'valor ruim')
        else:
            print(dicionario,'NOK')
            #total_chave_valor = len(itens.strip().split(':'))
            #print(itens, total_itens,total_chave_valor)
    ##linha = linha.split(' ')
    ##dicionario = {}
    ##for item in linha:
        ##print(len(item), len(item.strip().split(':')))
        ##chave,valor = item.strip().split(':')
        ##if valor is None:
        ##    valor='0'    
        ##dicionario[chave] = valor
    ##print(dicionario,type(dicionario))
    
    #if ('byr','iyr','eyr') in dicionario.keys(): 
    #    if int(dicionario['byr']) in range(1920,2003) and int(dicionario['iyr']) in range(2010,2021) and int(dicionario['eyr'] in range(2020,2031)):
    #        print('byr, iyr and eyr ok')



    #if ('byr' in linha and 'iyr' in linha and 'eyr' in linha and 'hgt' in linha and 'hcl' in linha and 'ecl' in linha and 'pid' in linha):
    #    contador_validos += 1
    #    print(linha, contador_validos)


