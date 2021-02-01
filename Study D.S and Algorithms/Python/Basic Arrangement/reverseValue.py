from typing import MutableSequence,Any

def reverse_array(a:MutableSequence) -> None:
    n = len(a)
    
    for i in range(n // 2):
        a[i], a[(n-1) - i] = a[(n-1) - i],a[i]
        
if __name__=="__main__":
    print("배열 원소를 역순으로 만든다.")
    num = int(input('원소수를 입력하기 : '))
    
    x = [None] * num
    
    for t in range(num):
        x[t] = int(input(f'x[{t}]값 입력하기 : '))
    
    reverse_array(x)
    
    print("역순정리 완료.")
    
    for e in range(num):
        print(f'x[{e}] = {x[e]}')

        
'''
파이썬에는 뮤터블 객체를 역순으로 정렬하는 두가지 내장 메소드가 존재한다.

1) reverse()

(리스트).reverse

2) list(reversed(리스트))
'''