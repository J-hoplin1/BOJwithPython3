'''
Code written by J-Hoplin
Date of creation : 2019/09/23
URL : https://www.acmicpc.net/problem/10814
'''
dic = {}

count = int(input())

for c in range(0, count):
    a, b = input().split(' ')
    a = int(a)
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)

ages = list(dic.keys())
ages = sorted(ages)

for d in ages:
    for e in dic[d]:
        print(d, e)


