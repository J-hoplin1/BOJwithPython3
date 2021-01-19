import sys

a,b = map(int, sys.stdin.readline().split())



# b가 a보다 크다는 가정의 parameter
def getGCD(a,b):
    if b % a == 0:
        return a 
    else:
        return getGCD(b%a,a)

def getLCM(a,b):
    gcd = getGCD(a,b)
    return gcd * (a // gcd) * (b // gcd)

if a > b:
    gcd = getGCD(b,a) 
    lcm = getLCM(b,a)
else:
    gcd = getGCD(a,b)
    lcm = getLCM(a,b)

print(f'{gcd}\n{lcm}')
