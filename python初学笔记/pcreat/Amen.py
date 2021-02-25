#coding:utf-8
from turtle import *
speed(0)
pensize(8)
shape('arrow')
setup(900,900)

#maolian
fillcolor('#00A1E8')
begin_fill()
circle(120)
end_fill()

#白脸
pensize(3)
fillcolor('white')
begin_fill()
circle(100)
end_fill()

pu()
home()
goto(0,30)
pd()
for i in range(80):
    left(0.7)
    forward(1)
left(125)
forward(126)
left(120)
for j in range(80):
    left(0.8)
    forward(1)

pu()
home()
goto(1,140)
pd()
fillcolor("red")
begin_fill()
circle(18)
end_fill()


goto(0,100)
goto(0,125)
forward(80)
backward(80)
left(180)
forward(80)
pu()
home()
goto(0,100)
pd()
right(20)
forward(70)
backward(70)
right(140)
forward(70)
left(160)


pu()
goto(0,112)
pd()
right(10)
forward(70)
backward(70)
right(160)
forward(70)
right(160)
left(90)




pu()
home()
goto(-30,165)
pd()
color('black','white')
begin_fill()
a = 0.4
for i in range(120):
    if 0<=i < 30 or 60<=i < 90:
        a = a+0.08
        left(3)
        forward(a)
    else:
        a = a - 0.08
        left(3)
        forward(a)
end_fill()


pu()
goto(30,165)
pd()

color('black','white')
begin_fill()
a = 0.4
for i in range(120):
    if 0<=i < 30 or 60<=i < 90:
        a = a+0.08
        lt(3)
        fd(a)
    else:
        a = a - 0.08
        lt(3)
        fd(a)
end_fill()

pu()
goto(24,195)
fillcolor('black')
begin_fill()
circle(10)
end_fill()
pd()

pu()
goto(-24,195)
fillcolor('black')
begin_fill()
circle(10)
end_fill()
pd()



pu()
goto(-3,-36)
pd()
pensize(2)
color('yellow')
begin_fill()
circle(18)
end_fill()

color('black')
begin_fill()
circle(8)
end_fill()


pu()
goto(-70,12)
pensize(12)
pencolor('red')
pd()
seth(-20)
circle(200,30)
circle(200,10)

right(20)

pu()
pensize(6)
pencolor('#FFC0CB')
goto(0,50)
pd()
forward(26)
backward(26)
left(180)
forward(22)
hideturtle()

done()