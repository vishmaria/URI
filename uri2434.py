"""dias, saldo = [int(n) for n in input().split()]
saldos = []

for _ in range (dias):
    movimentacao = int(input())
    saldo += movimentacao
    saldos.append(saldo)

print(min(saldos))"""
dias, saldo = [int(n) for n in input().split()]
min = saldo

for _ in range (dias):
    movimentacao = int(input())
    saldo += movimentacao
    if saldo <= min:
        min = saldo

print(min)
