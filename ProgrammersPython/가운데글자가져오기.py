#https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

from typing import Any

def solution(s) -> str:
    if len(s) % 2 == 0: #짝수인 경우
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    else:
        return s[(len(s)//2)]

'''
문자열 길이가 짝수인지 홀수인지에 따라 판별하면 된다.

짝수 : 2로 나눈 몫 - 1 부터 나눈몫 + 1의 index범위 슬라이싱

홀수 : 2로 나눈몫 index값 반환
'''

if __name__=="__main__":
    exString = "abcdef"
    print(solution(exString))
