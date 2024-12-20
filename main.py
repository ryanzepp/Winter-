import turtle




screen=turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')




t_ground=turtle.Turtle()
t_ground.speed(0)
t_ground.pencolor('white')
t_ground.fillcolor('white')
#Ground


t_tree=turtle.Turtle()
t_tree.speed(0)
t_tree.pencolor('green')
t_tree.fillcolor('green')
#tree


t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

#christmas tree
t_tree.hideturtle()
t_tree.penup()
t_tree.goto(0,75)
t_tree.pendown()
t_tree.begin_fill()
t_tree.goto(40,25)
t_tree.goto(-40,25)
t_tree.goto(0,75)
t_tree.end_fill()
t_tree.penup()
t_tree.goto(0,50)
t_tree.pendown()
t_tree.begin_fill()
t_tree.goto(55,0)
t_tree.goto(-55,0)
t_tree.goto(0,50)
t_tree.end_fill()
t_tree.penup()
t_tree.goto(0,25)
t_tree.pendown()
t_tree.begin_fill()
t_tree.goto(70,-25)
t_tree.goto(-70,-25)
t_tree.goto(0,25)
t_tree.end_fill()
t_tree.penup()
t_tree.goto(0,0)
t_tree.pendown()
t_tree.begin_fill()
t_tree.goto(80,-50)
t_tree.goto(-85,-50)
t_tree.goto(0,0)
t_tree.end_fill()
t_tree.penup()
t_tree.pencolor('saddle brown')
t_tree.fillcolor('saddle brown')
t_tree.goto(15,-50)
t_tree.pendown()
t_tree.begin_fill()
t_tree.goto(-15,-50)
t_tree.goto(-15,-100)
t_tree.goto(15,-100)
t_tree.goto(15,-50)
t_tree.end_fill()
t_tree.penup()
#Christmas ornements
t_tree.goto(0, -20)
t_tree.pendown()
t_tree.begin_fill()
t_tree.circle(10)
t_tree.end_fill()




t_tree.penup()
t_tree.color("purple")
t_tree.fillcolor("purple")
t_tree.goto(25, -40)
t_tree.pendown()
t_tree.begin_fill()
t_tree.circle(10)
t_tree.end_fill()


t_tree.penup()
t_tree.color("red")
t_tree.fillcolor("red")
t_tree.goto(-9, 20)
t_tree.pendown()
t_tree.begin_fill()
t_tree.circle(10)
t_tree.end_fill()


t_tree.penup()
t_tree.color("yellow")
t_tree.fillcolor("yellow")
t_tree.goto(-30, -40)
t_tree.pendown()
t_tree.begin_fill()
t_tree.circle(10)
t_tree.end_fill()
t_tree.penup()
t_tree.color("red")
t_tree.fillcolor("red")






t_tree.penup()
t_tree.color("silver")
t_tree.fillcolor("silver")
t_tree.goto(15, 10)
t_tree.pendown()
t_tree.begin_fill()
t_tree.circle(10)
t_tree.end_fill()





#rectangle
t_tree.penup()
t_tree.goto(-300,-100)
t_tree.pendown()
t_tree.fillcolor('peru')
t_tree.begin_fill()
t_tree.forward(200)
t_tree.left(90)
t_tree.forward(200)
t_tree.left(90)
t_tree.forward(200)
t_tree.left(90)
t_tree.forward(200)
t_tree.left(90)
t_tree.end_fill()

#triangle
t_tree.penup()
t_tree.goto(-300,100)
t_tree.pendown()

t_tree.fillcolor('saddle brown')
t_tree.begin_fill()
t_tree.goto(-100,100)
t_tree.goto(-200,200)
t_tree.goto(-300,100)
t_tree.end_fill()

#snowman
t1 = turtle.Turtle()
t1.speed(0)
t1.penup()
t1.goto(125,-100)
t1.pencolor('white')
t1.fillcolor('white')
t1.begin_fill()
t1.pendown()
t1.circle(25)
t1.end_fill()
t1.penup()
t1.goto(125,-60)
t1.begin_fill()
t1.pendown()
t1.circle(15)
t1.end_fill()
t1.penup()
t1.goto(125,-35)
t1.begin_fill()
t1.pendown()
t1.circle(10)
t1.end_fill()
t1.penup()
t1.pencolor('orange')
t1.fillcolor('orange')
t1.goto(125,-23)
t1.shapesize(1)
t1.setheading(180)
t1.begin_fill()
t1.pendown()
t1.circle(2.5,180)
t1.goto(135,-24.5)
t1.goto(125,-23)
t1.end_fill()
t1.penup()
t1.pencolor('black')
t1.fillcolor('black')
t1.goto(120,-23)
t1.shapesize(1)
t1.setheading(0)
t1.begin_fill()
t1.pendown()
t1.circle(1.5)
t1.end_fill()
t1.penup()
t1.goto(130,-23)
t1.shapesize(1)
t1.setheading(0)
t1.begin_fill()
t1.pendown()
t1.circle(1.5)
t1.end_fill()
t1.penup()
t1.hideturtle()

#Candycane
t1.penup()
t1.goto(200,-100)
t1.pendown()
t1.pensize(10)
t1.pencolor('red')
t1.goto(200,0)
t1.setheading(90)
t1.circle(25,180)
for i in range(9):
    t1.penup()
    if i%2 ==0:
        t1.pencolor('red')
    else:
        t1.pencolor('white')
    t1.pensize(10)
    t1.goto(200,-100+i*10)
    t1.pendown()
    t1.goto(200,-90+(i+1)*10)

t1.pensize(1)

#star
star = turtle.Turtle()
star.penup()
star.goto(-25, 90)
star.pendown()
t1.hideturtle()
star.pencolor('yellow')
star.fillcolor('yellow')
star.begin_fill()


for i in range(5):
   star.forward(50)
   star.right(144)


star.end_fill()


#present
t_tree.penup()
t_tree.goto(210,-22)
t_tree.pendown()
t_tree.fillcolor('red')
t_tree.begin_fill()
t_tree.forward(80)
t_tree.right(90)
t_tree.forward(80)
t_tree.right(90)
t_tree.forward(80)
t_tree.right(90)
t_tree.forward(80)
t_tree.right(90)
t_tree.end_fill()

t1.penup()
t1.goto(0,200)
t1.write("Merry Christmas",font=("arial",20,"bold"),align="center")



#last line of code
turtle.done()
