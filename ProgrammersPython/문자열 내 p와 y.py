'''
대소문자 섞여있는 문자열 s가 주어진다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True
다르면 False를 return하는 solution을 만들어라.
'p','y'모두 하나도 없는 경우에는 항상 True를 리턴한다.
단 개수 비교할때 대소문자 비교 x
'''
from collections import Counter

def solution(s):
    answer = True
    checker = Counter(list(s.lower()))
    if ('p' not in checker) and ('y' not in checker):
        return True
    elif checker['p'] == checker['y']:
        return True
    else:
        return False
