#운년이면 1 아니면 0
# 운년 : 연도가 4의배수이면서 100의 배수가 아닐때 또는 400 배수일때

year = int(input())

if year % 400 == 0:
    print('1')
elif year % 4 == 0 and year % 100 != 0:
    print('1')
else:
    print('0')
    
