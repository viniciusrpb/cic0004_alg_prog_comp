"""
frase = input()
decodificada = ""
for palavra in frase.split():
    decodificada += palavra[2]
print(decodificada)
"""

#André tretou cabum brocado trans pus -> deboas
#Esparta prestigia derrotas trincadas legais problemáticas -> perigo

print("".join([palavra[2] for palavra in input().split()]))