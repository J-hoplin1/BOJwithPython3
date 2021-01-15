'''
URL : https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

초단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어짐

가격이 떨어지지 않은 기간은 몇초인지 return

[1,2,3,2,3] -> [4,3,1,1,0]
'''

def solution(prices):
    answer = []

    for u in range(len(prices)):
        if u == len(prices) -1:
            answer.append(0)
        else:
            countSec = 0 
            for i in range(u+1,len(prices)):
                if prices[u] > prices[i]:
                    countSec += 1 # 문제를 보면 다음과 같이 적혀있다. '3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.' 즉 그 다음 초에 가격이 떨어져도 그 직전에 가격이 유지된 시간도 시간에 포함해준다.
                    break
                else:
                    countSec += 1
            answer.append(countSec)
    return answer

print(solution([1, 2, 3, 2, 3]))
