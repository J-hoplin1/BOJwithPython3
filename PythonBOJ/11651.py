import sys

'''
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램 작성하시오
'''

count = int(input())
results = list()
for _ in range(count):
    x,y = map(int,sys.stdin.readline().split())
    results.append((x,y))

results.sort(key=lambda x:(x[1],x[0]))
for t in results:
    print(f'{t[0]} {t[1]}')
