"""
frase = input()
decodificada = ""
for palavra in frase.split():
    for c in palavra:
        decodificada += "p"+c
    decodificada += " "
print(decodificada[:-1])
"""
#Um filme legal -> pUpm pfpiplpmpe plpepgpapl
#A papa do Papa -> pA pppapppa pdpo pPpapppa

print(" ".join(["".join(["p"+c for c in palavra]) for palavra in input().split()]))