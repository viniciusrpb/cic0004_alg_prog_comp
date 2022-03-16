frase = input()
decodificada = ""
for palavra in frase.split():
    decodificada += palavra[2]
print(decodificada)