
'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Listas (Python)
Objetivo: Solução do problema beecrowd 1259 - Even or Odd
          https://www.beecrowd.com.br/judge/en/problems/view/1259
 
Linha de comando para executar: python3 beecrowd_1259.py
'''

n = int(input())

pares = []
impares = []

while n > 0:
  
  x = int(input())

  if x % 2 == 0:
    pares.append(x)
  else:
    impares.append(x)

  n-=1

pares.sort()
impares.sort(reverse=True)

for i in range(0,len(pares)):
  print(pares[i])

for i in range(0,len(impares)):
  print(impares[i]) 
