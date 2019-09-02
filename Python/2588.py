a = input()
b = input()

p = len(b) - 1
o = 0

result = 0
while p >= 0:
    y = int(a) * int(b[p])
    print(y)
    num = str(y) + '0' * o
    result += int(num)
    p -= 1
    o += 1
print(result)
