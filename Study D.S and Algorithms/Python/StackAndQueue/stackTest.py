from enum import Enum 
from fixedStack import fixedStack

Option = Enum('option',['push','pop','peek','search','dump','exit'])

def selectOption() -> Option:
    t = [f'({t.value}) {t.name}' for t in Option]
    while True:
        print(*t,sep='  ',end='') # sep : 구분자 , end : 그 뒤 출력값과 이어서 출력
        n = int(input(' : '))
        if 1 <= n <= len(Option):
            return Option(n)

s = fixedStack(64)

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    option = selectOption()

    if option == Option.push:
        x = int(input('데이터 입력하기 : '))
        try:
            s.push(x)
        except fixedStack.full:
            print('스택이 가득찼습니다.')
    
    elif option == Option.pop:
        try:
            x = s.pop()
            print(f'pop 결과 출력 : {x}')
        except fixedStack.empty:
            print('스택이 비었습니다.')
    
    elif option == Option.peek:
        try:
            x = s.peek()
            print(f'peek 결과 출력 : {x}')
        except fixedStack.empty:
            print('스택이 비었습니다.')
    
    elif option == Option.search:
        x = int(input('검색할 내용 : '))
        if x in s:
            print(f'{s.count(x)}개 포합되고, 맨 앞 위치는 {s.find(x)}입니다')
        else:
            print('검색값을 찾을 수 없습니다.')
    elif option == Option.dump:
        s.dump()
    else:
        break
