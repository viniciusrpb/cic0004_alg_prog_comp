
def fatorial(n):
  if n == 1:
    return 1,0

  fatn_1,c = fatorial(n-1)
  return fatn_1*n,c+1

n = int(input())
ans,cham = fatorial(n)

print(ans)
print(cham)