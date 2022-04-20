dic = {}

def lerArquivo():
    arq = "usuarios.txt"
    with open(arq, 'r') as file:
        for line in file:
            nome = line.split()[0]
            usoMB = int(line.split()[1])/1000000
            percentual = (usoMB*100)/500000 
            dic[nome] = [usoMB, percentual]

def escreverArquivo():
    arq = "relatorio.txt"
    somaMb = 0
    somaPercent = 0
    with open(arq, 'w') as file:
        for e in dic.items():
            nome = e[0]
            usoMb = e[1][0]
            percentual = e[1][1]
            somaMb += usoMb
            somaPercent += percentual
            file.write(f"{nome}/{usoMb}/{percentual}\n")
        file.write(f"Total de Disco ocupado (MB): {somaMb}\n")
        file.write(f"Total de Disco ocupado (%): {somaPercent}")
    

lerArquivo()
escreverArquivo()