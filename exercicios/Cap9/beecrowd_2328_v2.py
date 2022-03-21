n = int(input())

lista = [int(x) for x in input().split()]

ans = 0
for i in range(0,n):
  ans+=lista[i]-1
print(ans)

  
