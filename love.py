# -*- coding: cp936 -*-
print('')
print('               1 运行          2 退出')
print('')
i = input('               是否运行：')
while i == 1 :
    
    for y in range(30, -30, -1):
        value = []
        for x in range(-30, 30):
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
                value.append("*")
            else:
                value.append(" ")
            s = "".join(value)
        print s
    print('')
    print('               1 继续          2 退出')
    print('')
    i = input('               是否继续：')
