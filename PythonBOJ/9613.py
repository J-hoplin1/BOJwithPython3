import sys
import itertools as it

def gcd(x,y):
    if y % x == 0:
        return x
    else:
        return gcd(y % x,x)

count = int(sys.stdin.readline())

for r in range(count):
    totalGCDSum = 0
    inp = list(map(int,sys.stdin.readline().split()))
    nums = inp[1:]

    for i in list(it.combinations(nums,2)):
        totalGCDSum += gcd(i[0],i[1])
    print(totalGCDSum)
