'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Listas (Python)
Objetivo: Solução do problema beecrowd 1168 - LED
          https://www.beecrowd.com.br/judge/en/problems/view/1168
 
Linha de comando para executar: python3 beecrowd_1168.py
'''

n = int(input())

leds = {'0':6, '1':2, '2': 5, '3':5, '4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

while n > 0:

  number = input()

  ans = 0
  for carac in number:
    ans=ans+leds[carac]

  print(f'{ans} leds')

  n-=1

