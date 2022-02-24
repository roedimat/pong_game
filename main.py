from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()

screen.setup(width=800, height=600)

screen.bgcolor("black")
screen.title("Pong")

net = Turtle()
screen.tracer(0)

net.penup()
net.goto(0,-300)
net.setheading(90)
net.pencolor("white")
net.speed("fastest")

more_net = True
while more_net:
    net.forward(10)
    net.pendown()
    net.forward(10)
    net.penup()
    if net.ycor() > 300:
        more_net = False

screen.update()
screen.tracer(1)





screen.tracer(0)
r_paddle = Paddle(start_pos=(350, 0))
l_paddle = Paddle(start_pos=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")


# directions = ["left", "right"]

# direction = random.choice(directions)
# if direction == "left":
#     heading = random.randint(135,225)
#     ball.setheading(heading)
# else:
#     heading = random.randint(-45,45)
#     ball.setheading(heading)

game_is_on = True

game_speed = 0.1
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    ball.move()
    

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # detect addle collision
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        game_speed -= .01


    # left scores
    if ball.xcor() > 390:
        time.sleep(1)
        ball.reset_position()
        scoreboard.add_l_point()
        game_speed = 0.1

    # right scores
    if ball.xcor() < -390:
        time.sleep(1)
        ball.reset_position()
        scoreboard.add_r_point()
        game_speed = 0.1


screen.exitonclick()