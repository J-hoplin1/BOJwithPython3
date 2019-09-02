num = int(input())

list_a = []
result = {}

for a in range(0, num):
    a,b = input().split(' ')
    result[a+ ' + '+b] = str(int(a) + int(b))
    list_a.append(result)
    result = dict()

for b in range(0, len(list_a)):
    print("Case #"+str(b+1)+':' + ' ' + list(list_a[b].keys())[0] + ' = ' + list(list_a[b].values())[0])
