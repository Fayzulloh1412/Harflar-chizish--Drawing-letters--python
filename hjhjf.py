from turtle import *

speed(1)
hideturtle()
tracer(5)
bgcolor('black')
for i in range(60):
    color('cyan')
    for n in range(6):
        forward(100)
        left(60)
    left(6)
    
done()