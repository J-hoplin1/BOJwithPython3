from string import ascii_uppercase, ascii_lowercase

li = list(ascii_uppercase)
dit = {}

for a in range(0,len(li)):
    dit[li[a]] = 0

io = list(input().upper())

for b in range(0, len(io)):
    dit[io[b]] += 1

op = list(dit.values())
if op.count(max(list(dit.values()))) > 1:
    print('?')
else:
    for k,v in dit.items():
        if v == max(list(dit.values())):
            print(k)
        else:
            pass




