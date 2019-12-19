#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Larry Warren
#Date
#12/19/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries

import turtle as trtl 

#create turtle

drawer = trtl.Turtle()
drawer.ht()
drawer.pensize(1)
pen_size = drawer.pensize()


#movement functions

def up():
    drawer.setheading(90)
    drawer.forward(15)
   
def right():
    drawer.setheading(0)
    drawer.forward(15)

def left():
    drawer.setheading(180)
    drawer.forward(15)

def down():
    drawer.setheading(270)
    drawer.forward(15)

#color/drawing functions

def clear():
    wn.resetscreen()
    drawer.reset()
    drawer.ht()

def change():
    global size
    size = drawer.pensize(1)
    size += 1
   

def pen():
    if (drawer.pu == False):
        drawer.pd()
    else:
        drawer.pu()
   






#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(down,"Down")
wn.onkeypress(clear,"space")
wn.onkeypress(change,"o")
wn.onkeypress(pen,"u")
wn.onkeypress(pen,"u")

#listen
wn.listen()

#mainloop
wn.mainloop()