#파이썬의 .sort()메소드는 기본적으로 퀵정렬을 기본으로 한다고 한다.
io = int(input())
inp = []
for a in range(0,io):
    soc = int(input())
    inp.append(soc)
inp.sort()
for b in range(0,len(inp)):
    print(inp[b])
