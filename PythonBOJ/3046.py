from typing import Any
import sys

'''
URL : https://www.acmicpc.net/problem/3046

R1 , R2 의 평균 s

r1 s가 주어졌을때 r2 구하기;


'''

datas = list(map(int, sys.stdin.readline().split()))

print((datas[-1] * 2) - datas[0])
