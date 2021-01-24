'''
직각삼각형 -> 가장 긴 변의 제곱 = 나머지 두 수의 제곱 더한값
'''
import sys
import math

while True:
    vals = sorted(list(map(int,sys.stdin.readline().split())))
    if sum(vals) == 0:
        break
    else:
        if math.pow(vals[-1],2) == sum([math.pow(t,2) for t in vals[:2]]):
            print('right')
        else:
            print('wrong')
