단순 선택 정렬(Straight Selection Sort)
===
***

### 단순선택정렬이란?

- 가장 작은 원소부터 선택해 알맞은 위치로 옮기는 작업을 반복하며 정렬하는 알고리즘이다.

    - 아래와 같은 배열이 있다고 가정하자.
        
        ~~~
        [6,4,8,3,1,9,7]
        ~~~
    
    - 1이 가장 작은 수이므로 맨 앞에 위치해야한다. 그렇기 때문에 이와 같이 교환해준다

        ~~~
        [1,4,8,3,6,9,7]
        ~~~
    
    - 그 후 다음으로 작은 숫자인 3은 두번째 자리에 위치해야한다. 이와같이 교환해준다.

        ~~~
        [1,3,8,4,6,9,7]
        ~~~
    - 단순 선택 정렬은 이과정을 계속해서 반복하여 정렬하는 정렬을 의미한다.

    - 결론적으로 정렬하지 않은 부분에 대해서 그 부분에서 가장 작은 값이 있는 index값과 가장 앞에있는 값과 자리를 바꾸어가며 정렬하는 방식이다.

- 단순 선택 정렬의 기본적인 구현은 아래와 같다.

    ```python
    from typing import MutableSequence

    def selection_sort(a : MutableSequence)-> None:
        n = len(a)
        for i in range(n-1):
            minValueIndex= i # 가장 작은 값의 index를 저장하는 변수이다.
            for t in range(i + 1,n):
                if a[t] < a[minValueIndex]:
                    minValueIndex = t
            a[i],a[minValueIndex] = a[minValueIndex], a[i]


    a = [1,2,4,3,6,5]
    selection_sort(a)
    print(a)  
    ```
- 단순선택 정렬은 서로 이웃하지 않는 원소를 비교하지 않기 때문에 안정적이지 않은 정렬이다.

    - ex)
    ~~~
    [3L, 4, 2, 3R, 1]
    [1, 4, 2, 3R, 3L]
    [1, 2, 4, 3R, 3L]
    [1, 2, 3R, 4, 3L]
    [1, 2, 3R, 3L, 4]

    위의 예시와 같이 초기 배열에서의 순서였던 3L-3R이 정렬후에는 3R-3L로 변경된것을 볼 수 있다.
    ~~~
