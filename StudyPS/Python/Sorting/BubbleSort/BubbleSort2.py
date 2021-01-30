from typing import MutableSequence

# 교환 횟수에 따른 중단으로 불필요한 반복문 실행을 줄일 수 있다.

def bubble_sort(a : MutableSequence) -> None:
    n = len(a)
    for t in range(n-1):
        sortedCount = 0
        for i in range(n-1,t,-1):
            if a[i-1] > a[i]:
                a[i-1],a[i] = a[i],a[i-1]
                sortedCount+=1
        if not sortedCount:
            break # 교환이 일어나지 않았다는것은 정렬할 필요가 없다는 이야기이므로.
