

t = int(input())
while t > 0:
    a,n = input().split()
    a,n = [int(a), int(n)]
    soma = 0
    while n > 0:
        soma += a
        print(a,end=" ")
        a += 1
        n-=1
    print(f"\n{soma}")
    t -= 1

