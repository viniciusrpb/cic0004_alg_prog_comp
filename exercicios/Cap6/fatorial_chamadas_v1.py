
def fatorial(n,cham):
  if n == 1:
    return 1,cham

  fatn_1,c = fatorial(n-1,cham+1)
  return fatn_1*n,c

n = int(input())
ans,cham = fatorial(n,0)

print(ans)
print(cham)