from typing import MutableSequence

def selection_sort(a : MutableSequence)-> None:
    n = len(a)
    for i in range(n-1):
        minValueIndex= i # 가장 작은 값의 index를 저장하는 변수이다.
        for t in range(i + 1,n):
            if a[t] < a[minValueIndex]:
                minValueIndex = t
        a[i],a[minValueIndex] = a[minValueIndex], a[i]


a = [6,4,8,3,1,9,7]
selection_sort(a)
print(a)
