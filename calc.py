a = float(input())
b = float(input())
c = input()

if c == '+':
    print(float(a+b))
elif c == '-':
    print(float(a-b))
elif c == '*':
    print(float(a*b))
elif c == 'pow':
    print(float(a**b))
elif b != 0 and c == '/':
    print(float(a/b))
elif b != 0 and c == 'mod':
    print(float(a%b))
elif b != 0 and c == 'div':
    print(float(a//b))
else:
    print('Деление на 0!')
