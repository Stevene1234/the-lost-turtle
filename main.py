import turtle
import random

def onscreen(window, turt):
    '''setting up the window boarder conditions'''
    leftboarder =-window.window_width()/2
    rightboarder = window.window_width() / 2
    topboarder = window.window_height() / 2
    bottomboarder =-window.window_height() / 2


    turtleX = turt.xcor()
    turtleY = turt.ycor()


    isonscreen = True
    if turtleX > rightboarder or turtleX < leftboarder:
       isonscreen = False
    if turtleY > topboarder or turtleY < bottomboarder:
        isonscreen = False

    return onscreen


wn = turtle.Screen()
wn.bgcolor('black')


sarah = turtle.Turtle()
sarah.color('red')
sarah.shape('turtle')

while onscreen(wn,sarah):
    rand = random.randrange(0, 2)
    if rand == 0:
        sarah.left(90)
    else:
        sarah.right(90)

    sarah.forward(50)

wn.exitonclick()