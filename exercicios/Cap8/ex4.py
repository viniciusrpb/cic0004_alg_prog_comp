frase = input()
decodificada = ""
for letra in frase:
    if letra.islower():
        decodificada += "L"
    elif letra.isupper():
        decodificada += "U"
    elif letra.isnumeric():
        decodificada += "D"
    elif letra.isspace():
        decodificada += "W"
print(decodificada)