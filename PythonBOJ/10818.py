li = []

a = int(input())
o = input()
u = o.split(' ')
for b in range(0, a):
    li.append(int(u[b]))
li.sort()
print(str(li[0]),str(li[-1]))