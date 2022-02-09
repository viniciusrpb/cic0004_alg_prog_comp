"""
Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
(8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
(7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar
, que horas chego em casa para o café da manhã?
"""

def calcula_tempo(km,minutos,segundos):
    total_tempo_s = ((minutos*60) + segundos)*km
    return total_tempo_s

#Entrada/Computacao
total_tempo_s = calcula_tempo(1,8,15)
total_tempo_s += calcula_tempo(3,7,12)
total_tempo_s += calcula_tempo(1,8,15)

horas,minutos = map(int,"6:52".split(":"))
segundos = (horas*3600) + (minutos*60)
total_tempo_s += segundos

horas = total_tempo_s//3600
minutos = (total_tempo_s%3600)//60
segundos = (total_tempo_s%3600)%60

print(f"Eu chego em casa para o café da manhã às {horas:02d}:{minutos:02d}:{segundos:02d}")


