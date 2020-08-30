result = []
li = []

io = int(input())
score = 0

for a in range(0, io):
    op = input()
    for y in range(0, len(op)):
        li.append(0)
    for b in range(0, len(op)):
        if b == 0:
            if op[b] == 'O':
                score += 1
                li[b] = score
            elif op[b] == 'X':
                pass
        else:
            if op[b] == 'O':
                score += 1
                li[b] = score
            elif op[b] == 'X':
                score = 0
                li[b] = 0
    result.append(li)
    li = list()
    score = 0

for r in range(0, len(result)):
    nr = 0
    for e in range(0, len(result[r])):
        nr += result[r][e]
    print(nr)