n = int(input())
brinquedos = input().split()
brinquedos_original = brinquedos[:]
d = 5
while d > 0:
    brinquedo,orientacao,casas = input().split()
    casas = int(casas)
    index = brinquedos.index(brinquedo)
    #brinquedos.remove(brinquedo)
    #del brinquedos[index]
    brinquedos.pop(index)
    if orientacao == "D":
        index += casas
        if index >= n:
            index = n-1
        brinquedos.insert(index,brinquedo)
    else:
        index -= casas
        if index < 0:
            index = 0
        brinquedos.insert(index,brinquedo)
    d -= 1

soma = 0
for i in range(n):
    if brinquedos[i] != brinquedos_original[i]:
        soma += 1
print(soma)

"""Gustavo V.
soma = 0
pos = 0
for i in brinquedos:
    if i != brinquedos_original[pos]:
        soma += 1
    pos += 1
print(soma)
"""




