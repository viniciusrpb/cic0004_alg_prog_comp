#Tá vendo

frase = input()
soma = 0
flag = False
for i in frase:
    if i.isspace():
        soma += 1
        flag = True
    else:
        if flag:
            if soma == 1:
                print(0)
            else:
                print(soma-2)
            soma = 0
            flag = False
        


        
    
        
        
        