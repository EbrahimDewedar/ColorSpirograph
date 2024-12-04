import random
import turtle as tur
tim = tur.Turtle()
tur.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fast")

def draw_spiro_graph(gap_size):
    for circle in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spiro_graph(10)
display = tur.Screen()
display.exitonclick()
