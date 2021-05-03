digitoFalho = ''
negociacao = ''
while  digitoFalho != '0' and negociacao != '0': 

    digitoFalho, negociacao = input().split()

    negociacao = "0" + negociacao
    correcao = int(negociacao.replace(digitoFalho, ''))
    print(correcao)
