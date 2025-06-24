name = input()
a = float(input())
b = float(input())
if name == '+':

    print(a+b)

elif name == '-':

    print(a-b)

elif name == '*':
    print(a*b)
elif name == '/':
    if b==0:
        print('zero division error')
    else:
        print(a/b)

else : print('종료')