# -*- coding: cp936 -*-
import turtle
import time
 
# �����ĵĶ���
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
 
# �����׵���䣬Ĭ��I Love you
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
love = raw_input('     ����������䣬Ĭ��Ϊ����Ϊ"I Love you": ')
print('')
# ��������������˭��û�в�ִ��
me = raw_input('     �������������˵����������ǳ�: ')
if love == '':
    love = 'I Love you'
# ���ڴ�С
turtle.setup(width=800, height=500)
# ��ɫ
turtle.color('red', 'pink')
# �ʴ�ϸ
turtle.pensize(5)
# �ٶ�
turtle.speed(1)
# ���
turtle.up()
# ���ر�
turtle.hideturtle()
# ȥ��������,��������Ϊ0,0
turtle.goto(0, -180)
turtle.showturtle()
# ������
turtle.down()
turtle.speed(1)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
# ���û�������ߵĶ���
LittleHeart()
# ���û����ұߵĶ���
turtle.left(120)
LittleHeart()
# ������
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.hideturtle()
# ������д�� һ��
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('#CD5C5C', 'pink')
# ������д�� font�������������Լ������еĶ������� align��ʼд�ֵ�λ��
turtle.write(love, font=('gungsuh', 30,), align="center")
turtle.up()
turtle.hideturtle()
time.sleep(2)
# ������д�� ����
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('red', 'pink')
turtle.write(love, font=('gungsuh', 30,), align="center")
turtle.up()
turtle.hideturtle()
# д����
if me != '':
    turtle.color('black', 'pink')
    time.sleep(2)
    turtle.goto(180, -180)
    turtle.showturtle()
    turtle.write(me, font=(20,), align="center", move=True)
 
# ������ڹر�
window = turtle.Screen()
window.exitonclick()
