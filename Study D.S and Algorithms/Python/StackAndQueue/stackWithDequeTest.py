from enum import Enum 
from stackWithDeque import Stack

option = Enum('opt',['push','pop','peek','search','dump','exit'])

s  = Stack(20)

def selectOption() -> option:
    lit = [f'({a.value}) {a.name}' for a in option]
    while True:
        print(*lit, sep = '     ', end = '')
        ret = int(input(' : '))
        if 1 <= ret <= len(option):
            return option(ret)

while True:
    print(f'현재 스택 내 데이터 개수 : {len(s)} / {s.capacity}')
    opt = selectOption()

    if opt == option.push:
        x = int(input('데이터 입력하기 : '))
        try:
            s.push(x)
        except Stack.full:
            print("스택이 가득 찼습니다.")
    elif opt == option.pop:
        try:
            print(f'pop 결과 : {s.pop()}')
        except Stack.empty:
            print("스택이 비어있습니다.")
    elif opt == option.peek:
        try:
            x = s.peek()
            print(f'peek 결과 : {x}')
        except Stack.empty:
            print("스택이 비어있습니다.")
    elif opt == option.search:
        x = int(input("검색할 내용 : "))
        if x in s:
            print(f"검색한 x는 총 {s.count(x)}개이며, 최초로 발견된 index는 {s.find(x)}입니다")
        else:
            print("검색할 수 없습니다 : 존재하지 않음.")
    elif opt == option.dump:
        s.dump()
    else:
        break
