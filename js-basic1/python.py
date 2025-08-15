import math
import time
from turtle import *

def heart_x(k):
    return 15 * math.sin(k)**3

def heart_y(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

def draw_heart(scale):
    penup()
    goto(heart_x(0)*scale, heart_y(0)*scale)
    pendown()
    begin_fill()
    for i in range(1, 601):
        k = math.radians(i)
        x = heart_x(k) * scale
        y = heart_y(k) * scale
        goto(x, y)
    end_fill()

# ตั้งค่า
bgcolor("black")
speed(0)
hideturtle()
color("red")
fillcolor("red")

# เต้นเป็นจังหวะ
while True:
    for size in [20, 21, 22, 21, 20]:  # ขยายแล้วหด
        clear()
        draw_heart(size)
        time.sleep(0.1)
        from turtle import *

bgcolor("black")
color("red")
begin_fill()
circle(100, 180)
left(90)
circle(100, 180)
end_fill()

done()
