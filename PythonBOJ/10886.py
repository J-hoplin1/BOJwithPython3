'''
Code written by J-Hoplin
Date of creation :2019/09/13
URL :https://www.acmicpc.net/problem/10886
'''

io = int(input())

ck = [0,0]

for a in range(0, io):
    op = int(input())
    ck[op] += 1

if ck[0] < ck[1]:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
