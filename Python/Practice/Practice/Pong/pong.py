import winsound
import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Functions
# Left Paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    
# Right Paddle
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
        
# Keybinds
win.listen()
# Left Paddle Controls
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

# Right Paddle Controls
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('Practice\\Pong\\annoyed.wav', winsound.SND_ASYNC)
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound('Practice\\Pong\\annoyed.wav', winsound.SND_ASYNC)

        
    if ball.xcor() > 385:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound('Practice\\Pong\\annoyed.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto (0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound('Practice\\Pong\\annoyed.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    # Paddle Collision
    # Right Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('Practice\\Pong\\annoyed.wav', winsound.SND_ASYNC)

        
    # Left Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('Practice\\Pong\\annoyed.wav', winsound.SND_ASYNC)