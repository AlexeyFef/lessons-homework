#from turtle import *

#my_turtle = Turtle()
#my_turtle.speed(0)
#my_turtle.screen.setup(1200, 800)

# Нарисовать квадрат
#def draw_rect(t):
#    for x in range(0, 4):
#        t.right(90)
#        t.forward(100)

# Рисует квадраты в цикле
#for x in range(0, 72):
#    draw_rect(my_turtle)
#    my_turtle.right(5)

# Необходимо, чтобы окно не закрывалось само, а только по клику
#my_turtle.screen.exitonclick()
#my_turtle.screen.mainloop()


import turtle

# создаем экран
screen = turtle.Screen()
screen.bgcolor("yellow")
screen.setup(600, 600)

# создаем черепаху
cheburashka = turtle.Turtle()
cheburashka.shape("classic")
cheburashka.color("brown")

# рисуем тело чебурашки
cheburashka.penup()
cheburashka.goto(-50, -50)
cheburashka.pendown()
cheburashka.begin_fill()
cheburashka.forward(100)
cheburashka.left(90)
cheburashka.forward(150)
cheburashka.left(90)
cheburashka.forward(100)
cheburashka.left(90)
cheburashka.forward(150)
cheburashka.left(90)
cheburashka.end_fill()

# рисуем голову чебурашки
cheburashka.penup()
cheburashka.goto(0, 100)
cheburashka.pendown()
cheburashka.begin_fill()
cheburashka.circle(30)
cheburashka.end_fill()

# рисуем уши чебурашки
cheburashka.penup()
cheburashka.goto(40, 120)
cheburashka.pendown()
cheburashka.begin_fill()
cheburashka.circle(10)
cheburashka.end_fill()

cheburashka.penup()
cheburashka.goto(-40, 120)
cheburashka.pendown()
cheburashka.begin_fill()
cheburashka.circle(10)
cheburashka.end_fill()

# рисуем глаза чебурашки
cheburashka.penup()
cheburashka.goto(-15, 135)
cheburashka.pendown()
cheburashka.dot(10, "blue")
cheburashka.penup()
cheburashka.goto(15, 135)
cheburashka.pendown()
cheburashka.dot(10, "blue")

# рисуем рот чебурашки
cheburashka.color("green")
cheburashka.penup()
cheburashka.goto(-10, 120)
cheburashka.pendown()
cheburashka.pensize(5)
cheburashka.forward(20)


# скрываем черепаху
cheburashka.hideturtle()

# закрываем окно при клике
screen.exitonclick()
screen.mainloop()