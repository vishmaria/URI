jogadores = int(input())
saques, bloqueios, ataques, pSaque, pBloq, pAtaque =[0, 0, 0, 0, 0, 0] #adiconando 6 posicoes para armazenar jogadas e pontos

for i in range (jogadores):
    nome = input()
    n, n1, n2 = list(map(int, input().split())) #adicionando valores a lista
    saques += n
    bloqueios += n1
    ataques += n2
    n3, n4, n5 = list(map(int, input().split())) #adicionando jogadas que pontuaram
    pSaque += n3
    pBloq += n4
    pAtaque += n5


print('Pontos de Saque: {:.2f} %.'.format((pSaque / saques)*100))
print("Pontos de Bloqueio: {:.2f} %.".format((pBloq / bloqueios)*100))
print("Pontos de Ataque: {:.2f} %.".format((pAtaque / ataques)*100))
