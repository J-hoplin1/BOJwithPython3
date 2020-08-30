'''
햄버거 3종류
음료 2종류

세트 -> 두개 가격 합친거 - 50
가장 싼 경우를 구하기
'''
import operator as op

mostCheapest = 0

burger = list()
total = list()

for e in range(3):
    i = int(input())
    burger.append(i)

checkSequence = [0 for a in range(len(burger))]

for t in range(2):
    p = int(input())
    checkSequence = [p-50 for a in range(len(burger))]
    t = map(op.add,checkSequence,burger)
    total += t

print(min(total))
