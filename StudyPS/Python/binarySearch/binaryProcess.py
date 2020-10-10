from typing import Any, Sequence 

def binSearch(a:Sequence, key : Any) -> int: 
    
    pl = 0
    pr = len(a) - 1
    
    print('    |',end='')
    for i in range(len(a)):
        print(f'{i:4}',end='') # {a : b} : 나타낼 값 a를 b자리수에 맞추어서 표현하는것을 의미한다. 여기에서는 표현하려는 i 값을 4자리에 맞추어서 표현해주는것을 의미힌다.
    print()
    print('---+' + (4 * len(a)+2) * '-')
    
    while True:
        pc = (pl + pr) // 2
        print('    |',end='')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+',end='')
        else: # pl == pc
            print((pc * 4 + 1) * ' ' + '<+',end='')
        if pc != pr:
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:4}|',end='')
        for i in range(len(a)):
            print(f'{a[i]:4}',end='')
        print('\n    |')
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1 #중간 인덱스의 실제값이 키값보다 작은 경우 중간 인덱스 + 1 부터 끝까지로 검색범위를 줄 일 수 있다. 
        else:
            pr = pc - 1 #중간 인덱스의 실제값이 키값보다 큰 경우 검색범위 시작 인덱스부터  중간 인덱스 - 1까지 검색범위를 줄일 수 있다. 
        if pl > pr: 
            break
            return -1

if __name__=="__main__":
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num
    
    for t in range(num):
        x[t] = int(input(f'x[{t}] : '))
    
    x.sort() #sequence x를 오름차순으로 정렬한다.
    
    key = int(input("검색하고자 하는 값 입력하기 : "))
    idx = binSearch(x,key)
    if idx == -1:
        print("찾으려는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")
            