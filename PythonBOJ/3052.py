li = []

for a in range(0,10):
    io = int(input())
    li.append(io)

for b in range(0,10):
    li[b] = li[b] % 42

li = set(li)
print(len(li))