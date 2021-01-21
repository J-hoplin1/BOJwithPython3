'''
재귀(Recursion) : 이벤트에서 자기 자신을 포함하고 다시 자기 자신을 이용해 정의되는 경우를 의미한다.

팩토리얼 : 양의 정수를 순서대로 곱하기에 순차 곱셈이라고도 부른다.

N! = N * (N-1) * ...... * 1

10! = 10 * 9!
    = 10 * 9 * 8!
    ....etc
'''

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

if __name__ == "__main__":
    n = int(input("팩토리얼 계산 : "))
    print(f'Result : {factorial(n)}')
