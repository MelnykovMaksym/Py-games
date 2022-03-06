import turtle


def sq(x):
    for i in range(4):
        t.color(colors[i % 4])
        t.forward(x)
        t.left(90)


colors = ['red', 'brown', 'green', 'blue']
t = turtle.Turtle()
t.speed(200)

size = 40
for i in range(50):
    t.circle(size)
    sq(size)
    t.right(7)
    size += 3


t.reset()

turtle.down()
turtle.goto(0,300)
turtle.goto(200,300)
turtle.goto(200,0)
turtle.goto(0,0)
turtle.up()
turtle.goto(150,200)
turtle.circle(30)
turtle.down()
turtle.circle(30)
turtle.up()
turtle.goto(50,200)
turtle.circle(30)
turtle.down()
turtle.circle(30)
turtle.up()
turtle.goto(100,200)
turtle.circle(-60,90)
turtle.down()
turtle.circle(-60,180)
turtle.color("blue")
turtle.up()
turtle.circle(-60,90)
turtle.goto(150,200)
turtle.down()
turtle.circle(20)
turtle.up()
turtle.goto(50,200)
turtle.down()
turtle.circle(20)
turtle.up()

turtle.mainloop()

