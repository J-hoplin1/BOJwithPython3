'''
운영체제 수업 -> 전 학생의 중간고사 기말고사 과제점 점수를 만점 기준 300점 환산

A+: 1~5등
A0: 6~15등
B+: 16~30등
B0: 31~35등
C+: 36~45등
C0: 46~48등
F: 49~50등

학점출력

'''

import sys

#scores -> list
scores = list(map(int, sys.stdin.readline().split()))
findData = int(input())

# Reverse score : 내림차순정렬을 통해 가장 높은 점수가 front index에 있도록
scores.sort(reverse = True)
#Get index of finding data
findIndex = scores.index(findData) + 1

if findIndex <= 5:
    print('A+')
elif findIndex <= 15:
    print('A0')
elif findIndex <= 30:
    print('B+')
elif findIndex <= 35:
    print('B0')
elif findIndex <= 45:
    print('C+')
elif findIndex <= 48:
    print('C0')
else:
    print('F')
