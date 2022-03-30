import os
import random
import time
import copy

os.system('clear') or None
n = int(input("Informe o tamannho do Jogo: "))
jogo = []

def cria_jogo(n):
    s = ".ox"
    for i in range(n):
        linha = []
        for j in range(n):
            e = random.randrange(3)
            linha.append(s[e])
        jogo.append(linha)

def imprime_jogo():
    os.system('clear') or None
    for linha in jogo:
        print(*linha)
        
def gravidade(jogo):
    for linha in range(len(jogo)-1,-1,-1):
        for coluna in range(len(jogo[linha])):
            if jogo[linha][coluna] == "o" and linha+1 < len(jogo):
                if jogo[linha+1][coluna] == ".":
                    jogo[linha][coluna] = "."
                    jogo[linha+1][coluna] = "o"
    return jogo

def fim_do_jogo():
    f = gravidade(copy.deepcopy(jogo))
    return f == jogo

cria_jogo(n)
vezes = 0
while True:
    imprime_jogo()
    
    #com tempo:
    time.sleep(1.5)
    jogo = gravidade(copy.deepcopy(jogo))
    vezes += 1
    #com acao:
    """
    if input("\nAgir Gravidade? (s/n): ") == "s":
        jogo = gravidade(copy.deepcopy(jogo))
        vezes += 1
    """
    if fim_do_jogo():
        imprime_jogo()
        print(f"\nFim do Jogo!\nA gravidade agiu {vezes} vezes")
        break

