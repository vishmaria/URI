x0, y0, x1, y1 = [int(n) for n in input().split()] #pontos no plano
x2, y2, x3, y3 = [int(n) for n in input().split()]
intersec = 0

if (x1 >  x2) and (y1 > y2):
    intersec = 1

print(intersec)
