from string import ascii_uppercase, ascii_lowercase

li = list(ascii_uppercase)#대문자
li_z = list(ascii_lowercase)#소문자

total = []
socket = []

for a in range(0, len(li)):
    socket.append(li[a])
    socket.append(li_z[a])
    total.append(socket)
    socket = list()

#알파벳 리스트
li_q = []
io = input()

#단어의 알파벳들을 모두 리스트에 넣기
for a in range(0, len(io)):
    li_q.append(io[a])

#문자가 소문자인 경우에는 모두 대문자로 변환해주기.
for b in range(0,len(li_q)):
    if li_q[b] in li_z:
        ind = li_z.index(li[b])
        li_q[b] = li[ind]
