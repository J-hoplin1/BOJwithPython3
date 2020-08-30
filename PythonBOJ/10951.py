# 조건 : 여러개의 테스트 케이스를 주는 경우 : 즉 이러한 문제에서는 만약 테스트케이스에서 부여하는 데이터의 개수가 예시의 개수 이상이 부여되는것을 검사하는것이 되는것이다,
try:
    while True:
        a,b = input().split(' ')
        print(int(a) + int(b))
except:
    exit()
