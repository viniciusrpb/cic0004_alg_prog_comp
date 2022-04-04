'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Listas (Python)
Objetivo: Solução do problema beecrowd 1318 - Fake Tickets
          https://www.beecrowd.com.br/judge/en/problems/view/1318
 
Linha de comando para executar: python3 beecrowd_1318.py
'''

n,m = (int(x) for x in input().split())

while n > 0 and m > 0:

  tickets = [int(x) for x in input().split()]

  histograma = {}

  for ticket in tickets:

    if ticket in histograma:
      histograma[ticket]+=1
    else:
      histograma[ticket]=1

  ans = 0
  for ticket in histograma:
    if histograma[ticket] > 1:
      ans+=1

  print(ans)

  n,m = (int(x) for x in input().split())
  
