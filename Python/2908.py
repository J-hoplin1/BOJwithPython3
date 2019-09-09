a = input().split(' ')
for c in range(0, len(a)):
    a[c] = int(a[c][::-1])
print(max(a))