from string import ascii_lowercase
li = list(ascii_lowercase)
io = input()
fin = []
for p in range(0, len(li)):
    fin.append(0)
checked = []
ck = []
for a in range(0, len(io)):
    if io[a] in checked:
        pass
    else:
        checked.append(io[a])
        ind = li.index(io[a])
        fin[ind] = a
for t in range(0,len(fin)):
    fin[t] = str(fin[t])
for r in range(0,len(li)):
    if li[r] not in checked:
        fin[r] = str(-1)
empty = ""
for r in range(0, len(fin)):
    empty += fin[r]
    empty += ' '
print(empty)

