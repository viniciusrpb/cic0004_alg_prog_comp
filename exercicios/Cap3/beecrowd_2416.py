'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Algoritmos Sequenciais (Python)
Objetivo: Solução do problema beecrowd 2416 - Corrida (OBI - Olimpíada Brasileira de Informática 2012)
          https://www.beecrowd.com.br/judge/en/problems/view/2416
 
Linha de comando para executar: python3 beecrowd_2416.py
'''

c,n = input().split()
c = int(c)
n = int(n)

ans = c%n

print(f'{ans}')
