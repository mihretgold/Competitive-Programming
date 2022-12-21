def swap_case(s):
    x=""
    for i in s:
        if i.islower():
           x+=i.upper()
        elif i.isupper():
            x+=i.lower()
        else:
            x+=i
            
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
