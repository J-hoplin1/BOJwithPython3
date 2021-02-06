from typing import MutableSequence

patterns = {
    '1' : [1,2,3,4,5],
    '2' : [2,1,2,3,2,4,2,5],
    '3' : [3,3,1,1,2,2,4,4,5,5]
}

def solution(answers : MutableSequence):
    answer = []
    datas = []
    maxVal = 0
    for l in range(3):
        check = 0
        ptn = patterns[str(l + 1)]
        checkFullPattern = len(answers) // len(ptn) 
        checkLackPattern = len(answers) % len(ptn)
        lastIndex = 0
        while len(ptn) * checkFullPattern != lastIndex:
            ans = answers[lastIndex : lastIndex + len(ptn)]
            for t in range(len(ptn)):
                if ptn[t] == ans[t]:
                    check += 1
                else:
                    pass
            lastIndex += len(ptn)
        
        if not checkLackPattern: # 나눈 나머지 0인경우
            pass
        else:
            ans = answers[lastIndex : lastIndex + len(ptn)]
            for p in range(len(ans)):
                if ptn[p] == ans[p]:
                    check += 1
                else:
                    pass
        
        if check > maxVal:
            maxVal = check
            datas.append(check)
        else:
            datas.append(check)

    for a,o in enumerate(datas,start = 1):
        if not o:
            pass
        elif o == maxVal:
            answer.append(a)
    
    if not datas:
        return 0
    else:
        return answer
