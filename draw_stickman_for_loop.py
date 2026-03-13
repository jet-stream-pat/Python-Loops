# draw stickperson

# draw square (head)
from turtle import *
for sides in range(1, 5):
    forward(40)
    left(90)

# move to torso start position
penup()
forward(20)
right(90)
pendown()

# draw line (torso)
forward(90)

# move to r/leg start position
penup()
left(45)
pendown()

# draw line (r/leg)
forward(75)

# move to l/leg start position
penup()
left(180)
forward(75)
left(90)
pendown()

# draw line (l/leg)
forward(75)

# move to r/arm start position
penup()
left(180)
forward(75)
left(45)
forward(45)
right(90)
pendown()

# draw line (r/arm)
forward(45)

# move to l/arm start position
penup()
left(180)
forward(45)
pendown()

# draw line (l/arm)
forward(45)


