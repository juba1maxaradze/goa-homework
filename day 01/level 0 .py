from turtle import*
speed(200)
width(5)
color("purple")
begin_fill()
for i in range(4):
    forward(200)
    left(90)
    end_fill()
#end of square

#drawing door

color("yellow")
begin_fill()
forward(70)
left(90)
forward(100)
left(90)
forward(60)
right(90)
forward(100)
end_fill()
#end of drawing door

#drawing roof

penup()
goto(200, 200)
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing roof

#drawing windows
 penup()
 goto(200, 150)
 pendown()
 color("blue")
 begin_fill()
 for i in range(4):
    forward(30)
    left(90)


goto(0, 150)
 for i in range(4):
    forward(30)
    left(90)
end_fill()

hideturtle()
exitonclick()