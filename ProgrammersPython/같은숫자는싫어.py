'''
연습문제
URL : https://programmers.co.kr/learn/courses/30/lessons/12906
'''

def solution(arr):
    answer = []
    # 배열의 중복된 수를 제거하되, 숫자의 기본적인 순서는 유지
    recentAdded = arr[0]
    for t in arr:
        if t != recentAdded:
            answer.append(recentAdded)
            recentAdded = t
        else:
            pass
    answer.append(recentAdded)#마지막에 있는 recentAdded를 answer에 추가해준다
    return answer
