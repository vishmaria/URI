digitoFalho = None
negociacao = None

while digitoFalho != '0' and negociacao != '0': 
    digitoFalho, negociacao = input().split()

    correcao = int(negociacao.replace(digitoFalho, ''))
    print(correcao)

