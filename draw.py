import turtle
import random

x = 300
y = 0
n = 20
color=['red','green','blue']

for y in range (0, x + n, n):
    turtle.penup()
    turtle.goto(x, 0,)
    turtle.color(color[random.randint(0,2)])
    turtle.pendown()
    turtle.goto(0, y)    
    x -= n
turtle.done()