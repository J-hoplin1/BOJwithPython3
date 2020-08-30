'''
Code written by J-Hoplin
Date of creation : 2020/01/02
URL : https://www.acmicpc.net/problem/2108
'''

import sys
#산술평균 : N개의 수들의 합을 N으로 나눈 값
#중앙값 : N개의 수들을 증가하는 순서대로 나열때 중앙값
#최빈값 : 가장 많이 나타나는값
#범위 : 최대최소 차이
s=sys.stdin.readline
total_count = int(s())

values = []
data = dict()
total_sum = 0

# 값받기
for a in range(0, total_count):
    val = int(s())
    total_sum += val
    values.append(val)
    if val in data.keys():
        data[val] += 1
    else:
        data[val] = 1

# 중복요소 제거
set_total_count = list(set(values))
# 정렬
sort_values = sorted(values)

data_key = list(data.keys())
data_values = list(data.values())
#산술평균
print(round(total_sum / total_count))

#중앙값
print(sort_values[int(total_count / 2)])

#최빈값
appear_count = sorted(data.values())
result_val = []
for d in range(len(data_key)):
    if data[data_key[d]] == appear_count[-1]:
        result_val.append(data_key[d])
if len(result_val) == 1:
    print(result_val[0])
if len(result_val) > 1:
    result_val.sort()
    print(result_val[1])
#범위
print(max(values) - min(values))