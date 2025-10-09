a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if a+b>c and b+c>a and a+c>b:
    print('True')
else:
    print("False")