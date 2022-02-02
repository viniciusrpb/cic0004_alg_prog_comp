"""
Suponha que o preço de capa de um livro seja R$ x (entrada do usuário), mas as livrarias
recebem um desconto de x (entrada do usuário). O transporte custa R$ x (entrada do usuário)
para o primeiro exemplar e x (entrada do usuário) centavos para cada exemplar adicional.
Qual é o custo total de atacado para x (entrada do usuário) cópias?
"""

#Entrada
preco_livro = float(input("Informe o valor do livro(R$): "))
desconto = float(input("Informe o valor do desconto(%): "))
transporte = float(input("Informe o valor do transporte do primeiro livro(R$): "))
transporte_a = float(input("Informe o valor do transporte do demais(R$): "))
copias = int(input("Informe a quantidade de cópias: "))

#Computacao
custo_total_transporte = ((copias-1)*transporte_a)+transporte
preco_livros = preco_livro*copias
custo_total_livros = preco_livros-(preco_livros*desconto/100)

valor_total = custo_total_transporte + custo_total_livros

#Saida
print(f"O custo total de atacado para {copias} cópias é: R${valor_total:.2f}")
