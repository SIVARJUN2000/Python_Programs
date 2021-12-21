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
    
wn.onKey(h1, "up")
wn.onKey(h2, "Left")
wn.onKey(h3, "right")
wn.onKey(h4, "q")

wn.listen()
wn.mainloop()
    
