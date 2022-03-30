n = int(input())
jogo = []

def ler_jogo(n):
    for _ in range(n):
        jogo.append(input().split())

def mostra_jogo():
    for linha in jogo:
        print(*linha)

def gravidade():
    for i in range(len(jogo)-1,-1,-1):
        for j in range(len(jogo[i])):
            if jogo[i][j] == "o" and i+1 < len(jogo) and jogo[i+1][j] == ".":
                jogo[i][j],jogo[i+1][j] = jogo[i+1][j],jogo[i][j]

ler_jogo(n)
gravidade()
mostra_jogo()



