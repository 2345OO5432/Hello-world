import turtle as T
import math

def set_place(x, y):
    T.penup()
    T.goto(x, y)
    T.pendown()

def star_1(angle, distance):
    set_place(-260, 40)
    T.penup()
    T.seth(180 / math.pi * math.atan(angle))
    T.forward(math.sqrt(distance) - 8)
    T.pendown()
    T.begin_fill()
    for i in range(5):
        T.forward(16 * math.sin(math.pi * 72 / 180))
        T.right(144)
    T.end_fill()

def star_2(i, x):
    T.color("white", "white")
    T.seth(0)
    T.penup()
    T.left(144)
    T.forward(160*0.0616/2)
    T.pendown()
    T.seth(0)
    T.begin_fill()
    for k in range(5):
        T.forward(160 * 0.0616 * math.sin(math.pi * 72 / 180))
        T.right(144)
    T.end_fill()
    T.penup()
    T.seth(-36)
    T.forward(160 * 0.0616 / 2)
    T.setx(x + 0.0633 * 160 * 2 * i)
    T.pendown()

def flag(x, y, l, w, color):
    set_place(x, y)
    T.color(color, color)
    T.begin_fill()
    for i in range(4):
        if i%2==0:
            T.forward(l)
        else:
            T.forward(w)
        T.right(90)
    T.end_fill()

#初始化窗口大小、画布大小、海龟大小、速度
T.setup(width=800, height=600)
T.screensize(canvwidth=800, canvheight=600)
T.pensize(0.1)
T.speed(100)
T.hideturtle()#隐藏海龟
T.pendown()

#绘制中国国旗
#绘制旗体
flag(-300, 80, 240, 160, "red")
set_place(-260, 40)
#绘制主星星
T.penup()
T.seth(144)
T.forward(24)
T.seth(0)
T.pendown()
T.color("yellow", "yellow")
T.begin_fill()
for i in range(5):
    T.forward(48*math.sin(math.pi*72/180))
    T.right(144)
T.end_fill()
#绘制四颗小星星
star_1(3/5, 24**2+40**2)
star_1(1/7, 8**2+56**2)
star_1(-2/7, 16**2+56**2)
star_1(-4/5, 40**2+32**2)

#绘制VS
T.pencolor("black")
set_place(0, -10)
T.write("VS", align="center", font=("consolas", 20))

#绘制美国国旗
color1 = (196, 30, 58)
color2 = (0, 43, 127)
T.colormode(255)
#绘制旗体
T.seth(0)
for i in range(7):
    flag(60, (80-i*2*160/13), 304, 160/13, color1)
#绘制右上角的旗体部分
flag(60, 80, 304*0.4, 160*7/13, color2)
#绘制52颗星星
for i in range(1,10):
    if i%2==1:
        set_place(60+0.0633*160, 80-0.0538*160*i)
        for j in range(1,7):
            star_2(j, 60+0.0633*160)
    else:
        set_place(60+0.0633*160*2, 80-0.0538*160*i)
        for j in range(1,6):
            star_2(j, 60+0.0633*160*2)

T.penup()

T.done()
