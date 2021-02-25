from turtle import *
speed(10)
pensize(8)

setup(900,900)

#maolian
fillcolor('#00A1E8')
begin_fill()
circle(120)
end_fill()

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


done()