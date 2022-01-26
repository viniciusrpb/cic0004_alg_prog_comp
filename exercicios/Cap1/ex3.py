#Se você correr X (entrada do usuário) quilômetros em Y (entrada do usuário)
#minutos e Z (entrada do usuário) segundos,
#qual é o seu passo médio (tempo por milha em minutos e segundos)?
#Qual é a sua velocidade média em milhas por hora?

#Entrada
km = float(input("São quantos quilômetros você correu: "))
minutos = int(input("Em quantos minutos: "))
segundos = int(input("Em quantos segundos: "))

#Computacao
#Solução: Pedro Victor Roriz
milhas = km/1.61
totalsegundos = (minutos * 60) + segundos
hora = totalsegundos/3600
velocidade = milhas/hora

#Solução: Arthur Torsani
#velocidade= (km / 1.61) / (( minutos + (segundos / 60)) / 60)

#Saida
print(f"A velocidade média em milhas por hora é: {velocidade}")