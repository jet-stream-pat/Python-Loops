# draw squares across page
from turtle import *
number_of_shapes = 4 # created the variable and set to 4
for shape in range(1, number_of_shapes + 1):
    for shape in range(1, 5): # draw square
        forward(40)
        right(90)
# move to start position of next square
    penup() # note that it's indented as this needs looped
    forward(100)
    pendown()
