import  sys
code = list(map(int,sys.stdin.readline().split()))
code = [a * a for a in code]
print(sum(code) % 10)
