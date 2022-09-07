f = input()

if f == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p*(p-a)*(p-b)*(p-c)) ** (0.5)
    print(s)
if f == 'круг':
    r = int(input())
    pi = 3.14
    s = pi*(r**2)
    print(s)
if f == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a*b
    print(float(s))

    
