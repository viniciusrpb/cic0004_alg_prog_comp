

n = int(input())
maximo = float("-inf")
minimo = float("inf")
while n > 0:
    x,y = input().split()
    x,y = [int(x), int(y)]
    soma = 0
    if x%2 == 0:#par
        x += 1
    while y > 0:
        soma += x
        x += 2
        y -= 1
    print(soma)
    if soma > maximo:
        maximo = soma
    if soma < minimo:
        minimo = soma
    n -= 1
    
print(f"{maximo}\n{minimo}\n{(maximo+minimo)/2:.2f}")