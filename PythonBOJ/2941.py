'''
-크로아티어 알파벳 변경하여 입력

č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=


ljes=njak -> lj / e / s= / nj / a / k

위의 표에 없는 알파벳은 단독적 알파벳으로 간주한다.'
입력된 크로아티어 알파벳에 대해서 총 몇개의 알파베으로 이루어져있는지 구하시오

ex
 ljes=njak -> 6
 
 d dz= z
'''


inputData = input()

convertDict = ['c=','c-','dz=','d-','lj','nj','s=','z=']

totalCount = 0
nowInCheck = [inputData]
lastString = inputData
for t in convertDict:
    capsule = list()
    for u in nowInCheck:
        for y in list(u.split(t)):
            capsule.append(y)
    nowInCheck = capsule
    totalCount += (len(lastString) - len(''.join(nowInCheck))) / len(t)
    lastString = ''.join(nowInCheck)
    
totalCount += len(''.join(nowInCheck))
print(int(totalCount))