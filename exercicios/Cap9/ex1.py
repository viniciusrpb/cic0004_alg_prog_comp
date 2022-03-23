fatias,premiada = map(int, input().split())
bolo = [False] * fatias
bolo[premiada] = True
ganhador = ""
while fatias > 0:
    nome,fatia = input().split()
    if bolo.pop(int(fatia)):
        ganhador = nome
    fatias -= 1
print(ganhador)



