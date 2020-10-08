convertDict = ['c=','c-','dz=','d-','lj','nj','s=','z=']

inp = input()

for e in convertDict:
    inp = inp.replace(e, '*')

print(len(inp))