io = input()
to_li = []
for a in range(0, len(io)):
    to_li.append(int(io[a]))
p = list(reversed(sorted(to_li)))
bla = ""
for b in range(0, len(p)):
    bla += str(p[b])
print(bla)