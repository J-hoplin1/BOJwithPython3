'''
연산 R -> Reverse -> reverse시행 횟수가 짝수인경우 시행 X 홀수인 경우는 1번 시행
연산 D -> 첫번째 숫자를 버리는 함수 -> deque의 popleft()

결론적으로 시간 줄이는 문제였다.

deque클래스를 만들어서 최초 R과 최초 D사이의 R개수에 따라 홀수인 경우 reverse()연산 후 popleft()
짝수인 경우에는 popleft()를 해주었는데

시간을 줄이는 요소로 한번더 생각해보면

결론적으로 전체적인 흐름에서 실행할 함수 R의 개수가 짝수인 경우는 어차피 reverse를 하지않는다
반대로 전체적인 흐름에서 실행할 함수 R의 개수가 홀수인 경우는 어차피 reverse를 한번 한것과 동일하다

이를 기반으로 해석해보면

RRRD 와 같은 함수 실행을 하게 되면, 이는 reverse() 후 popleft()한 값이 어야 한다.
하지만 여기서 reverse()를 수행하지 않고 pop()을 한 후 마지막에 전체 R의 개수에 따라 reverse를 해준다면
연산의 시간을 훨씬 단축시킬수 있다.

기존 접근 법대로 풀게되면 

RRRDDRRRDDDRRD
라는 예시가 있으면 총 2번의 reverse()를 했겠지만
아래와 같은 접근법으로 풀면 만약 D가 나오기 전까지 R의 개수가 짝수라면 그냥 popleft()를 해주면된다
반대로 R의 개수가 홀수였다면 실제로는 reverse()후 popleft()를 해야하지만 이는 그냥 단순히 오른쪽에서 pop()연산을 수행한것과 마찬가지가 된다


결론은 R에 대한 count변수 하나를 두고
D가 나올 경우 그 때의 count변수가 짝수인지 홀수인지 판별 후 popleft()혹은 pop()을 수행해주면 되는것이다

주의해야할 반례

1
RRRRR
0
[]
-> []
'''


import sys
from collections import deque

#테스트케이스 개수 T
testCase = int(input())
results = list()
for _ in range(testCase):
    # 사용할 함수들
    functions = list(input())
    #배열에 들어있는 원소의 개수
    elementCount = int(input())
    arr = list(sys.stdin.readline().strip('[]\n').split(','))
    
    if not elementCount:
       arr = []
    else:
        arr = deque(arr,elementCount)

    shutdown = False
    countR =0
    for p in functions:
        if p == 'R':
            countR += 1
        else:
            if not arr:
                shutdown = True
                break
            else:
                if countR % 2:
                    arr.pop() # R의 개수가 홀수인 경우에는 reverse한 값에서 popleft()를 하는것이므로 pop()연산과 동일한 값
                else:
                    arr.popleft()
    
    if shutdown:
        print('error')
    else:
        if countR % 2:
            arr.reverse()
            print('[',end='')
            for t in range(len(arr)):
                if t == len(arr) - 1:
                    print(f'{arr[t]}',end='')
                else:
                    print(f'{arr[t]},',end='')
            print(']')
        else:
            print('[',end='')
            for t in range(len(arr)):
                if t == len(arr) - 1:
                    print(f'{arr[t]}',end='')
                else:
                    print(f'{arr[t]},',end='')
            print(']')
