n = int(input('Nhập 1 năm bắt kỳ: '))
if n>0:
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print ('Năm nhuận')
    else:
        print('Năm không nhuận')
else:
    print('Nhập lại')