from openpyxl import load_workbook
wb = load_workbook('F:\data2.xlsx')
ws = wb.active
n = 100000  #������
i = 100  #��Ⱦ����
s = n -i  #δ��Ⱦ����/�׸�Ⱦ����
a = 0.03  #��Ⱦ��
b = 0.5  #�ָ���
times = 0
while(times>100000 or i >= n or n <=0):
    it = s*a*i/n
    r = i*b
    i = it + i - r
    times=times + 1
    ws.cell(row=times,column=1).value=i
    wb.save('F:\data2.xlsx')
    print i