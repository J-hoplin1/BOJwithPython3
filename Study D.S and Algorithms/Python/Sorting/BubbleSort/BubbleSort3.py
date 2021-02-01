'''
알고리즘 개선3

각각의 패스에서 비교 교환을 하다가 특정 원소 이후에 교환하지 않게 되면 
해당 원소의 앞부분은 이미 정렬이 되어있음을 의미한다.

그렇기 때문에 다음 비교 교환은 마지막 교환이 이루어진 index부터 다시 시작해 주면 되는 것이다.
'''
from typing import MutableSequence

def bubble_sort(a:MutableSequence):
    n = len(a)
    k = 0
    while k < n-1:  # k는 마지막으로 교환이 이루어진 index값을 저장하는 변수이다. 이 값이 n-1과 같거나 더 크면 안된다.
        last = n-1 # 검사를 하면서 마지막으로 교환이 이루어진 index를 저장한다.
        for t in range(n-1,k,-1):
            if a[t-1] > a[t]:
                a[t-1],a[t] = a[t],a[t-1]
                last = t
        k = last # 검사를 최종적으로 마친 후에 마지막으로 비교 교환이 이루어진 index를 k에 넣어준다.
