from typing import Any, Sequence

'''
Any : Any는 제약이 없는 임의의 자료형을 의미한다.

Sequence : 시퀸스형을 의미한다. 시퀸스형에는 리스트형 , 바이트배열형 ,  문자열형 ,  튜플(immutable 자료형)형 바이트형이 있다.

함수 어노테이션( -> )
파이썬은 문법의 제약성이 적어 유연하다. 하지만 파이썬은 변수를 자료형 선언없이 함에 있어서 명시적으로 해석하기 어려운 경우도 있다.
그렇기 때문에 이를 방지하기 위해 어노테이션이 있는것이다. 어노테이션은 코드에 어떠한 영향을 미치지 않는다.
어노테이션은 '함수의 매개변수와 반환값을 나타내는 역할을 한다.'
여기서는 -> Any이므로, 반환하는것은 임의의 자료형이라는 의미를 가지고 있다.
'''

def max_of(a:Sequence) -> Any:
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__=="__main__":
    print("배열의 최댓값을 구합니다.")
    num = int(input("원소의 개수를 입력하세요 : "))
    x = [None] * num
    
    for t in range(num):
        x[t] = int(input(f"x[{t}]값을 입력하세요 : "))
        
    print(f'최댓값은 {max_of(x)}입니다.')