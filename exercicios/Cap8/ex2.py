frase = input()
decodificada = ""
for palavra in frase.split():
    decodificada += palavra[1::2] + " "
print(decodificada[:-1])
