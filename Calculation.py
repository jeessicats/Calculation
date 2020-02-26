linha = '-' * 125
titulo = "Programa de estatística"
nome = "Jéssica Teixeira dos Santos"
linha2 = '*' * 50 + "\n"

print(linha)
print(titulo.center(125))
print(linha)

print(nome.rjust(125))

print("\nBem vindo ao programa de estatística.\nPara começar selecione um arquivo contendo um conjunto de valores e um comando para calcular média, desvio padrão e mediana.\n")
print("Comandos válidos:\nPara calcular apenas a média: media\nPara calcular média e desvio padrão: media+sd\nE para calcular média, desvio padrão e mediana: media+sd+mediana\n\nPara sair digite: 'exit'.\n")

import statistics
import sys

try:
    if sys.argv[1] == "numeros.txt":
        f = open("numeros.txt","r")
        print("Cálculo efetuado com sucesso! Seu resultado foi impresso no arquivo 'resultado.txt'.")
    elif sys.argv[1] != "numeros.txt":
        while True:
            print("Este arquivo não existe!")
            try:
                file_name = input("Digite o nome de um arquivo:\n")
                if (file_name == "exit"):
                    print("Programa finalizado!")
                    sys.exit()
                f = open(file_name)
                print("Cálculo efetuado com sucesso! Seu resultado foi impresso no arquivo 'resultado.txt'.")
                break
            except FileNotFoundError:
                print("Este arquivo não existe!\n")
except IndexError:
    while True:
            try:
                file_name = input("Digite o nome de um arquivo:\n")
                if (file_name == "exit"):
                    print("Programa finalizado!")
                    sys.exit()
                f = open(file_name)
                print("Cálculo efetuado com sucesso! Seu resultado foi impresso no arquivo 'resultado.txt'.")
                break
            except FileNotFoundError:
                print("Este arquivo não existe!\n")

num = f.read()
numeros = num.split()

comando = numeros.pop(0)
comando = comando.lower()

c = 0
for i in numeros:
    numeros[c] = float(i)
    c = c + 1

word = "media"
word2 = "media+sd"
word3 = "media+sd+mediana"

media = 0
sd = 0
mediana = 0

for i in numeros:
    if (comando == word):
        media = statistics.mean(numeros)
    elif (comando == word2):
        media = statistics.mean(numeros)
        sd = statistics.stdev(numeros)
    elif (comando == word3):
        media = statistics.mean(numeros)
        sd = statistics.stdev(numeros)
        mediana = statistics.median(numeros)
    else:
        print("Este arquivo não contém um comando válido!\nOs comando possíveis são:\nmedia\nmedia+sd\nmedia+sd+mediana\n\nCorrija seu arquivo e tente novamente!")
        break

media = str(media)
sd = str(sd)
medi = str(mediana)

f2 = open("resultado.txt","w")
f2.write("INPUT:\n\n")
f2.write(linha2) + f2.write(num) + f2.write(linha2)
f2.write("\nRESULTADOS:\n\n")
if comando == word:
    f2.write("Média calculada: ") + f2.write(media)
elif comando == word2:
    f2.write("Média calculada: ") + f2.write(media)
    f2.write("\nDesvio padrão calculado: ") + f2.write(sd)
elif comando == word3:
    f2.write("Média calculada: ") + f2.write(media)
    f2.write("\nDesvio padrão calculado: ") + f2.write(sd)
    f2.write("\nMediana calculada: ") + f2.write(medi)

f.close()
f2.close()