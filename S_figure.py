'''
Описание задачи/Task description
RU
Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

ENG
Residents of Malevia often experiment with the layouts of their rooms. 
Rooms are triangular, rectangular and round.
To quickly calculate the living space, you need to write a program that receives the type of room figure and the corresponding parameters as input, which would display the area of the resulting room
For the number π in the country of Malevia, the value 3.14 is used.
'''

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

    
