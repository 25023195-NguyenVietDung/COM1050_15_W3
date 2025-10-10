a = int(input('Nhập hệ số a: '))
b = int(input('Nhập số tự nhiên b: '))
import math
if a == 0 and b !=0:
    print('Phương trình vô nghiệm.')
else:
    x = -b/a
    ketqua = math.ceil(x*100)/100
    print(ketqua) 
    