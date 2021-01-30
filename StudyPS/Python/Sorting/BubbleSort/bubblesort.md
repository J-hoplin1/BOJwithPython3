버블정렬
===
***

### 버블정렬(Bubble sort)이란?

- 이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘으로 단순교환 정렬이라고 부르기도 한다.

- 버블 정렬에서 index n에 있는 값보다 index n-1 에 있는 값이 더 클 경우에는 index n-1의 값을 index n으로 index n의 값을 index n-1로 보낸다.

- 기본적인 버블 정렬 알고리즘 같은 경우는 다음과 같이 코드를 작성 할 수 있다.

    ```python3
         
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
    ```
- 버블 정렬은 위의 코드 해석만으로도 알 수 있듯이 하나하나 비교해 가며 정렬하는 방법이다. for문이 2개 쓰이는 버블정렬의 시간복잡도는 최선, 최악, 평균의 경우 모두 O(n^2)로 결론지을 수 있다.(시간복잡도 게산법은 제 블로그에 올려져 있습니다.)

- 버블 정렬에서 중요한것이 있다. 서로 이웃한 두 수를 비교하고 이 비교에 의해 교환이 필요할때 교환하는 이 과정을 **패스(pass)**라고 부른다. 패스의 코드 부분은 아래와 같다.

    ```python3
    for j in range(n - 1,t,-1): # n-1부터 t번째 inedx 전까지
                if a[j-1] > a[j]: # 마지막 검사 index가 나올때 t번째 index와 검사를 시행한다.
                    a[j-1], a[j] = a[j], a[j-1]
    ```

### 버블 정렬을 계산해 보자.

- 위에서 말했듯 버블정렬의 시간복잡도는 O(n^2)로 매우 비효율적인 알고리즘을 가지고 있다. 배열의 원소 개수가 많으면 많아질수록 처리속도는 기하급수적으로 느려질 것이다.

- 버블정렬의 기본적인 성질인 '이웃된 두 수끼리 비교, 교환을 수행' 이라는것은 바꿀 수 없지만 몇가지 방법을 통해서 불필요한 연산을 제거함에 따라 효율적으로 만들어 볼 수 있다.

    1. [비교 교환 횟수가 없는 경우의 중단](https://github.com/J-hoplin1/Problem-Solving/blob/master/StudyPS/Python/Sorting/BubbleSort/BubbleSort2.py)

        - 예를 들어서 아래와 같은 배열이 있다고 가정하자.

            ~~~
            [1,3,6,4,7,8,9]
            ~~~
        
        - 이 배열에 대해 4번째 패스를 수행할 떄 교환이 한번도 일어나지 않는다. 이말은 즉슨 이미 정렬이 완료되었다는 뜻이다.4번쩨 패스의 마지막 검사 index기준 앞은 당연히 정렬이 끝난상태여야하고, 뒤에 또한 정렬할것이 없다는 의미가 된다.

        - 이런 경우에는 해당 패스가 끝난 후에 그 다음 패스를 거칠 이유가 없다. 그 즉시 반복문을 break해주면 된다.

    2. [더 이상 비교 교환이 이루어지지 않는 특정 원소](https://github.com/J-hoplin1/Problem-Solving/blob/master/StudyPS/Python/Sorting/BubbleSort/BubbleSort3.py)

        - 아래와 같은 배열이 있다고 가정하자.

            ~~~
            [1,3,9,4,7,8,6]
            ~~~
        
        -   이 배열의 첫번째 패스를 보면

            ~~~
            1 3 9 4 7 8-6
            1 3 9 4 7-6 8
            1 3 9 4-6 7 8
            1 3 4-9 6 7 8
            1 3-4 9 6 7 8
            1-3 4 9 6 7 8
            ...
            ~~~
        
        - 4번째 비교 교환까지가 마지막 비교 교환이고 그 이후에는 일어나지 않는다. 이말은 즉 마지막 비교 교환이 일어난 부분보다 앞부분은 이미 정렬이 완료된 상태라는 의미이다.

        - 그렇기 때문에 다음 패스를 거칠때는 마지막으로 교환이 일어난 index부터 패스를 시작하면 되는것이다. 이러면 불필요한 반복문을 줄일 수 있다.

    3. [Shaker Sort](https://github.com/J-hoplin1/Problem-Solving/blob/master/StudyPS/Python/Sorting/BubbleSort/ShakerSort.py)

        - 홀수번째 패스는 뒤에서 앞으로, 짝수번째 패스는 앞에서 뒤로 정렬하는 방법
