
def calcula_desconto(valor_produto):
    print(f"O valor do produto com desconto de 9% é: R${valor_produto*0.91:.2f}")
    #return valor_produto*0.91

#Entranda
valor = float(input("Informe o valor do produto: "))

#Computacao
#valor_final = calcula_desconto(valor)
calcula_desconto(valor)

#Saida
#print(f"O valor do produto com desconto de 9% é: R${valor_final:.2f}")
