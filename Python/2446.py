totoalLine = int(input())
maxStars = ((totoalLine-1) * 2) + 1


for e in range(1,totoalLine * 2):
    if e <= totoalLine:
        typeStars = (totoalLine - e) * 2 + 1
        typeBlank = int((maxStars - typeStars) // 2)
        print(' ' * typeBlank + '*'* typeStars)
    else:
        typeStars = (e - totoalLine) * 2 + 1
        typeBlank = int((maxStars - typeStars) // 2)
        print(' ' * typeBlank + '*' * typeStars)
