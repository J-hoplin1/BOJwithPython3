'''
enumerate() : 인덱스와 원소를 짝지어서 튜플로 꺼내는 내장함수이다.
(인덱스, 원소)
'''

a = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ']

for e,t in enumerate(a):
    print(f'a[{e}] = {t}')