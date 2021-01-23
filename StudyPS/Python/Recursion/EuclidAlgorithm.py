'''
8 * 22의 크기를 가진 직사각형이 있다고 가정하자. 이 직사각형 내부를 정사각형으로 채워나갈때 가장 작게 만들수 있는 정사각형의 변 길이는?

-> 가장 작은 변을 기준으로 정사각형을 만든다

(8x8) x 2 + (8x6) x 1

-> 여기서 유일한 직사각형인 (8x6)에 대해 다시 정사각형으로 분할하면

(6x6) x 1 + (6x2) x 1

-> 위와 동일한 방법으로 지속해서 정사각형으로만 이루어지는 경우까지 간다.

(2x2) x 3

결론은 2이다.

이 원리를 이용하면 두 수간의 최대공약수 GCD(Great Common Divisor)를 구할 수 있다.

추가적으로 두 수의 최소 공배수는 두수를 각각 GCD로 나눈 후에 그 수들과 GCD를 곱한 값이다.
'''

import sys

# 여기서 y가 x보다 크다는 가정을 가진다.
def gcd(x,y):
    if y % x == 0:
        return x
    else:
        return gcd(y % x, x)

x,y = map(int,sys.stdin.readline().split())

if x > y:
    print(f'두 수의 최대공약수 : {gcd(y,x)}')
else:
    print(f'두 수의 최대공약수 : {gcd(x,y)}')
