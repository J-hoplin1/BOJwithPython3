'''
블랙잭

-> 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.

새 버전의 블랙잭

딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
그런후 딜러는 숫자 M을 외친다.

플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다.
플레이어가 고른 카드들의 합은 M을 넘지 않으며, M과 최대한 가깝게 만들어야한다.

N장의 카드에 써져있는 숫자가 주어졌을때 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오

Brute Force알고리즘을 이용하자
'''

import sys
from typing import Any

N,M = map(int,sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
maxValue = 0
for a in range(N-1, -1 ,-1):
    if cards[a] > M: #가장 큰 카드가 
        pass
    else:
        ck = cards[a]
        for w in range(len(cards[:a-1])):
            for r in range(len(cards[w+1:a])):
                if ck + cards[w] + cards[w+1:a][r] <= M:
                    if ck + cards[w] + cards[w+1:a][r] > maxValue:
                        maxValue = ck + cards[w] + cards[w+1:a][r]
                    else:
                        pass
                else:
                    pass
print(maxValue)
            
