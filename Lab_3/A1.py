x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

if x1==0 or y1==0 or x2==0 or y2==0:
    print('Error')
    exit()
if x1>0 and y1>0 and x2>0 and y2>0:
    print('YES, I')
elif x1 < 0 < y2 and y1 > 0 > x2:
    print('YES, II')
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print('YES, III')
elif x1 > 0 > y1 and x2 > 0 > y2:
    print('YES, IV')
else:
    print('NO')











