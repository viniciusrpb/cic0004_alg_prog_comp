'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Funções com Resultado e Recursividade (Python)
Objetivo: Solução do problema beecrowd 2166 - Square Root of 2
          https://www.beecrowd.com.br/judge/en/problems/view/2166
 
Linha de comando para executar: python3 beecrowd_2166.py
'''

def solve(a):

  if a == 0:
    return 0
  
  resp = 1/(2 + solve(a-1))
  return resp

n = float(input())
ans = 1+solve(n)
print("{:.10f}".format(ans))
