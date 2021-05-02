import sys

'''
a는 하루 최대 올라갈수 있는 높이
b는 하루에 미끄러 지는 높이
v는 달팽이가 올라가야하는 총 높이이다.

결론적으로 달팽이가 잠을 자는 날에는 a-b만큼의 높이밖에 못올라가는 것이다.
그리고 마지막에는 결국에는 최대 a만큼의 높이를 올라가게 되어있다.

그렇기에 전체 높이에서 마지막날 최대 올라가는 높이만큼 빼주고 남은 높이에대해 계산을 해준다

남은 높이에 대해 a-b로 나누어 준다. 나머지가 존재한다면 어차피 다음날 그 높이만큼 또 올라가줘야하기 떄문에
몫에 1을 더해주고 나머지가 없다면 그냥 몫만 놔둔다

마지막에는 최대 a높이만큼 올라간다는 가정이 있었기에 이에대한 하루를 더 추가해준다.
'''

a,b,v = map(int,sys.stdin.readline().split())

subtractDistance = v - a
res = 0

if (subtractDistance % (a - b)) == 0:
    res = subtractDistance // (a - b)
else:
    res = (subtractDistance // (a - b)) + 1
print(res + 1) 
