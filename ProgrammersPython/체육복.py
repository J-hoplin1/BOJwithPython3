'''
문제 : https://programmers.co.kr/learn/courses/30/lessons/42862 

점심시간에 도둑이 듬 -> 체육복 도벽함 -> 여벌로 가져온 사람은 자기 번호 -1 혹은 + 1 사람에게만 빌려줄 수 있음

중요하게 여거볼 제한사항
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 도 있다. 이때 이 학생은 체육복을 하나만 도난당했다 가정, 남은 체육복이 하나이기에 다른 학생에게 빌려줄 수 없다.

위 제한사항은 트릭이다. 입출력 예시에는 주어지지 않았지만 만약 parameter lost와 reserve에 둘다 있다면
reserve에 해당되지 않으므로 reserve에서 제외해주어야한다.

이 문제는 Greedy알고리즘으로 해결을 하였다

우선 reserve요소들중 lost에 있는 학생이 있는지 filter를 해주고 reserve에서 제거를 해준다
그 후 lost, reserve에서 조건에 걸린 요소들을 제거해주고
여벌을 빌려주는 반복문을 실행해준다

filter 최대 시간복잡도를 O(n)으로 가정하면
해당 알고리즘 총 O(3n)값을 가진다. 
'''

def solution(n, lost, reserve):
    lostButReserved = list(filter(lambda x : x in lost, reserve))
    for i in lostButReserved:
        lost.remove(i)
        reserve.remove(i)
    
    for i in reserve:
        if i in lost: # 만약 여벌 체육복을 가져온 학생이 도둑 맞은 경우
            lost.remove(i)
            continue
        if i - 1 in lost: # 여벌 학생 -1 번이 도둑맞은 경우
            lost.remove(i - 1)
            continue
        if i + 1 in lost:# 여벌학생 + 1 번이 도둑맞은 경우
            lost.remove(i + 1)
            continue
    return n - len(lost)
