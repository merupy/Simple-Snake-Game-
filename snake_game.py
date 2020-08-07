import turtle
import time
import random

delay = 0.05
body=[]
#For Screen
wn = turtle.Screen()
wn.title("Snake Game by Meru ")
wn.bgcolor("black")
wn.setup(width=600, height=600)


#For Score
score1 = 0
hscore= 0


#Score display
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("yellow")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Score: 0   High Score:0", align="center", font="45")


#Food
food= turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

#For Snake Head
head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

#motion
def move():
    if head.direction == "up":
        yaxis= head.ycor()
        head.sety(yaxis + 20)

    if head.direction == "down":
        yaxis= head.ycor()
        head.sety(yaxis - 20)
    
    if head.direction == "left":
        xaxis= head.xcor()
        head.setx(xaxis - 20)
    if head.direction == "right":
        xaxis= head.xcor()
        head.setx(xaxis + 20)

#direction
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

#keyboard bindings 

wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
 

#Game Loop
while True:
    wn.update()

    #Border collision check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.drection = "stop"

        #For hiding segments
        for x in body:
            x.goto(1000, 1000)

        #clear segments
        body.clear()

        #clear score
        score1 = 0
        score.clear()
        score.write("Score: {} High Score: {}".format(score1, hscore), align="center", font="45")
    
    #head and food
    if head.distance(food) < 20:
        food.goto((random.randint(-290, 290)), (random.randint(-290, 290)))

        #For snake Body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("gray")
        new_body.penup()
        body.append(new_body)
        delay -=0.001

        #Increase score
        score1 += 1

        if score1 > hscore:
            hscore = score1

        score.clear()
        score.write("Score: {} High Score: {}".format(score1, hscore), align="center", font="45")   
         
    for index in range(len(body)-1, 0, -1):
        x= body[index-1].xcor()
        y= body[index-1].ycor()
        body[index].goto(x,y)

    if len(body) > 0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()

    #Head collision with body
    for x in body:
        if x.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #For hiding segments 
            for x in body:
                x.goto(1000, 1000)

            #clear segments
            body.clear()

            #clear score
            score1= 0
            score.clear()
            score.write("Score: {} High Score: {}".format(score1, hscore), align="center", font="45")


    time.sleep(delay)

wn.mainloop()