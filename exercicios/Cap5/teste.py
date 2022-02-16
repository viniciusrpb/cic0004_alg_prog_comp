
def fat(x):
    if x <= 1:
        return 1
    elif x == 2:
        return 2
    else:
        return x*fat(x-1)
    

print(fat(int(input())))