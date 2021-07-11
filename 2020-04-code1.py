with open("2020-04-input.txt") as arquivo:
    lista_linhas = arquivo.read()

lista_linhas = lista_linhas.replace('\n\n','AAAAA')
lista_linhas = lista_linhas.replace('\n',' ')
lista_linhas = lista_linhas.replace('AAAAA','\n').splitlines()

contador_validos = 0

for linha in lista_linhas:
    if ('byr' in linha and 'iyr' in linha and 'eyr' in linha and 'hgt' in linha and 'hcl' in linha and 'ecl' in linha and 'pid' in linha):
        contador_validos += 1
        print(linha, contador_validos)


