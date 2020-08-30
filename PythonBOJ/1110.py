#10보다 작으면 앞에 0을 붙여 두자리 수로 만들고 각자리 숫자를 더한다.
global b
global value
global cycle

cycle = 0
value = -1

def add_zero(num):
    return "0" + num
#try:
a = int(input())
if a < 0 and a >= 99:
    exit()
#except TypeError:
#    exit()

while a != value:
    if cycle == 0:
        b = None
        b = str(a)
        if a < 10:
            b = add_zero(b)
    elif cycle != 0:
        b = str(value)
        if value < 10:
            b = add_zero(b)
    middle = int(b[0]) + int(b[1])
    final = str(b[1]) + str(middle)[-1]
    value = int(final)
    cycle += 1
print(cycle)
