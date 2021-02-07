import sys

def getLCM(n,m):
    GCD = getGCD(n,m)
    return GCD * (n // GCD) * (m // GCD)

def getGCD(n,m): # n < m이라는 가정
    if m % n == 0:
        return n
    else:
        return getGCD(m % n,n)

def solution(n, m):
    answer = None
    if n > m:
        answer= ([getGCD(m,n),getLCM(m,n)])
    else:
        answer = ([getGCD(n,m),getLCM(n,m)])
    return answer

if __name__=="__main__":
    n,m = map(int,sys.stdin.readline().split())
    print(solution(n,m))
