"""
frase = input()
decodificada = ""
for palavra in frase.split():
    decodificada += palavra[1::2] + " "
print(decodificada[:-1])
"""
#pUpm pfpiplpmpe plpepgpapl -> Um filme legal
#pA pppapppa pdpo pPpapppa -> A papa do Papa

print(" ".join([palavra[1::2] for palavra in input().split()]))
