notas = [float(x) for x in input().split()]
notas.sort()
nf = sum(notas) - notas[0] - notas[-1]
print("{:.1f}".format(nf))