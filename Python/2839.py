a = input()

test = 0
min_num = 0  
a_n = 0

while(test <= (int(a) // 5)):
    a_n = int(a) - (test *5) 
    if((a_n % 3) != 0):
        test += 1
        continue
    else:
        min_num = test + (a_n / 3)
        test += 1

if(min_num == 0):
    min_num = -1

print(int(min_num))

    
        
        
