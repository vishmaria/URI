testes = int(input())


for i in range (testes):
    op = input().split()

    if '+' in op:

        r = int(op[0]) + int(op[2])
    elif '-' in op:

        r = int(op[0]) - int(op[2])
    else:

        r = int(op[0]) * int(op[2])

    dist = abs(int(op[4]) - r)
    print ("E" + ('r' * dist ) + "ou!")