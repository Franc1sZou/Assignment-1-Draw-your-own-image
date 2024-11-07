from turtle import *


def draw_doraemon():
    speed(10)

    # Draw the blue face
    penup()
    goto(0, -60)
    pendown()
    color('#0093dd')
    begin_fill()
    circle(75)
    end_fill()

    # Draw the white face
    penup()
    goto(0, -50)
    pendown()
    color('white')
    begin_fill()
    circle(60)
    end_fill()

    # Draw the right eye white
    draw_eye_white_circle(15)

    # Draw the right eye black
    draw_eye_black_circle(6)

    # Draw the left eye white
    draw_eye_white_circle(-15)

    # Draw the left eye black
    draw_eye_black_circle(-24)

    # Draw the nose
    penup()
    goto(0, -5)
    pendown()
    color('#c70000')
    begin_fill()
    circle(8)
    end_fill()

    # Draw the mouth
    penup()
    goto(-30, -20)
    seth(-60)
    pendown()
    color('black')
    circle(30, 120)

    # Draw the line connecting the nose and mouth
    penup()
    goto(0, -5)
    seth(-90)
    pendown()
    fd(30)

    # Draw whiskers on the left side
    draw_whisker(-55, 0)
    draw_whisker(-55, -10)
    draw_whisker(-55, 10)

    # Draw whiskers on the right side
    draw_whisker(25, 0)
    draw_whisker(25, -10)
    draw_whisker(25, 10)


def draw_eye_white_circle(x):
    penup()
    goto(x, 25)
    pendown()
    color('black')
    begin_fill()
    circle(15)
    color('white')
    end_fill()


def draw_eye_black_circle(x):
    penup()
    goto(x, 40)
    pendown()
    color('black')
    begin_fill()
    circle(6)
    end_fill()


def draw_whisker(x, y):
    penup()
    goto(0, -15)
    seth(0)
    goto(x, y)
    pendown()
    color('black')
    fd(30)


# Start drawing Doraemon
draw_doraemon()

hideturtle()
done()
