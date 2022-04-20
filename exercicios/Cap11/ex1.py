
def printaMediaNumero(n):
    arq = "notas.txt"
    with open(arq) as file:
        for line in file:
            numero = int(line.split()[0])
            if n == numero:
                return sum(list(map(float,line.split()[1:])))/len(line.split()[1:])

def printaNotasNumero(n):
    arq = "notas.txt"
    with open(arq) as file:
        for line in file:
            numero = int(line.split()[0])
            if n == numero:
                print(" ".join(line.split()[1:]))
                print(f"{printaMediaNumero(n):.2f}")

def printaNotasNome(entrada):
    arq = "classe.txt"
    with open(arq) as file:
        for line in file:
            nome = " ".join(line.split()[1:])
            if nome == entrada:
                cod = int(line.split()[0])
                printaNotasNumero(cod)
                print(f"{printaMediaNumero(cod):.2f}")

def buscaNotas(entrada):
    if entrada.isnumeric():
        printaNotasNumero(int(entrada))
    else:
        printaNotasNome(entrada)

entrada = input()
buscaNotas(entrada)