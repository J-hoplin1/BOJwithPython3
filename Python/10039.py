import sys
scores = list()

for e in range(5):
    a = int(input())
    if a < 40:
        a = 40
    else:
        pass
    scores.append(a)

print(int(sum(scores)/len(scores)))
