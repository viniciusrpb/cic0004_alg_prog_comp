import math

def ler_maior(n, maior = -math.inf,primeiro = None):
    """
    Essa função ler n numeros e retorna o maior deles e o primeiro lido
    n => Quantidade de numeros q ele ta lendo
    """
    if n == 0:
        return maior,primeiro
    else:
        a = int(input())
        
        if primeiro == None:
            primeiro = a
        
        if a > maior:
            maior = a
        return ler_maior(n-1, maior,primeiro)
        


maior, primeiro = ler_maior(2)
print(maior)
if maior%primeiro == 0:
    print(primeiro)
    



    