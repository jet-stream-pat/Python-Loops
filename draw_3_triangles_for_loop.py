# draw 3 triangles
# triangles starting position are different at each iteration

#draw a triangle1
from turtle import *
for sides in range (1, 4):
    forward(40)
    left(120)

# move to next triangle start position
penup()
left(90)
forward(100)
right(90)
pendown()

#draw a triangle2
from turtle import *
for sides in range (1, 4):
    forward(40)
    left(120)

# move to next triangle start position
penup()
right(90)
forward(100)
left(90)
forward(100)
pendown()

#draw a triangle3
from turtle import *
for sides in range (1, 4):
    forward(40)
    left(120)
