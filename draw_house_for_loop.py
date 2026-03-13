#draw a house

#draw a square for wall
from turtle import *
for sides in range(1, 5):
    forward(60)
    left(90)

#move to roof start position
penup()
left(90)
forward(60)
right(90)
pendown()

#draw a triange for roof
for sides in range(1, 4):
   forward(60)
   left(120)

#move to door start position
penup()
right(90)
forward(60)
left(90)
forward(25)
left(90)
pendown()

#draw a square for door
for sides in range(1, 5):
    forward(10)
    right(90)
    
#move to window start position
penup()
forward(40)
right(90)
forward(20)
pendown()

#draw a square for window
for sides in range(1, 5):
    forward(10)
    left(90)
