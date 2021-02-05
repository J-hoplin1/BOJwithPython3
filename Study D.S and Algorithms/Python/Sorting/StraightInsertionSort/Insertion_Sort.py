from typing import Any, MutableSequence


def insertSort(a : MutableSequence):
    n = len(a)
    for t in range(1, n): # 삽입정렬은 맨앞에서 두번째 원소부터 검색을 시작한다.
        sa = t # 현재 주목중인 인수의 index이다. 이 index를 기준으로 왼쪽은 정렬된 부분 오른쪽은 정렬되지 않은 부분으로 구분된다.
        insertVal = a[t] # 현재 주목중인 인수의 value이다. 주목중인 인자값의 적절한 자리 검색이 완료 되면 그 부분에 값을 넣는다.
        while sa > 0 and a[sa - 1] > insertVal:# 정렬된 부분에 대한 검사이다. 정렬된 부분 검사 index값이 0 이상이고, 검사 index - 1번째 index의 값이 검사index의 값보다 큰경우에 멈춘다.
            a[sa] = a[sa - 1] # 위 조건문이 끝날때 까지 현재 검사중인 index의 자리에 이전 index자리의 value를 스캔한다.
            sa -= 1
        a[sa] = insertVal
        print(a)

a = [6,4,3,7,1,9,5]
insertSort(a)
print(*a , sep='  ')
