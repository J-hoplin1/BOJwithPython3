import sys
#문제 ㄹㅇ 역겹다

Ndict = {
    0 : [],
    1 : [1],
    2 : [2,4,8,6],
    3 : [3,9,7,1],
    4 : [4,6],
    5 : [5],
    6 : [6],
    7 : [7,9,3,1],
    8 : [8,4,2,6],
    9 : [9,1]
}

testCase = int(input())
for _ in range(testCase):
    a,b = map(int, sys.stdin.readline().split())
    a = a % 10 # a의 범위는 다음과 같다.1 <= a <= 100
    if a == 0:
        print(10)
    elif a==5 or a == 1 or a == 6:
        print(a)
    else:
        print(Ndict[a][b % len(Ndict[a]) -1 ])
