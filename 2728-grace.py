while True:
    try:
        frase = input().upper().split('-')
        verifica=['C','O','B','O','L']
        for palavra in frase:
            for i in verifica:
                if i in palavra:
                    verifica.remove(i)

        if verifica==[]:
            print("GRACE HOPPER")
        else:
            print("BUG")


    except EOFError:
        break
