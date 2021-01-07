from queue import FixedQueue
from enum import Enum
from typing import Any

option = Enum('option',['인큐','디큐','피크','검색','덤프', '종료'])

def selectOption() -> option:
    s = [f'{t.value}. {t.name}' for t in option]
    while True:
        print(*s, sep='     ', end='')
        n = int(input(" : "))
        if 1<=n<= len(option):
            return option(n)


quee = FixedQueue(30)

while True:
    print(f'현재 데이터의 개수 : {len(quee)} / {quee.capacity}')
    
    opt = selectOption()
    
    if opt == option.인큐:
        x = int(input("인큐할 데이터 입력하기 : "))
        try:
            quee.enque(x)
        except FixedQueue.Full:  #enque의 발생 가능한 예외 : Full에 대한 예외
            print("큐가 가득 찼습니다.")

    elif opt == option.디큐:
        try:
            deqData = quee.deque()
            print(f'deque한 데이터는 {deqData}입니다.')
        except FixedQueue.Empty:  #deque의 발생 가능한 예외 : Empty에 대한 예외
            print("큐가 비었습니다.")
    
    elif opt == option.피크:
        try:
            peekData = quee.peek()
            print(f'peek한 데이터는 {peekData}입니다.')
        except FixedQueue.Empty:# peek의 발생 가능한 예외 : Empty에 대한 예외
            print("큐가 비었습니다.")

    elif opt == option.검색:
        searchData = int(input("검색하고자 하는 데이터값 입력하기 :"))
        if searchData in quee: # FixedQueue클래스의 __contains__ 메소드에 의해 in  연산자 사용이 가능하다.
            print(f'찾고자 하는 데이터는 총 {quee.count(searchData)}개 이며 가장 처음 등장하는 index는 {quee.find(searchData)}입니다')
        else:
            print(f"찾고자 하는 데이터 {searchData}는 현재 queue에 존재하지 않습니다.")
    
    elif opt == option.덤프:
        quee.dump()
    else:
        break
