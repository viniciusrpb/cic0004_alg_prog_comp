"""
O máximo divisor comum (MDC) de dois números inteiros
x e y pode ser calculado usando-se uma definição recursiva:
MDC(x, y) = MDC(x - y, y), se x > y
MDC(x,y) = MDC(y,x)
MDC(x,x) = x
Faça um programa que calcule o MDC
"""
def mdc(x,y):
    if x < y:
        x,y = y,x
    if x == y:
        return x
    else:
        return mdc(x - y, y)

x,y = map(int,input().split())
print(mdc(x,y))

    
    
