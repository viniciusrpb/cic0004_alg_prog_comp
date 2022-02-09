
def calcula_desconto(nome_produto, valor_produto):
    print(f"O valor do {nome_produto} com desconto é: {valor_produto*0.91:.2f} R$")

#Entranda
produto = input("Informe o nome do produto: ")
valor = float(input("Informe o valor do produto: "))

#Computacao
calcula_desconto(produto,valor)

