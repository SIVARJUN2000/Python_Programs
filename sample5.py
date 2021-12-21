from turtle import*
colors=['red','yellow','purple','green','pink']
for x in range(200):
    pencolor(colors[x%5])
    width(x/100+1)
    forward(x)
    left(91)
    
