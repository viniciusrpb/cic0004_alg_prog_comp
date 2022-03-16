vezes = int(input())

somaP = 0
somaU = 0

while vezes > 0:
    frase = input()
    for c in frase:
        if c.lower() == "p":
            somaP += 1
        if c.lower() == "u":
            somaU += 1
    vezes -= 1
print(somaP,somaU)