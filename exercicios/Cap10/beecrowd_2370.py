'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
 
Tópico: Dicionários e Tuplas (Python)
Objetivo: Solução do problema beecrowd 2370 - Times
          https://www.beecrowd.com.br/judge/en/problems/view/2370
 
Linha de comando para executar: python3 beecrowd_2370.py
'''

n,t = (int(x) for x in input().split())

atletas = {}

for i in range(0,n):
    nome,habilidade = input().split()
    habilidade = int(habilidade)
    
    # cria uma entrada no dicionario atletas
    atletas[habilidade] = nome

# ordenacao do dicionario em relação às chaves em ordem decrescente
atletas_sorted = {}

for chave in sorted(atletas,reverse=True):
    atletas_sorted[chave] = atletas[chave]

times = {}
for i in range(0,t):
    times[i] = []

ind_time = 0 
for hab in atletas_sorted:
    nome_atleta = atletas_sorted[hab]
    
    times[ind_time].append(nome_atleta)
    ind_time+=1
    if ind_time == t:
        ind_time = 0
    
for time in times:
    
    #ordena em ordem alfabetica os nomes dos jogadores para cada time
    times[time].sort()

    print(f'Time {time+1}')
    for atleta in times[time]:
        print(atleta)
    print()
