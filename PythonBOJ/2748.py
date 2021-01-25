N = int(input())


def fibo(x,y,loop):
    if loop == N:
        return y
    else:
        return fibo(y,x + y,loop + 1)

print(fibo(0,1,1)) # 피보나치 0번째 피보나치 수는 0, 1번째 피보나치 수는 1이다.
# y매개변수에 들어가는 수는 loop번째의 수를 의미한다.
