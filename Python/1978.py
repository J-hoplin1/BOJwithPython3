import sys
totalNum = int(input())
vals = list(map(int,sys.stdin.readline().split()))
total_count = 0
for a in vals:
    if a == 1:
        continue
    if a == 2:
        total_count+=1
    else:
        TF = True
        for b in range(2,a):
            if a % b == 0:
                TF = False
                break
            else:
                continue
        if TF == True:
            total_count+=1
        else:
            continue
print(total_count)