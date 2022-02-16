"""
Implemente uma função recursiva que, dados dois
números inteiros positivos x e n, calcula o valor de x**n.
Caso base: x**0 = 1
Passo da recursão: x**n = x* x**(n-1)
"""
def powAPC(x,y):
    if y == 1:
        return x
    else:
        return x*powAPC(x,y-1)
print(powAPC(5,3))


