P = int(input())

for y in reversed(range(1,P + 1)):
    print(' ' * (P - y) + '*' * ((2 * y)-1))
for w in range(2,P+1):
    print(' ' * (P - w) + '*' * ((2 * w) - 1))
