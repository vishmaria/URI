'''verificar se conectores sao compativeis'''
conector1= input().split()
conector2= input().split()
for i in range(len(conector1)):
    if conector1[i]== conector2[i]:
        print('N')
        quit()
print('Y')