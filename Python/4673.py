'''
셀프넘버 

n 이 있다고 하면 n + n의 각 자리수의 합의 결과값을 y 라고하자.

그러면 n은 y의 생성자가 된다.

셀프넘버는 생성자가 없는 숫자를 의미한다.

'''


totalScopes = set(range(1,10001))
existSelfNumber = list()


for t in totalScopes:
    for p in str(t):
        t += int(p)
    existSelfNumber.append(t)

filt = sorted(list(totalScopes - set(existSelfNumber)))

for u in filt:
    print(u)
