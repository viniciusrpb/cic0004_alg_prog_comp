frase = input()
decodificada = ""
for palavra in frase.split():
    for c in palavra:
        decodificada += "p"+c
    decodificada += " "
print(decodificada[:-1])
