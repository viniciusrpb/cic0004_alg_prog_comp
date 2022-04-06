m = int(input())

dd = {}
dd["x"] = 0
dd["y"] = 0

while m > 0:
    d,q = input().split()
    q = int(q)
    if d == "N":
        dd["y"] += q
    elif d == "S":
        dd["y"] -= q
    elif d == "L":
        dd["x"] += q
    elif d == "O":
        dd["x"] -= q
    m -= 1
n,s,l,o = 0,0,0,0
if dd["y"] >= 0:
    s = dd["y"]
else:
    n = dd["y"]*-1

if dd["x"] >= 0:
    o = dd["x"]
else:
    l = dd["x"]*-1

print(n,s,l,o)



    
