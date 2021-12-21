import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
turtle.bgcolor('cyan')
for x in range(90):
    t.pencolor(colors[x%6])
    t.width(x/30+1)
    t.forward(x)
    t.left(30)
