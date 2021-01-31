'''
보초법

선형 검색 알고리즘에서 종료조건은 두가지가 존재한다.

1) 검색할 값을 찾지 못하고 배열의 맨 끝을 지나갔는가? -> 검색실패조건

2) 검색할 값과 같은 원소를 찾았는가? -> 검색 성공 조건

종료를 위해 이 두가지를 항상 검색하는데, 이 과정을 계속해서 반복하다 보면 종료조건을 검사하는 '비용(cost)'를 무시할 수 없다.

우선 기본적으로 검색 대상인 sequence가 있다면 그 sequence 맨 끝에는 검색하고자 하는 key값을 넣어준다.
여기서 sequence맨 끝에 넣어주는 이 검색하려는 key값을 '보초'라고 한다.

만약 원래 seqeunce에 자신이 찾으려는 key값이 존재하지 않는다면, 스캔 인덱스는 원래 sequence의 길이와 동일해 질 것이다.
반대로 원래 sequence에 자신이 찾으려는 key가 존재한다면, 원래 sequence보다 작은 값이 될것이다.

이런 방식을 이용하면, 위의 두가지 방법중, 1)을 검사할 필요가 없고, 2)의 방법만으로 종료조건 판단을 할 수 있어, 비용이 줄어들게 된다.

사실 copy.deepcopy()가 깊은 복사로 효율성이 그리 좋지 않아 이진검색이 더 

'''

from typing import Any, Sequence
import copy

def seq_search(seq:Sequence,key : Any) -> int:
    
    a = copy.deepcopy(seq) #Sequence seq에 대한 깊은 복사를 해준다.
    a.append(key) #깊은 복사를 한 sequence 뒤에 key값을 append해준다
    
    i = 0
    while True:
        if a[i] == key:
            break
        i+=1
    return -1 if i == len(seq) else i #스캔 인덱스 i가 만약 원래 sequence길이값과 동일한 값을 가지면, 검색 실패이므로, 실패란 의미인 -1을 반환, 아닌경우는 스캔인덱스 i 반환

if __name__=="__main__":
    num = int(input("원소 수를 입력하세요 : "))
    x = [None] * num
    
    for e in range(num):
        x[e] = int(input(f'x[{e}] : '))
    
    key = int(input('검색할 값 입력하기 : '))
    
    idx = seq_search(x,key) 
    
    if idx == -1:
        print("검색하려는 원소 존재하지 않음")
    else:
        print(f'검색하려는 원소는 x[{idx}]에 존재합니다.')
