while True:
    try:
        frase = input().upper().split('-')
        print(frase)
        p = 'COBOL'
        for i in range(len(frase)):
            if 'C' in frase[i]or 'O'*2 in frase[i] or 'B' in frase[i] or 'L' in frase[i]: 
                r = ("GRACE HOPPER")
                
            else:
                r = ("BUG") 
        print(r) 
    except EOFError:
        break
    
