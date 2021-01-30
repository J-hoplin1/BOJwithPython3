from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for t in range(n - 1): # 마지막 원소는 다음 비교할 대상이 없기때문
        for j in range(n - 1,t,-1): # n-1부터 t번째 inedx 전까지
            if a[j-1] > a[j]: # 마지막 검사 index가 나올때 t번째 index와 검사를 시행한다.
                a[j-1], a[j] = a[j], a[j-1]

if __name__=="__main__":
    print("Bubble Sort")
    elemetns = int(input("원소개수 입력하기 : "))
    seq = []
    for _ in range(elemetns):
        seq.append(int(input("원소 입력하기 : ")))
    
    bubble_sort(seq)
    print(*seq, sep = '  ')
