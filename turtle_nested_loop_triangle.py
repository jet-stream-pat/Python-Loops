# draw triangles across page
from turtle import *
number_of_shapes = 4 # created the variable and set to 4
for shape in range(1, number_of_shapes + 1):
    for shape in range(1, 5): # draw triangle
        forward(60)
        left(120)
# move to start position of next square
    penup() # note that it's indented as this needs looped
    right(120)
    forward(50)
    pendown()
