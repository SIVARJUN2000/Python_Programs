import turtle
turtle.setup(400,500)
wn=turtle.Screen()
wn.title("Handling key press events")
wn.bgcolor("pink")
tess=turtle.Turtle()
def h1():
    tess.forward(30)
def h2():
    tess.left(45)
def h3():
    tess.right(45)
def h4():
    wn.bye()
wn.onkey(h1,"up")
wn.onkey(h2,"Left")
wn.onkey(h3,"right")
wn.onkey(h4,"q")
wn.listen()
wn.mainloop()
    
