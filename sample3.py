from turtle import*
colors=['red','purple','green','pink']
for x in range(200):
    pencolor(colors[x%4])
    width(x/100+1)
    forward(x)
    left(91)
    
