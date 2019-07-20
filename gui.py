import turtle as turtle
import main as mn
import random as rand
#JOSUE HERNANDEZ 2019

RADIUS = 220
full_degree= 360
prev = []
length=0
remaining=0




def pie_slice(bill,degree,letter,percentage):
    """assumes circle canvas is already set"""
    global prev
    a = rand.randint(0,200)
    b = rand.randint(0,200)
    c = rand.randint(0,200)
    number= str(percentage)
    if letter=='\t':
        letter="/t"
    elif letter==' ':
        letter="'space'"
    elif letter=='\n':
        letter='/n'
    string="'"+letter+"': "+number[0:5]

    #Nancy helps us create the text by going halfway through the arc and creating label by going away from center
    nancy = turtle.Turtle()
    nancy.up()
    nancy.hideturtle()
    nancy.speed(10)
    nancy.color(a,b,c)
    nancy.setpos(bill.pos())
    nancy.setheading(bill.heading())
    nancy.circle(RADIUS,degree/2)
    nancy.setheading(nancy.towards(0,0))
    nancy.right(180)

    #debug x,y cords to fine tune label placements
    #print(letter,": ",nancy.xcor(),", ",nancy.ycor())

    #at the top it can get crowded so randomly space top labels so you can see them
    if nancy.xcor()<30 and nancy.ycor()>200 and nancy.xcor()>0:
        nancy.forward(rand.randint(5,25))
        nancy.down()
        nancy.write(string, align="center",font=("arial",8,"normal"))
    elif nancy.xcor()>0:
        nancy.forward(10)
        nancy.down()
        nancy.write(string, align="left")
    else:
        nancy.forward(10)
        nancy.down()
        nancy.write(string, align="right")




    bill.fillcolor(a,b,c)
    bill.begin_fill()
    bill.circle(RADIUS,degree)
    prev = bill.pos()
    bill.setpos(0,0)
    bill.end_fill()
    bill.setpos(prev)


def bake_pie(list):
    """call this to start pie_creation"""
    global length
    global remaining
    input=len(list)
    remaining=length= len(mn.file_string)



    canvas = turtle.Screen()
    canvas.title("pie")
    canvas.colormode(255)
    turtle.mode("logo")
    bill = turtle.Turtle()
    if input > 40:
        bill.speed(10)
    elif input>25:
        bill.speed(5)
    else:
        bill.speed(5)
    bill.setpos(0, -RADIUS)
    bill.right(90)
    bill.circle(RADIUS)
    ###above initiates our canvas ready to make the full circle
    for object in list:
        slice= (object[1]/length)*360
        remaining -= object[1]
        pie_slice(bill,slice,object[0],(object[1]/length))
    if remaining:
        slice=(remaining/length)*360
        pie_slice(bill,slice,"other",(remaining/length))

    turtle.done()


