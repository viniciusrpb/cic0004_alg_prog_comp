
def ordena(a,b,c):
    if a > b and a > c:
        if b > c:
            return a,b,c
        else:
            return a,c,b
    elif b > c and b > a:
        if a > c:
            return b,a,c
        else:
            return b,c,a
    else:
        if a > b:
            return c,a,b
        else:
            return c,b,a
    
#entrada
#a,b,c = map(float,input().split())
a = float(input())
b = float(input())
c = float(input())

#computacao:
a,b,c = ordena(a,b,c)

if a >= b+c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c:
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")

