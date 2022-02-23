
x = 31

def oi(nome, idade = x):
    idade = 800
    x = 200
    print(x)
    print(f"Olá {nome}, sua idade é {idade}")

oi("Lucas")
print(x)

####################
import sys
#maxSize = sys.maxsize
#minSize = -sys.maxsize - 1

menor = sys.maxsize

a = int(input())
if a < menor:
    menor = a
    
a = int(input())
if a < menor:
    menor = a
    
a = int(input())
if a < menor:
    menor = a

print(menor)


import math
print(math.inf)
print(-math.inf)






