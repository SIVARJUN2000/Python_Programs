import turtle
t=turtle.Turtle()
xs=[48,117,200,240,160,260,220]
def drawbar(t,height):
    t,begin_fill()
    if(v>=200):
        t.color("blue","red")
    elif(v>=100):
        t.color("blue","yellow")
    else:
        t.color("blue","green")
    t.left(90)
    t.fd(height)
    t.write(""+str(height))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    t.penup()
wn=turtle.screen()
wn.bgcolor("lightgreen")
t.pensize(30)
for v in xs:
    drawbar(t,v)
