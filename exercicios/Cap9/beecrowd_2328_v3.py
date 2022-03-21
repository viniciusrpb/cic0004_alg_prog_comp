n = int(input())

lista = [int(x) for x in input().split()]

ans = 0
for elem in lista:
  ans += elem-1
print(ans)

  
