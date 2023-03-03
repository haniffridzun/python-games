# graphics module
import turtle
import os

# window setup
wn = turtle.Screen()
wn.title("Pong by Hanzun")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    # speedup the process

# paddle A: left side
paddle_a = turtle.Turtle()
paddle_a.speed(0)
# resize the shape to 125px height, 25px width
paddle_a.shapesize(5, 1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)  # start position in left side of screen

# paddle B: right side
paddle_b = turtle.Turtle()
paddle_b.speed(0)
# resize the shape to 125px height, 25px width
paddle_b.shapesize(5, 1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)   # start position in right side of screen

# ball
ball = turtle.Turtle()
ball.speed(0)
# default size: 25px by 25px
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)         # start position in middle of screen
ball.dx = 0.2             # ball movement in x-axis, by 2px
ball.dy = 0.2             # ball movement in y-axis, by 2px

# score
score_a = 0
score_b = 0

# display score
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "A  0 : 0  B",
    align="center",
    font=("Courier", 21, "bold")
)


# function for paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# function for paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "j")
wn.onkeypress(paddle_b_down, "l")

# main game loop
while True:
    wn.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # ball bounce off the top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # ball bounce off the bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # ball bounce off the right wall
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1    # score for A
        pen.clear()
        pen.write(
            "A  {} : {}  B".format(score_a, score_b),
            align="center",
            font=("Courier", 21, "bold")
        )

    # ball bounce off the left wall
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1    # score for B
        pen.clear()
        pen.write(
            "A  {} : {}  B".format(score_a, score_b),
            align="center",
            font=("Courier", 21, "bold")
        )

    # ball bounce off the paddle A
    if ball.xcor() < -330 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    # ball bounce off the paddle B
    if ball.xcor() > 330 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
