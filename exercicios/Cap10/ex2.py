n = int(input())

dd = {}
while n > 0:
    p,s,d = input().split()
    d = int(d)
    dd[s] = d
    n -= 1

"""
for item in sorted(dd.items(),reverse=True,key=lambda x: x[1]):
    print(item[0],end="")
"""

print("".join(i[0] for i in sorted(dd.items(),reverse=True,key=lambda x: x[1])))
