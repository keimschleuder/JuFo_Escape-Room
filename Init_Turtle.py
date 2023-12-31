import turtle
import os

final_barrier = turtle.Turtle()
final_barrier.speed(0)
final_barrier.hideturtle()
final_barrier.penup()
final_barrier.pensize(4)
final_barrier.color("red")

image_rechts = r"{}\rennt_rechts.gif".format(os.path.dirname(os.path.abspath(__file__)))
image_links = r"{}\rennt_links.gif".format(os.path.dirname(os.path.abspath(__file__)))

def initPlayer():
    # Der Turtle wird eine .gif Datei zugewiesen, als welche die Turtle angezeigt wird
    player = turtle.Turtle()
    player.hideturtle()
    screen = turtle.Screen()
    screen.addshape(image_rechts)
    player.shape(image_rechts)
    # Verhindert, dass die Turtle eine Linie malt
    player.penup()
    player.speed(2)
    return player

def setImage(myTurtle: turtle.Turtle, image):
    screen = turtle.Screen()
    screen.addshape(image)
    myTurtle.shape(image)

def bewegeSpieler(player: turtle.Turtle, dir: str):
    if dir == "a":
        setImage(player, image_links)
    else:
        setImage(player, image_rechts)

def initRoom(number: int):
    room = turtle.Turtle()
    room.speed(0)
    room.hideturtle()
    room.penup()
    room.back(150)
    room.pendown()
    room.pensize(1)

    barrier = turtle.Turtle()
    barrier.speed(0)
    barrier.hideturtle()
    barrier.penup()
    barrier.pensize(4)
    barrier.color("red")

    return_room = [room]

    if number == 0:
        room.left(90)
        room.forward(150)
        room.left(90)
        room.forward(250)
        room.left(90)
        room.forward(45)

        room.right(90)
        room.forward(75)
        room.left(90)
        room.forward(160)
        room.left(90)
        room.penup()
        room.forward(45)
        room.pendown()
        room.left(90)
        room.forward(80)
        room.right(90)
        room.forward(30)
        room.right(90)

        barrier.goto(room.xcor(), room.ycor())
        barrier.pendown()
        barrier.right(90)
        barrier.back(80)
        barrier.penup()

        room.forward(105)
        room.left(90)
        room.forward(250)
        room.left(90)
        room.forward(100)

        xLeft = -400
        xRight = -150
        yTop = 150
        yBottom = -100
        finish = [-480, -100]
        special_room = [0, 0]
        escape = [50]
    elif number == 1:
        room.left(90)
        room.back(50)
        room.forward(300)
        room.left(90)
        room.forward(300)
        room.left(90)
        room.forward(300)
        room.left(90)
        room.forward(220)

        barrier.goto(room.xcor(), room.ycor())
        barrier.pendown()
        barrier.forward(40)
        barrier.penup()

        room.penup()
        room.forward(40)
        room.pendown()
        room.forward(40)
        room.back(40)
        room.right(90)
        room.forward(50)
        room.left(90)
        room.forward(40)

        room.right(90)
        room.forward(200)
        room.right(90)
        room.forward(200)
        room.right(90)
        room.forward(120)

        final_barrier.goto(room.xcor(), room.ycor())
        final_barrier.pendown()
        final_barrier.left(90)
        final_barrier.forward(80)
        final_barrier.penup()

        room.penup()
        room.forward(80)
        room.pendown()

        room.left(30)
        room.forward(58)
        room.back(58)
        room.right(120)

        room.forward(120)
        room.left(90)
        room.forward(50)
        room.right(90)

        xLeft = -450
        xRight = -150
        yTop = 250
        yBottom = -70
        finish = [-235, -145]
        special_room = [0, 0]
        temp_esc = [xLeft, xRight, yTop, yBottom]
        escape = [temp_esc, [[-340, -150, -130, -320], [-230, -150, -70, -130]]]
    elif number == 2:
        xLeft = -450
        xRight = -150
        yTop = 250
        yBottom = -70
#        links, rechts, oben, unten
        connection = [-230, -150, -70, -130]
        bottom_room = [-340, -150, -145, -320]
        special_room = [connection, bottom_room]
        finish = [-430, -140]
        escape = [-150]
    else:
        xLeft = 0
        xRight = 0
        yTop = 0
        yBottom = 0
        finish = [0, 0]
        special_room = [0, 0]
        escape = [0]

    return_room.append(xLeft)
    return_room.append(xRight)
    return_room.append(yTop)
    return_room.append(yBottom)
    return_room.append(finish)
    return_room.append(special_room)
    return_room.append(barrier)

    if number == 2:
        return_room.append(final_barrier)

    return_room.append(escape)
        
    return return_room