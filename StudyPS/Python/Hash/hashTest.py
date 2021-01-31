from enum import Enum
from hash import ChainedHash

option = Enum('option',['추가','삭제','검색','출력','종료'])

hashTable = ChainedHash(13)

def optionSelect() -> 'option':
    s = [f'({a.value}) {a.name}' for a in option]
    while True:
        print(*s, sep = ' ', end='')
        select = int(input(' : '))
        if 1 <= select <= len(option):
            return option(select)

while True:
    option = optionSelect()

    if option == option.추가:
        key = int(input('추가할 키값 입력하기 : '))
        value = input('추가할 값 입력하기 : ')
        if not hashTable.add(key,value):
            print("추가하고자 하는 Key Value는 Hash Table에 이미 존재합니다.")
        else:
            print("추가 성공")
    
    elif option == option.삭제:
        key = int(input('삭제하고자 하는 데이터의 Key값 입력하기 : '))
        if not hashTable.remove(key):
            print("삭제하고자 하는 Key값은 Hash Table에 존재하지 않습니다")
        else:
            print("삭제 완료")
    
    elif option == option.검색:
        key = int(input('검색할 키값 입력하기 : '))
        searchData = hashTable.search(key)
        if not searchData:
            print("검색하고자 하는 Key Value는 검색하지 않습니다.")
        else:
            print(f'{key} : {searchData}')
    
    elif option == option.출력:
        hashTable.dump()

    else:
        break
