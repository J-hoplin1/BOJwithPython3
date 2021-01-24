from typing import Any

def hanoi(floor,A,B,C):
    if floor == 1:
        print(f'{floor}층 원반은 {A}에서 {C}로 이동.')
    else:
        hanoi(floor-1,A,C,B)
        print(f'{floor}층 원반은 {A}에서 {C}로 이동.')
        hanoi(floor-1,B,A,C)

if __name__=="__main__":
    hanoifloor = int(input("하노이의 탑 층 입력 : "))
    hanoi(hanoifloor,'A','B','C')
