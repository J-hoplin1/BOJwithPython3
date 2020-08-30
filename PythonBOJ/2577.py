A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_a = str(result)

count = []
num = 0


for p in range(0, 10):
    count.append(0)
for a in range(0,len(result_a)):
    for b in range(0, 10):
        if int(result_a[a]) == b:
            count[b] += 1
            break
        else:
            pass

for t in range(0, len(count)):
    print(count[t])

