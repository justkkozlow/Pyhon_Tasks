n = int(input())

if n % 10 == 1 and (n % 100) // 10 != 1:
    print(n, 'программист')
elif (n % 10 == 2 or n %  10 == 3 or n % 10 == 4) and (n % 100) // 10 != 1:
    print(n, 'програмиста')
else:
    print(n, 'программистов')


