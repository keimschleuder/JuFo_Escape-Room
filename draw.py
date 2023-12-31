import time
import turtle as t
from array import array
import math

difficulty_txt = "Wähle den Schwierigkeitsgrad (1 - 9)"
difficulty = 0

plus = array('I', [5, 8, 10, 6, 7, 12, 7, 5, 8, 10])
minus = array('I', [5, 8, 10, 6, 4, 5, 8, 10])
multi = array('I', [5, 8, 10, 17, 5, 8, 4, 10])
divide = array ('I', [5, 15, 10, 17, 5, 16, 10, 17, 5, 15, 4, 10])
zero = array('I', [6, 8, 8, 4, 2, 2, 8, 8])
one = array('I', [5, 11, 10, 8, 8, 1, 5, 4, 10])
two = array('I', [6, 4, 8, 6, 8, 4])
three = array('I', [6, 8, 4, 6, 8, 4])
four = array('I', [5, 6, 10, 8, 8, 2, 4, 8])
five = array('I', [6, 8, 4, 8, 6, 4])
six = array('I', [8, 2, 6, 8, 4, 8, 6, 4])
seven = array('I', [9, 7, 3, 9, 4])
eight = array('I', [6, 8, 4, 8, 6, 2, 4, 2, 8, 8])
nine = array('I', [6, 8, 4, 8, 6, 2, 8, 4])
passing = array('I', [5, 8, 8, 4, 4, 10])
open = array('I', [13])
close = array('I', [14])
gleich = array('I', [5, 15, 10, 6, 4, 5, 16, 10, 6, 4, 5, 15, 10])
rund = array('I', [5, 15, 10, 19, 5, 16, 10, 19, 5, 15, 10])
komma = array('I', [20, 5, 8, 8, 4, 10])

instruction = t.Turtle()
instruction.hideturtle()
instruction.speed(0)
instruction.penup()
instruction.goto(-700, 250)
instruction.pendown()

tu = t.Turtle()
tu.hideturtle()
tu.speed(7)
tu.penup()
tu.goto(-100, 100)
tu.pendown()

difficulty_tu = t.Turtle()
difficulty_tu.hideturtle()
difficulty_tu.penup()
difficulty_tu.speed(0)
difficulty_tu.pensize(10)

standby = t.Turtle()
standby.penup()
standby.hideturtle()

screen = t.Screen()
count = 0

def mySleep(duration: int, myTu:t.Turtle = standby):
    time_end = time.time() + duration
    while time.time() <= time_end:
        myTu.circle(10)

def mode1_fun():
    global difficulty
    difficulty = 1
def mode2_fun():
    global difficulty
    difficulty = 2
def mode3_fun():
    global difficulty
    difficulty = 3
def mode4_fun():
    global difficulty
    difficulty = 4
def mode5_fun():
    global difficulty
    difficulty = 5
def mode6_fun():
    global difficulty
    difficulty = 6
def mode7_fun():
    global difficulty
    difficulty = 7
def mode8_fun():
    global difficulty
    difficulty = 8
def mode9_fun():
    global difficulty
    difficulty = 9

def listen_difficulty():
    screen.listen()
    screen.onkeypress(mode1_fun, "1")
    screen.onkeypress(mode2_fun, "2")
    screen.onkeypress(mode3_fun, "3")
    screen.onkeypress(mode4_fun, "4")
    screen.onkeypress(mode5_fun, "5")
    screen.onkeypress(mode6_fun, "6")
    screen.onkeypress(mode7_fun, "7")
    screen.onkeypress(mode8_fun, "8")
    screen.onkeypress(mode9_fun, "9")

def stop_listen_difficulty():
    screen.listen()
    screen.onkeypress(None, "1")
    screen.onkeypress(None, "2")
    screen.onkeypress(None, "3")
    screen.onkeypress(None, "4")
    screen.onkeypress(None, "5")
    screen.onkeypress(None, "6")
    screen.onkeypress(None, "7")
    screen.onkeypress(None, "8")
    screen.onkeypress(None, "9")

