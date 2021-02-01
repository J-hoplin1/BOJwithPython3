'''
셰이커 정렬

shaker sort : 홀수 패스에서는 가장 작은 원소를 맨 앞으로 이동시키고, -> 뒤에서 앞으로 검사
                짝수 패스에서는 가장 큰 원소를 맨 뒤로 이동시킨다. -> 앞에서 뒤로 검사
'''

from typing import MutableSequence

def shaker_sort(a : MutableSequence) -> None:
    n = len(a)
    right = n-1
    left = 0
    last = right
    passCount = 0
    while left < right:
        for j in range(right,left,-1): # 첫번째 shaking : 가장 작은 원소를 맨 앞으로 이동시킨다.
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j], a[j-1]
                last = j
                passCount += 1
        left = j # 첫번째 shaking에 대해서 비교 교환이 일어난 가장 마지막 index를 left에 저장
        
        for p in range(left,right): # 두번째 shaking : 가장 큰 원소를 맨 뒤로 이동시킨다.
            if a[p+1] < a[p]:
                a[p+1],a[p] = a[p], a[p+1]
                last = p
                passCount += 1
            right = p
    print(f'패스를 거친 횟수 : {passCount}')

if __name__ == "__main__":
    mutSeq = []
    a = int(input("리스트 총 길이 : "))
    for _ in range(a):
        mutSeq.append(int(input("원소 : ")))
    shaker_sort(mutSeq)
