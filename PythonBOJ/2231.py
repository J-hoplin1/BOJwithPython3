'''
brute force
'''

N = int(input())

br = True
for t in range(1,N+1):
    if N == sum(list(map(int,[t] + list(str(t))))):
        print(t)
        br = False
        break
if br:
    print(0)
