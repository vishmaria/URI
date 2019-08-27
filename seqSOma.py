while True: ##while porque a qtd é indefinida
    try:
        x, y = input().split()
        x, y = int(x),int (y)
        if x <= 0 or y <= 0: ##o programa finaliza quando recebe negativo ou 0
            break

        troca = 0 #variavel vazia para colocar os valores em ordem crescente
        if x > y:
            troca = x
            x = y
            y = troca

        soma = 0 #variavel para acumular
        result = '' #string vazia que sera a impressao do resultado
        while x <= y:
            result += str(x) + ' ' #converter x para string para ser impressa no resultado
            soma += x
            x += 1
        result += 'Sum=%d'
        print(result %soma)

        #outra forma:
        #print (soma, end = "")

    except:
        break
