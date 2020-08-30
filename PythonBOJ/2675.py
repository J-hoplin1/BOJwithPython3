cycle = int(input())

data = []
socket = []

cyc = 0
while cyc < cycle:
    a,b = input().split(' ')
    socket.append(int(a))
    socket.append(b)
    data.append(socket)
    socket = list()
    cyc += 1

fin = ''
for t in range(0, len(data)):
    for r in range(0, len(data[t][1])):
        fin += data[t][1][r] * data[t][0]
    print(fin)
    fin = ''