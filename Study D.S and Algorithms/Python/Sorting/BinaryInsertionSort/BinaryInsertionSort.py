from typing import MutableSequence  

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1,n):
        key = a[i] # 정렬하고자 하는 값
        pl = 0
        pr = i -1

        while True:
            # pc : 검색 범위 pl부터 pr의 중간 지점
            pc = (pl + pr) // 2
            if a[pc] == a: # 만약 가운데 값이 정렬하고자 하는 값이랑 같은 경우 break
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr: # pl > pr인 경우 -> 검색범위가 없어진 경우를 의미한다.
                break
        print(f'{pl} {pr}  {pc}')
        pd = pc + 1 if pl <= pr else pl

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key


if __name__ == "__main__":
    li = [19, 29, 38, 47, 26, 5, 17, 87, 44, 24, 67]
    binary_insertion_sort(li)
    print(li)
