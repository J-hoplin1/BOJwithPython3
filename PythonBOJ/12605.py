import sys

totalCases = int(sys.stdin.readline())
for e in range(1,totalCases + 1):
    sentence = sys.stdin.readline()
    reverseSentence = ' '.join((sentence[:-1].split(' '))[::-1])
    print(f'Case #{e}: {reverseSentence}')
