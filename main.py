import turtle




screen = turtle.Screen()


screen.setup(800, 800)


screen.bgcolor('silver')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)
t.penup()
t.goto(-50,200)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Anthony Pirring", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")


t.showturtle()
t.clear()


t.penup()
t.goto(0,200)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")


turtle.addshape("chicken.gif")
t.shape("chicken.gif")
t.goto(-300,0)
a = t.stamp()
t.hideturtle()
t.write("Chicken", font=("arial", 30, "bold"), align="center")


turtle.addshape("hibachi.gif")
t.shape("hibachi.gif")
b = t.stamp()
t.write("hibachi", font=("arial", 30, "bold"), align="center")
turtle.addshape("taco.gif")
t.shape("taco.gif")
c = t.stamp()
    )
t.write("taco", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
screen.bgcolor('magenta')
t.clear()
t.clearstamps()

t.penup()
t.write("My favorite hobbies", font=("arial", 30, "bold"), align="center")


turtle.addshape("quad.gif")
t.shape("quad.gif")
a = t.stamp()
t.hideturtle()
t.write("quad riding", font=("arial", 30, "bold"), align="center")

turtle.addshape("travel.gif")
t.shape("travel.gif")
a = t.stamp()
t.hideturtle()
t.write("travel", font=("arial", 30, "bold"), align="center")

turtle.addshape("Basketball.gif")
t.shape("Basketball.gif")
b = t.stamp()
t.write("Basketball", font=("arial", 30, "bold"), align="center")
turtle.addshape("ps5.gif")
t.shape("ps5.gif")
c = t.stamp()
    )
t.write("video games", font=("arial", 30, "bold"), align="center")






turtle.done()

