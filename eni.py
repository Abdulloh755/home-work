
import turtle

window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("Red")

# Пример рисунка
for _ in range(36):
    pen.forward(100)
    pen.left(170)

window.mainloop()