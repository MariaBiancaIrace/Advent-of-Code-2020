input_file = '/home/bibi/python/2020-01-input.txt'

input1 = open(input_file,'r')

lista_linhas = input1.readlines()

for linha in lista_linhas:
    for linha2 in lista_linhas:
        for linha3 in lista_linhas:
            if (int(linha) + int(linha2) + int(linha3) == 2020):
                num1=int(linha)
                num2=int(linha2)
                num3=int(linha3)
                produto = num1*num2*num3

print("Os numeros são ")
print(num1)
print(num2) 
print(num3)
print("e o produto deles é")
print(produto)




input1.close()
