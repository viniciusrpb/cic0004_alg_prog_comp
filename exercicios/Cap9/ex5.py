#Crie uma função ehPrimo(n) que retorna 0 se o número for primo e 1 caso não seja

def ehPrimo(n):
    if n == 2:
        return 1
    if n%2 == 0 and n != 0:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
        
n = int(input())
l = [i for i in range(2,n) if n%i == 0]
if not l:
    print(f"O número {n} é primo!")
else:
    print(f"O número {n} NÃO é primo!")    