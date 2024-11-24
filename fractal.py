
import turtle
import random
import tkinter

root = tkinter.Tk()

def draw_tree(t, branch_length, angle, level):
    if level <= 0:
        return

    t.pensize(level)
    t.pencolor("brown")

    t.forward(branch_length)

    if level == 1:
        t.pencolor("#ec407a")  
        t.dot(25)
        t.pencolor("brown")

    t.left(angle)
    draw_tree(t, branch_length * 0.9, angle, level - 1)
    t.right(2 * angle)
    draw_tree(t, branch_length * 0.7, angle, level - 1)
    t.left(angle)
    t.backward(branch_length)

def animate_leaves(num_leaves):
    leaves = []
    for _ in range(num_leaves):
        leaf = turtle.Turtle()
        leaf.shape("circle")
        leaf.color("#ec407a")  
        #leaf.hideturtle()
        leaf.penup()
        leaf.speed(100)

        start_x = random.randint(-100, 200)
        start_y = random.randint(50, 200)
        leaf.goto(start_x, start_y)
        leaves.append(leaf)

    while any(leaf.ycor() > -200 for leaf in leaves):
        for leaf in leaves:
            if leaf.ycor() > -200:
                leaf.sety(leaf.ycor() - random.randint(3, 8))
        turtle.update()
        turtle.delay(20)


def animate_snow(num_flakes):
   
    snowflakes = []
    for _ in range(num_flakes):
        flake = turtle.Turtle()
        flake.shape("circle")
        flake.color("white")
       # flake.hideturtle()
        flake.penup()
        flake.speed(100)

        start_x = random.randint(-500, 500)
        start_y = random.randint(-500, 500)
        flake.goto(start_x, start_y)
        snowflakes.append(flake)

    while True:
        for flake in snowflakes:
            if flake.ycor() > -200:
                flake.sety(flake.ycor() - random.randint(3, 8))
        turtle.update()
        turtle.delay(20)
    #return animate_snow()

def draw_WinterTree(t, branch_length, angle, level):
    if level <= 0:
        return
    if level == 1:
        t.pencolor("#ec407a")  
        
        t.pencolor("brown")
    t.pensize(level)
    t.pencolor("brown")

    t.forward(branch_length)

    
    t.left(angle)
    draw_WinterTree(t, branch_length * 0.9, angle, level - 1)
    t.right(2 * angle)
    draw_WinterTree(t, branch_length * 0.7, angle, level - 1)
    t.left(angle)
    t.backward(branch_length)


def spring():
    t.clear()
    screen = turtle.Screen()
    #screen.title("")
    screen.bgcolor("#196f3d")
    screen.bgpic("download.gif")
    screen.setup(width=800, height=600)
  
    draw_tree(t, 100, 30, 10)
    animate_leaves(num_leaves=15)

def winter():
    t.clear()
    screen = turtle.Screen()
    #screen.title("")
    screen.bgcolor("#ADD8E6")
    screen.bgpic("download.gif")
    screen.setup(width=800, height=600)
   
    draw_WinterTree(t, 100, 30, 10)
    label =tkinter.Label(root, text="Here comes the snow storm!")
    label.pack()
    animate_snow(num_flakes=50)
   



screen = turtle.Screen()
screen.bgcolor("#196f3d")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.hideturtle()
t.left(90)
t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()


label = tkinter.Label(root, text="Click on a season!")
label.pack()


Wbutton = tkinter.Button(root, text="Spring", command=spring)
Wbutton.pack()

Lbutton = tkinter.Button(root, text="Winter", command=winter)
Lbutton.pack()

root.mainloop()