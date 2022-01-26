#Quantos segundos há em X (entrada do usuário) minutos e
#Y (entrada do usuário) segundos?

#Entrada
minutos = int(input("São quantos minutos: "))
segundos = int(input("São quantos segundos: "))

#Computacao
result = (minutos * 60) + segundos


#Saida
print(f"Em {minutos} minutos e {segundos} segundos temos {result} segundos")
