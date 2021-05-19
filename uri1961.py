
p,n = map(int,input().split())
alturas = [int(x) for x in input().split()]

for i in range(n-1):
    if abs(alturas[i]-alturas[i+1])> p:
        result = 'GAME OVER'
        break
    else:
        result ='YOU WIN'

print(result)