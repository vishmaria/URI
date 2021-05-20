nao_repetidos = [] #cria uma lista vazia p/ comparação
nListas = int(input())

for i in range (nListas):
    lista = input().split()
    for entrada in lista:
        if entrada not in nao_repetidos:
            nao_repetidos.append(entrada)
    for x in sorted(nao_repetidos):
        print(x, end=" ") 

    nao_repetidos = []   
      
        
