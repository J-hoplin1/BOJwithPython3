'''
각 자리가 등차수열을 이루는 숫자 개수 찾기

1~99는 모두 등차수열로 본다. -> Why? 두자리수에서 날수있는 차수는 한가지밖에 없으므로

ex) 123 -> 2 - 1 = 1, 3 - 2 = 1
'''

n = int(input())

countNum = 0

for e in range(1, n + 1):
    if e < 100:
        countNum += 1
    else:
        # 두번째 자리 숫자와 첫번째 자리 숫자의 최초차이를 빼서 저장
        lastSub = int(str(e)[1]) - int(str(e)[0])
        #만약 차수가 달라질 경우 seq변수값을 False로 바꾸고 다음 정수로 넘어간다
        seq = True
        for p in range(1,len(str(e))-1):
            if int(str(e)[p + 1]) - int(str(e)[p]) == lastSub:
                pass
            else:
                seq = False
        if seq == True:
            countNum+=1
        else:
            pass
        

print(countNum)