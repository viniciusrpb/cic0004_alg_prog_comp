'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Estruturas Condicionais e Recursividade (Python)
Objetivo: Solução do problema beecrowd 1153 - Fatorial Simples
          https://www.beecrowd.com.br/judge/en/problems/view/1153
 
Linha de comando para executar: python3 beecrowd_1153.py
'''

def fatorial(n):
  # Criterio de parada
  if n == 1:
    return 1
  
  # Termo principal da recursao:
  # onde faco a chamada recursiva
  return n*fatorial(n-1)

n = int(input())
print(fatorial(n))
