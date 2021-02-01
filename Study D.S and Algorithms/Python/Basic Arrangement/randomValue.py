import random
from MaxValue import max_of

print('난수의 최대값을 구합니다.')

num = int(input('난수의 개수를 입력하세요 : '))
low = int(input("난수의 최소값을 입력하세요 : "))
high = int(input("난수의 최댓값을 입력하세요 : "))
x = [None] * num

for t in range(num):
    x[t] = random.randint(low,high) # low이상 high 이상이 난수를 반환한다.
print(f'{x}')
print(f'해당 리스트의 최댓값은 {max_of(x)}입니다.')