from turtle import *
pendown()
setheading(90)
len = 1
for i in range(60):
    if i < 30:
        len+=0.2
    else:
        len-=0.2
    forward(len)
    left(3)
penup()
done()