diametro = int(input())

altura,largura,profundidade = (int(x) for x in input().split())

if diametro > altura or diametro > largura or diametro > profundidade:
    print('N')
else:
    print('S')