def turn(dir, step, tu: t.Turtle):
    if dir == 1:
        tu.right(130)
        tu.forward(step)
        tu.back(step)
        tu.left(130)
    elif dir == 2:
        tu.right(90)
        tu.forward(step)
        tu.left(90)
    elif dir == 3:
        tu.forward(step /2 + step / 5)
        tu.back(step / 5)
    elif dir == 4:
        tu.back(step)
    elif dir == 5:
        tu.penup()
    elif dir == 6:
        tu.forward(step)
    elif dir == 7:
        tu.back(step / 2)
    elif dir == 8:
        tu.left(90)
        tu.forward(step)
        tu.right(90)
    elif dir == 9:
        tu.goto(tu.xcor() + round(step / 3), tu.ycor() + step)
    elif dir == 10:
        tu.pendown()
    elif dir == 11:
        tu.forward(step / 2)
    elif dir == 12:
        tu.left(90)
        tu.forward(step /2)
        tu.back(step)
        tu.forward(step / 2)
        tu.right(90)
    elif dir == 13:
        tu.penup()
        tu.forward(step / 2)
        tu.right(90)
        tu.forward(step / 2)
        tu.left(90)
        tu.pendown()
        tu.back(step / 2)
        tu.left(90)
        tu.forward(step * 3)
        tu.right(90)
        tu.forward(step / 2)
        tu.penup()
        tu.back(step * 2.4)
        tu.forward(step / 4)
        tu.right(90)
        tu.forward(step / 2)
        tu.left(90)
    elif dir == 14:
        tu.penup()
        tu.back(step)
        tu.left(90)
        tu.back(step / 2)
        tu.right(90)
        tu.pendown()
        tu.forward(step / 2)
        tu.left(90)
        tu.forward(step * 3)
        tu.right(90)
        tu.back(step / 2)
        tu.penup()
        tu.back(step)
        tu.right(90)
        tu.forward(step / 2)
        tu.left(90)
    elif dir == 15:
        tu.left(90)
        tu.forward(step * 0.8)
        tu.right(90)
    elif dir == 16:
        tu.left(90)
        tu.forward(step * 0.4)
        tu.right(90)
    elif dir == 17:
        tu.fillcolor("black")
        tu.begin_fill()
        tu.circle(step / 10)
        tu.end_fill()
    elif dir == 18:
        tu.circle(step)
    elif dir == 19:
        tu.left(45)
        oldX = tu.xcor()
        tu.circle(-10, extent = 90)
        tu.circle(10, extent = 90)
        tu.penup()
        tu.goto(oldX, tu.ycor())
        tu.pendown()
        tu.right(45)
    elif dir == 20:
        tu.right(100)
        tu.forward(step / 2)
        tu.back(step / 2)
        tu.left(100)
    elif dir == 21:
        tu.circle(step - step - step / 2, extent = 180)
        tu.left(180)
    elif dir == 22:
        tu.goto(tu.xcor() + step / 2, tu.ycor() - step)
    elif dir == 23:
        tu.circle(step / 2, extent = 180)
        tu.circle(step - step - step / 2, extent = 180)
    elif dir == 24:
        tu.goto(tu.xcor() + step / 2, tu.ycor() + step)
    elif dir == 25:
        tu.goto(tu.xcor() + step / 2, tu.ycor() - step)
    elif dir == 26:
        tu.circle(step - step - step, extent = 180)
        tu.left(180)
    elif dir == 27:
        tu.pensize(5)
    elif dir == 28:
        tu.pensize(1)
    elif dir == 29:
        tu.left(180)
        tu.circle(step - step- step, extent = 180)
    else:
        print("Error")

def start():
    global count
    if count == 0:
        print("Starting ...")
    count = 1

def set_difficulty():
    global difficulty
    difficulty_tu.goto(-540, 200)

    difficulty_tu.pendown()
    difficulty_tu.write(difficulty_txt, font = ("Arial", 40, "normal"))
    difficulty_tu.penup()

    listen_difficulty()

    while difficulty == 0:
        mySleep(1)

    stop_listen_difficulty()
    difficulty_tu.clear()

    return difficulty

def setFinish(cor: list, step: int, tu: t.Turtle):
    xcor = cor[0]
    ycor = cor[1]
    tu.penup()
    tu.goto(xcor, ycor)
    tu.pendown()
    tu.write("ZIEL", font = ("Arial", int(step * 1.5), "normal"))

def intToDidgits(numb: float):  
    count = 0

    original = numb

    while int(numb) != numb:
        if count == 2:
            break
        numb = numb * 10
        count = count + 1

    if numb == -0:
        numb = 0

    if numb == 10:
        giveBack = [1, 0]
    elif numb == 100:
        giveBack = [1, 0, 0]
    elif numb == 1:
        giveBack = [1]
    elif numb == 0:
        giveBack = [0]
    elif numb == -1:
        giveBack = ["(", "-", 1, ")"]
    elif numb == -10:
        giveBack = ["(", "-", 1, 0, ")"]
    elif numb == -100:
        giveBack = ["(", "-", 1, 0, 0, ")"]
    elif numb < -1:
        number = numb - numb - numb
        giveBack = [(number//(10**i))%10 for i in range(math.ceil(math.log(number, 10))-1, -1, -1)]
        giveBack.insert(0, "-")
        giveBack.insert(0, "(")
        giveBack.append(")")
    elif numb > 1:
        giveBack = [(numb//(10**i))%10 for i in range(math.ceil(math.log(numb, 10))-1, -1, -1)]
    else:
        giveBack = [1] 

    if count > 0:
        if original > 0:
            giveBack.insert(len(giveBack) - count, ",")
        elif original < 0:
            giveBack.insert(len(giveBack) - count - 1, ",")

    return giveBack

def encode(num, operator, step, at: t.Turtle, op = True):
    numbers = intToDidgits(num)
    for myNum in numbers:
        draw(myNum, step, at)
    if op == True:
        draw(operator, step, at)
    elif op == "=":
        draw("=", step, at)
    elif op == "~":
        draw("~", step, at)

def draw(number, step_widh, tur:t.Turtle = tu):
    if number == 0:
        number = zero
    elif number == 1:
        number = one
    elif number == 2:
        number = two
    elif number == 3:
        number = three
    elif number == 4:
        number = four
    elif number == 5:
        number = five
    elif number == 6:
        number = six
    elif number == 7:
        number = seven
    elif number == 8:
        number = eight
    elif number == 9:
        number = nine
    elif number == 10:
        tur.clear()
        tur.penup()
        tur.goto(-100, 100)
        tur.pendown()
        number = passing
    elif number == "-":
        number = minus
    elif number == "+":
        number = plus
    elif number == "(":
        number = open
    elif number == ")":
        number = close
    elif number == "*":
        number = multi
    elif number == "/":
        number = divide
    elif number == "=":
        number = gleich
    elif number == "~":
        number = rund
    elif number == ",":
        number = komma

    for mystep in number:
        turn(mystep, step_widh, tur)

    tur.penup()
    tur.goto(tur.xcor() + step_widh * 2, tur.ycor() - step_widh * 2)
    tur.pendown()