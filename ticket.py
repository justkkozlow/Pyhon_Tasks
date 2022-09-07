t = int(input())  
sum_left = 0
sum_right = 0
for i in range(6):
    if i < 3:
        sum_right += t // 10**i % 10
    else:
        sum_left  += t // 10**i % 10 
if sum_left == sum_right:
    print('Счастливый')
else:
    print('Обычный')  
