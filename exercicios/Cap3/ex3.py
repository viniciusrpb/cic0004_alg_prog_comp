
def calcula_desconto(nome_produto, valor_produto, des):
    des = 1-(des/100)
    print(f"O valor do {nome_produto} com desconto é: {valor_produto*des:.2f} R$")

#Entranda
produto = input("Informe o nome do produto: ")
valor = float(input("Informe o valor do produto: "))
desconto = float(input("Informe o desconto: "))

#Computacao
calcula_desconto(produto,valor, desconto)


