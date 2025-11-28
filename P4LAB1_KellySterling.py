import turtle

win = turtle.Screen()
win.bgcolor("lightblue")

t = turtle.Turtle()
t.color("red")
t.pensize(3)

# draw square for the house
for i in range(4):
    t.forward(100)
    t.left(90)

# move turtle to top of the square
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()

# draw triangle roof with while loop
count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count = count + 1

win.mainloop()
