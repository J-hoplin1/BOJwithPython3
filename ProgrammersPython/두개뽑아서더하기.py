'''
월간 코드 챌린지 시즌1 : 두개 뽑아서 더하기
URL : https://programmers.co.kr/learn/courses/30/lessons/68644
'''
def solution(numbers):
    answer = []
    cutInd = 1
    for e in numbers:
        for t in numbers[cutInd:]:
            answer.append(e+t)
        cutInd += 1
    answer = sorted(list(set(answer)))
        
    return answer
