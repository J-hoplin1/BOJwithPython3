totalLine = int(input())

for e in range(1,totalLine * 2):
    if e <= totalLine:
        print('*' * e)
    else:
        print('*' * (totalLine - (e - totalLine)))
