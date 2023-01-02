t = int(input())
for index in range(t):
    a, b = input().split(' ')
    a_length = len(a)
    b_length = len(b)
    if a == b:
        print('=')
    elif a[-1] == 'L'  and (b[-1] == 'S' or b[-1] == 'M'):
        print('>')
    elif a[-1] == 'S'  and (b[-1] == 'L' or b[-1] == 'M'):
        print('<')
    elif a[-1] == 'M'  and b[-1] == 'S':
        print('>')
    elif a[-1] == 'M'  and b[-1] == 'L':
        print('<')
    elif a[-1] == 'S'  and b[-1] == 'S':
        if a_length > b_length:
            print('<')
        else:
            print('>')
    elif a[-1] == 'L'  and b[-1] == 'L':
        if a_length > b_length:
            print('>')
        else:
            print('<')
