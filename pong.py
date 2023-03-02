# graphics module
import turtle

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
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "j")
wn.onkeypress(paddle_b_down, "l")
wn.listen()

# main game loop
while True:
    wn.update()
