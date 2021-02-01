from enum import Enum 
from openAddressHash import OpenAddress

options = Enum('Option',['추가','삭제','검색','덤프','종료'])

def optionSelect():
    s = [f'({a.value}) {a.name}' for a in options]
    while True:
        print(*s, sep = '  ', end = '')
        select = int(input(' : '))
        if 1 <= select <= len(options):
            return options(select)

hashTable = OpenAddress(13)

while True:
    select = optionSelect()
    if select == options.추가:
        key = int(input('추가할 키값 입력하기 : '))
        value = input('추가할 값 입력하기 : ')
        if not hashTable.add(key,value):
            print("값 추가에 실패하였습니다.")
    
    elif select == options.삭제:
        key = int(input("삭제할 값 키값 입력하기 : "))
        if not hashTable.remove(key):
            print("입력한 키값이 존재하지 않습니다.")
    
    elif select == options.검색:
        key = int(input('검색하고자 하는 값 입력하기'))
        data = hashTable.search(key)
        if not data:
            print("검색한 값이 존재하지 않습니다")
        else:
            print(f"검색한 키값 {key}의 값은 {data}입니다")
    
    elif select == options.덤프:
        hashTable.dump()
    else:
        break
