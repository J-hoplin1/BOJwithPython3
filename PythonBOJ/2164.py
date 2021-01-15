'''
풀이

순서대로 K번째 사람을 제거한다. 한사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해서 나가진다
이 과정은 N명의 사람이 제거되면 남은 살마들로 이루어진 원을 따라 이과정을 계속해 나간다.

처음에는 1~N번까지의 cards를 초기화해준다

이 문제는 Rounded Queue의 원리를 응용하면 풀수 있다

풀이 과정을 다음과 같다


front : 0

1)
1234567

delete index of : (front + (K-1)) % len(cards) = 2(3) -> K-1을 하는 이유는 리스트에서 실제로 인덱싱을 할때는 0부터 시작하기 떄문이다

front = 2

2)
124567

delete index of : (front + (K-1)) % len(cards) = 4(6)

front = 4

3)
12457

delete index of : (front + (K-1)) % len(cards) = 1(2)

front = 1

4)
1457

delete index of : (front + (K-1)) % len(cards) = 3(7)

front = 3

5)
145

delete index of : (front + (K-1)) % len(cards) = 2(5)

front = 2

6)
14

delete index of : (front + (K-1)) % len(cards) = 0(1)
front = 0

7)
4

이제 남은 카드는 4 하나이므로 result에 그냥 넣어준다.
'''

N,K = input().split()

cards = [t for t in range(1,int(N) + 1)]
results = []
front = 0
while len(cards) != 1:
    capacity = len(cards)
    deleteIndex = (front + (int(K)-1)) % capacity
    results.append(cards[deleteIndex])
    del cards[deleteIndex]
    front = deleteIndex
results = list(map(str,results + cards))
print('<' + ', '.join(results) + '>')
