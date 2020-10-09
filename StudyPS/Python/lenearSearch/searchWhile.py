'''
선형 검색의 종료조건

1) 검색할 값을 찾지 못하고 배열의 맨 끝을 지나간 경우
2) 검색할 값과 같은 원소를 찾는 경우

'''

from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int: 
    
    ''' sequence a 에서 key와 값이 같은 원소를 선형 검색한다. '''
    
    i = 0
    while True:
        if i == len(a):
            return -1 #실패시 -1반환
        if a[i] == key:
            return i 
        i += 1
        
if __name__=="__main__":
    num = int(input('원소수 입력하기 : '))
    x = [None] * num
    
    for e in range(num):
        x[e] = int(input(f'x[{e}] : '))
    
    key = int(input('검색할 값 입력하기 : '))
    
    ind = seq_search(x,key)  
    
    if ind == -1:
        print('검색하려는 값 존재하지 않음')
    else:
        print(f'검색하려는 값 x[{ind}]')