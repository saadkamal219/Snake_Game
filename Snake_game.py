import turtle 
import time
import random
import os
import tkinter

# snake_head_color = input("Enter the color of snake head: ")
# snake_body_color = input("Enter the color of snake body: ")

snake_head_color = "#eeff03"
snake_body_color = "#20ff03"

sum = 0

f = open("high_score.txt", "r")

delay = 0.1
speed_of_snake = 10
score = 0
high_score = int(f.read())
f.close()

#set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0) #turns off the animation no the screen

#game code start here

#Creating custom shapes

#directing the image path
# os.chdir("/home/saad/Desktop/VS-Code_Workplace/Project/python/OOP_2_Project")
# turtle.register_shape("snake_head.gif")

#Snake Head
snake_head = turtle.Turtle()
snake_head.speed(0) #fastest animation speed, no delay at all
snake_head.shape("square")
snake_head.left(90)
snake_head.fillcolor(snake_head_color)
snake_head.pencolor(snake_head_color)
snake_head.penup() #does not draw anything on the screen
snake_head.goto(0,0)
snake_head.direction = "stop"

#Snake Food
snake_food = turtle.Turtle()
snake_food.speed(0) #fastest animation speed, no delay at all
snake_food.shape("turtle")
snake_food.color("red")
snake_food.penup() #does not draw anything on the screen
snake_food.goto(0,100)

#Snake Body
segments = []

#Score Writing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,255)
f5 = open("high_score.txt", "r")
s = open("last_score.txt", "r")
pen.write("Score: {} | Last Score: {} | High Score: {}".format(0, s.read(), f5.read()), align="center", font=("courier", 16, "normal"))
f5.close()
s.close()

#score board to snake pit difference
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0,225)
pen1.write("-----------------------------------------------------", align="center", font=("courier", 24, "bold"))

# functions
def move():

    if snake_head.direction == "up":
        y_axis = snake_head.ycor()
        snake_head.sety(y_axis + speed_of_snake)
    
    if snake_head.direction == "down":
        y_axis = snake_head.ycor()
        snake_head.sety(y_axis - speed_of_snake)

    if snake_head.direction == "left":
        x_axis = snake_head.xcor()
        snake_head.setx(x_axis - speed_of_snake)

    if snake_head.direction == "right":
        x_axis = snake_head.xcor()
        snake_head.setx(x_axis + speed_of_snake)

def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
    # snake_head.left(90)


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"
    # snake_head.left(270)

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
    # snake_head.left(180)

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"
    # snake_head.left(0)
        
#keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

sum = 0

#main game loop

while True:
    window.update()

    #check for collision with the border
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 220 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"

        #hide the segments:
        for segment in segments:
            segment.goto(1000,1000)
        
        #clear the segments list
        segments.clear()

        sw = open("last_score.txt", "w")
        last_score_str = str(score)
        sw.write(last_score_str)
        sw.close()

        #reset the score
        score = 0

        #reset the delay
        delay = 0.1

        pen.clear()
        f1 = open("high_score.txt", "r")
        s3 = open("last_score.txt", "r")
        pen.write("Score: {} | Last Score: {} | High Score: {}".format(score, s3.read(), f1.read()), align = "center", font = ("courier", 16, "normal"))
        f1.close()
        s3.close()

    #check for a collision with the food
    if snake_head.distance(snake_food) < speed_of_snake:

        #move the food to a random spot of the module
        x = random.randint(-250, 250)
        y = random.randint(-250, 200)
        snake_food.left(random.randint(-360, 360))
        snake_food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.fillcolor(snake_body_color)
        new_segment.pencolor("black")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001

        #increase the score
        score += 1

        if score > high_score:
            high_score = score

        f2 = open("high_score.txt", "w")
        high_score_str = str(high_score)
        f2.write(high_score_str)
        f2.close()

        pen.clear()
        f3 = open("high_score.txt", "r")
        s2 = open("last_score.txt", "r")
        pen.write("Score: {} | Last Score: {} | High Score: {}".format(score, s2.read(), f3.read()), align = "center", font = ("courier", 16, "normal"))
        f3.close()
        s2.close()

    #check for colision with the body
    for segment in segments:
        if segment.distance(snake_head) < 10:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"

            #hide the segments:
            for segment in segments:
                segment.goto(1000,1000)
        
            #clear the segments list
            segments.clear()

            sw2 = open("last_score.txt", "w")
            last_score_str = str(score)
            sw2.write(last_score_str)
            sw2.close()

            #reset the score
            score = 0

            #reset the delay
            delay = 0.1

            pen.clear()
            f4 = open("high_score.txt", "r")
            s4 = open("last_score.txt", "r")
            pen.write("Score: {} | Last Score: {} | High Score: {}".format(score, s4.read(), f4.read()), align = "center", font = ("courier", 16, "normal"))

    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    #move segment 0 to here the head is
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)
    
    move()

    time.sleep(delay) #stops the program

#game code end here

window.mainloop() #keep the game window open for user
