lado = int(input())
cont = 0

#contando quantas vezes pode quebrar o chocolate
while lado >= 2:
    lado /= 2
    cont += 1

print (4**cont)


 
