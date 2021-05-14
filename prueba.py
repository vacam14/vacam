import turtle



vn = turtle.Screen()
vn.title('Famille Mougari par Camilo')
vn.bgcolor('white')
vn.tracer(0)

titre = turtle.Turtle()
titre.speed(0)
titre.color("black")
titre.penup()
titre.hideturtle()
titre.goto(0,250)
titre.write("Famille Mougari", align = "center", font=("Courier", 50, "normal"))


while True:
    vn.update()