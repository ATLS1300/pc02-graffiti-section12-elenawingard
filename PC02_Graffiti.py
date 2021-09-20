#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: elena
september 6, 2021
'''

import turtle
turtle = turtle.Turtle()
wn = turtle.Screen()
wn.bgpic("Bezos.gif")
wn.mainloop()


turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

from Bezos.gif import *
# Draw a circle
color = ('blue')
color('blue')
begin_fill()
circle(270)
end_fill()
turtle.done()



from Bezos.gif import *
# Draw a square
color = ('yellow')
color('yellow')
begin_fill()
forward(271)
left(231)
forward(271)
left(231)
end_fill()
turtle.done()





#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
