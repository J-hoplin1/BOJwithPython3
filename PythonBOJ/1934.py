from typing import Any

'''
A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수

A,B의 최소공배수 구하기

'''
#유클리드 호제법을 사용한다.
#b가 a보다 큰 수라는 가정

# 결론적으로 두 수의 최소 공배수는 두 수의 곱  // 최대 공약수
def getGCD(a,b):
    if b % a == 0:
        return a
    else:
        return getGCD(b%a,a)

def getLCM(a,b) -> int:
    gcd = getGCD(a,b)
    return a * b // gcd

testCase = int(input())
result = []
for e in range(testCase):
    a,b = input().split()
    if int(a) > int(b):
        result.append(getLCM(int(b),int(a)))
    else:
        result.append(getLCM(int(a),int(b)))

for e in result:
    print(e)
