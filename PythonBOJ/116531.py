numb = int(input())
#입력된 수가 1인 경우 아무것도 출력하지 않는다.
divisor = 2
while numb != 1:
    if numb % divisor == 0:
        print(divisor)
        numb = numb // divisor
    else:
        divisor += 1
