import math
a,b = map(int,input().split())
for b in range(a,b + 1):
    if b == 1:
        continue
    if b == 2:
        print(b)
    else:
        boolT = True
        for c in range(2,int(math.sqrt(b)) + 1): # 제곱근을 통해서 나누어지는 수 검사를 줄인다. 왜냐? 수가 많아질수록 for문이 도는 속도는 더 길어지기 때문
            if b % c == 0:
                boolT = False
                break
            else:
                continue
        if boolT == True:
            print(b)
        else:
            continue