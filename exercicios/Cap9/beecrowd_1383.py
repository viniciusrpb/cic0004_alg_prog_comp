
'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Listas - Matrizes (Listas de listas) (Python)
Objetivo: Solução do problema beecrowd 1383 - Sudoku
          https://www.beecrowd.com.br/judge/pt/problems/view/1383
 
Linha de comando para executar: python3 beecrowd_1383.py
'''

def lematriz(n):

  matriz = []

  for i in range(0,n):
    matriz.append([int(x) for x in input().split()])

  return matriz

def imprimeMatriz(m):

    string = ""

    for i in range(0,len(m)): # 2
        linha = ""
        for j in range(0,len(m[i])-1):
            linha+=str(m[i][j])+" "
        linha+=str(m[i][j+1])+"\n"
        string+=linha

    return string

n = int(input())

while n > 0:

  m = lematriz(9)

  print('\n\n')
  print(imprimeMatriz(m))

  
  
  n-=1
