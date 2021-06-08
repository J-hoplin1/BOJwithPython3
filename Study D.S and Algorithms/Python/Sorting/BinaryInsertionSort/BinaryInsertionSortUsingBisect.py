from typing import MutableSequence
import bisect

'''
bisect모듈의 insort()함수는 단순 삽입정렬을 제공한다.

이를 사용하면 이미 정렬이 끝난 배열의 상태를 유지하면서 원소를 삽입한다.

bisect.insort()를 사용하여 이진삽입정렬을 구현해 보자.
'''


def binary_insertion_sort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a,a.pop(i),0,i) # pop()에 인자를 건내주면 해당 인자 index의 값을 반환한다.
        # binsect.insort(a,x,lo,hi)를 호출하면 a(list)가 이미정렬된 상태를 유지하면서 a[lo] ~ a[hi]사이에 x를 삽입한다.
        #만약 a안에 x와 동일한 값을 가지는 원소가 여러개 있는 경우 가장 오른쪽에 위치하게 된다.

print("이진 삽입 정렬을 수행합니다")
totalCount = int(input("원소 수를 입력하세요 : "))
li = []
for i in range(totalCount):
    data = int(input(f"x[{i}] : "))
    li.append(data)

binary_insertion_sort(li)

for t in range(len(li)):
    print(f"x[{t}] : {li[t]}")
