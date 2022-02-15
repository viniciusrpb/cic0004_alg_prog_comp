diametro = int(input())

altura,largura,profundidade = (int(x) for x in input().split())

if diametro <= altura and diametro <= largura and diametro <= profundidade:
    print('S')
else:
    print('N')


