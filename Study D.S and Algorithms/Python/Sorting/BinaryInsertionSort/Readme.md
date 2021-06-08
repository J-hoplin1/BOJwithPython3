이진삽입정렬(Binary Insertion Sort)
===
***

- Straight Insertion Sort같은 경우 원소 수가 많아지면 원소 삽입에 필요한 비교 교환 비용이 커진다.

- Binary Insertion Sort를 사용해 삽입정렬을 하면 정렬을 마친 배열을 제외하고 원소 삽입할 위치를 검사하므로 비용을 줄일 수 있다.

***
### 들어가기전 Binary Sort에 대해 알아보자

들어가기전  이진검색에 대해 알아보자. 이진검색 알고리즘의 기본 조건은 **'정렬이 되어있는 상태'** 이다. 이진 검색을 사용하면 선형검색에 비해 빠르게 검색할 수 있다.

이진 검색에서는 아래 두가지 중요한 변수가 존재한다.

  - pl : 검색범위의 첫번째 Index
  
  - pr : 검색범위의 마지막 Index
 
이 두 변수를 가지고 검색범위를 설정하고 검색범위의 가운데 Index(여기서는 pc라고 하겠다.)(pl + pr // 2)의 값(여기서는 key라고 하겠다)에 따라 검색범위를 좁힌다.

  - key > list[pc] : pl값을 pc + 1로 변경
  
  - key < list[pc] : pr값을 pc - 1로 변경

이진검색의 기본적인 종료조건은 아래 두가지가 있다.

  - list[pc]와 key값이 일치하는경우(= 찾고자하는 값을 찾은 경우)
  
  - 검색범위가 더이상 없는 경우(= 찾고자 하는 값을 못찾은 경우)
  
이진 검색 기본 구현 -> [여기](https://github.com/J-hoplin1/Problem-Solving/blob/master/Study%20D.S%20and%20Algorithms/Python/binarySearch/binarySearch1.py)
***

이진 삽입 정렬의 결론은 정렬을 위해 삽입할 key값을 binary search를 이용해서 찾는 과정을 의미한다.

```python
from typing import Any, MutableSequence

def binary_search(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1,n):
        key = a[i] # 정렬할 위치를 찾아야하는 key값을 미리 저장한다.

        pl = 0 # 정렬하고자 하는 검색범위의 첫번째 index
        pr = i # 정렬하고자 하는 검색범위의 마지막 index

        while True:
            pc = (pl + pr) // 2 # 검색범위의 가운데 index값이다. 이 index값을 기준으로 검색범위를 조정한다.
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1 # 'pl <= pr' -> a[pc] == key인 경우 else : 정렬할 곳을 찾은 경우
        for j in range(i,pd,-1):
            a[j] = a[j-1]
        a[pd] = key
```
