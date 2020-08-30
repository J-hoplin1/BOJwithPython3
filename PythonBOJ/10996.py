
#입력값
n = int(input())

if n == 1:
    print('*')
else:
    firstLineStars = 0
    secondLineStars = 0
    if n %2 != 0:
        firstLineStars = int(n // 2) + 1
        secondLineStars = int(n // 2)
    else:
        firstLineStars = int(n // 2)
        secondLineStars = int(n // 2)
    for t in range(1,n + 1):
        print('* ' * firstLineStars)
        print(" *" * secondLineStars)