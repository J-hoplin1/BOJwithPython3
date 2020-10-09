from searchWhile import seq_search

print("실수를 검색합니다.")
print("주의 : End 를 입력하면 종료합니다.")

number = 0

x = list()

while True:
    s = input(f'x[{number}] : ')
    if s == 'End': 
        break 
    x.append(float(s))
    number += 1

key = float(input('검색할 값을 입력하세요 : '))

idx = seq_search(x,key)

if idx == -1:
    print("검색하려는값 존재하지 않음")
else:
    print(f"검색값은 x[{idx}]에 있습니다.")