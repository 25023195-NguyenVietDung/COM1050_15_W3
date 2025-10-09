a = int(input('Nhập độ dài cạnh số 1: '))
b = int(input('Nhập độ dài cạnh số 2: '))
c = int(input('Nhập độ dài cạnh số 3: '))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print('Tam giác đều')
    elif a==b or b==c or a==c:
        if a*a+b*b == c*c or b*b+c*c == a*a or a*a+c*c == b*b:
            print('Tam giác vuông cân')
        else:
            print('Tam giác cân')
    elif a*a+b*b == c*c or b*b+c*c == a*a or a*a+c*c == b*b:
        print('Tam giác vuông')
    else:
        print('Tam giác thường')
else:
    print('Không phải tam giác')
    
 