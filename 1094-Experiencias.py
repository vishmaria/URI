# #ChooseCrueltyFree
testes = int(input())
coelhos = 0
ratos = 0
sapos = 0

for i in range (testes):
	a = input().split()
		
	if a[1] == 'C':
		coelhos += int(a[0])
	elif a[1] == 'R':
		ratos += int(a[0])
	elif a[1] == 'S':
		sapos += int(a[0])


total = sapos+ratos+coelhos


print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format((coelhos/total)*100))
print("Percentual de ratos: {:.2f} %".format((ratos/total)*100))
print("Percentual de sapos: {:.2f} %".format((sapos/total)*100))
