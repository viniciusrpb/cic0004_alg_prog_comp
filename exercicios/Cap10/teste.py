"""
tt = 1,2,3,4,5
ll = [1,2,3,4,5]

def mudaLista(lista):#lista = ll
    lista.append(6)

def mudaTupla(tupla):#tupla = tt
    print(tupla)
    tupla = 10
    print(tupla)

#mudaLista(ll)
print(tt)
mudaTupla(tt)
print(tt)
"""

dd = {}
dd["Zezinho"] = [31,7]
dd["Lucas"] = [31,10]
dd["Arthur"] = [21,7]
dd["Joao"] = [23,9]


def sortLucas(item):
    return -item[1][0],item[0]

#for item in sorted(dd.items(),key=lambda x: (-x[1][0],x[0])):
for item in sorted(dd.items(),reverse=False,key=sortLucas):
    print(item)





    
    