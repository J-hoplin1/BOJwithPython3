num = int(input())

result = []

for a in range(0, num):
    a,b = input().split(' ')
    result.append(int(a) + int(b))

for b in range(0, num):
    print(result[b])