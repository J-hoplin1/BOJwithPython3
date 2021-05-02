import sys


# 하노이의 탑에서 최소 이동 횟수는 2의 n승 -1번이다.
N = int(sys.stdin.readline())
def hanoi(floor,a,b,c):
    if floor == 1:
        print(f'{a} {c}')
    else:
        hanoi(floor - 1,a,c,b)
        print(f'{a} {c}')
        hanoi(floor -1, b,a,c)

print(pow(2,N) - 1)
if N <= 20:
    hanoi(N,1,2,3)
