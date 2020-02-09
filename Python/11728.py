import sys
donknowwhat = list(map(int,sys.stdin.readline().split()))
val = None
for a in range(0,2):
    r = list(map(int,sys.stdin.readline().split()))
    if val == None:
        val = r
    else:
        val += r
for b in sorted(val):
    print(b, end=' ')