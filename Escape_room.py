from enum import Enum
from turtle import *
import turtle
import draw
import random
import time
import Init_Turtle

class Directions(Enum):
    RIGHT = "d"
    LEFT = "a"
    UP = "w"
    DOWN = "s"
    ARROW_UP = "Up"
    ARROW_DOWN = "Down"
    ARROW_RIGHT = "Right"
    ARROW_LEFT = "Left"

turtle.setup(1.0, 1.0)

turtle.title("Escaperoom")
screen = turtle.Screen()
screen.bgcolor("lightgrey")

step = 40
player_step = 5
task_step = 20

at = turtle.Turtle()
at.hideturtle()
at.speed(0)
at.penup()
at.goto(-100, 0)
at.pendown()

fin = turtle.Turtle()
fin.hideturtle()
fin.speed(0)

eingabe = []
komma = False
klammer_zu = False

player_orienatation = Directions.RIGHT.value

willContinue = True

difficulty = 0
mode1 = {"+1": 1, "+2": 4, "-1": 1, "-2": 7, "-3": 9, "*1": None, "*2": None, "/1": None, "/2": None, "/3": None, "n": 2}
mode2 = {"+1": 0, "+2": 10, "-1": 0, "-2": 10, "-3": 50, "*1": None, "*2": None, "/1": None, "/2": None, "/3": None, "n": 2}
mode3 = {"+1": 0, "+2": 20, "-1": 0, "-2": 15, "-3": 50, "*1": 1, "*2": 5, "/1": None, "/2": None, "/3": None, "n": 2}
mode4 = {"+1": 0, "+2": 40, "-1": 0, "-2": 40, "-3": 200, "*1": 1, "*2": 5, "/1": 1, "/2": 4, "/3": 12, "n": 3}
mode5 = {"+1": 0, "+2": 50, "-1": 0, "-2": 30, "-3": 75, "*1": 1, "*2": 10, "/1": 1, "/2": 4, "/3": 12, "n": 3}
mode6 = {"+1": -25, "+2": 50, "-1": -25, "-2": 50, "-3": 50, "*1": -5, "*2": 10, "/1": -10, "/2": 10, "n": 3}
mode6["/3"] = random.randint(mode6["/1"], mode6["/2"] + 40)
mode7 = {"+1": -30, "+2": 60, "-1": -30, "-2": 60, "-3": 70, "*1": -5, "*2": 10, "/1": -5, "/2": 10, "n": 4}
mode7["/3"] = random.randint(mode6["/1"], mode6["/2"] + 50)
mode8 = {"+1": -50, "+2": 75, "-1": -50, "-2": 75, "-3": 100, "*1": -10, "*2": 12, "/1": -10, "/2": 15, "n": 4}
mode8["/3"] = random.randint(mode8["/1"], mode8["/2"] + 50)
mode9 = {"+1": -60, "+2": 90, "-1": -60, "-2": 90, "-3": 100, "*1": -12, "*2": 12, "/1": -10, "/2": 15, "n": 4}
mode9["/3"] = random.randint(mode9["/1"], mode9["/2"] + 50)

modes = [None, mode1, mode2, mode3, mode4, mode5, mode6, mode7,  mode8, mode9]

code0 = [2, 0, 2, 3]
code1 = [5, 1, 3, None]
code2 = [0, 7, 5, None]
codes = [code0, code1, code2]

et1 = turtle.Turtle()
et1.hideturtle()
et1.speed(0)
et1.penup()
et1.goto(at.xcor(), at.ycor())
et1.color("blue")

et2 = turtle.Turtle()
et2.hideturtle()
et2.speed(0)
et2.penup()
et2.goto(at.xcor(), at.ycor())
et2.color("blue")

et3 = turtle.Turtle()
et3.hideturtle()
et3.speed(0)
et3.penup()
et3.goto(at.xcor(), at.ycor())
et3.color("blue")

et4 = turtle.Turtle()
et4.hideturtle()
et4.speed(0)
et4.penup()
et4.goto(at.xcor(), at.ycor())
et4.color("blue")

ets = [et1, et2, et3, et4]

res = 6300000

standby = turtle.Turtle()
standby.hideturtle()
standby.penup()

# Quiz init:
class Belohnungszahl:
    def __init__(self, wert) -> None:
        self.wert = wert

    def getWert(self):
        return self.wert
    
    def getAufgabe(self):
        return self

class ReverseLookup:
    def __getattribute__(self, attr):
        if attr.startswith('__'):
            return super().__getattribute__(attr)
        cls = self.__class__
        if attr in self.__dict__:
            return self.__dict__[attr]
        for base in cls.__mro__[-3::-1]:
            if attr in base.__dict__:
                value = base.__dict__[attr]
                # handle descriptors
                if hasattr(value, '__get__'):
                    return value.__get__(self, cls)
                else:
                    return value
        raise AttributeError("Attribute {} not found".format(attr))

class Aufgabe(ReverseLookup):
    def __init__(self, num1, num2, num3, num4, nums) -> None:
        self.numb1 = num1
        self.numb2 = num2
        self.numb3 = num3
        self.numb4 = num4
        self.numUsed = nums

    def calculate(self, insertion):
        insert = round(insertion, 2)
        new_sol = self.getLoesung()
        if insert == new_sol:
            return True
        else:
            return False

    def whereEqual(self):
        if self.numUsed == 2:
            return [True, "=", True, True]
        elif self.numUsed == 3:
            return [True, True, "=", True]
        else:
            return [True, True, True, "="]

    def getLoesung(self):
        num1 = round(self.numb1, 2)
        num2 = round(self.numb2, 2)
        num3 = round(self.numb3, 2)
        num4 = round(self.numb4, 2)
        solution = self.__class__.calc(self, num1, num2, num3, num4)
        new_sol = round(solution, 2)
        return new_sol

class Addition(Aufgabe):
    def __init__(self, num1, num2, num3 = 0, num4 = 0, nums = 2) -> None:
        super().__init__(num1, num2, num3, num4, nums)

    operator = "+"

    def calc(self, num1, num2, num3, num4):
        solution = num1 + num2 + num3 + num4
        return solution
class Substract(Aufgabe):
    def __init__(self, num1, num2, num3 = 0, num4 = 0, nums = 2) -> None:
        super().__init__(num1, num2, num3, num4, nums)

    operator = "-"

    def calc(self, num1, num2, num3, num4):
        solution = num1 - num2 - num3 - num4
        return solution
class Multiply(Aufgabe):
    def __init__(self, num1, num2, num3 = 1, num4 = 1, nums = 2) -> None:
        super().__init__(num1, num2, num3, num4, nums)

    operator = "*"

    def calc(self, num1, num2, num3, num4):
        solution = num1 * num2 * num3 * num4
        return solution
class Divide:
    def __init__(self, num1, num2, nums = 2) -> None:
        self.numb1 = num1
        self.numb2 = num2
        self.numUsed = nums

    operator = "/"

    def calculate(self, insertion):
        if self.numb2 != 0:
            new_sol = self.getLoesung()
            insert = round(insertion, 2)
            if insert == new_sol:
                return True
            else:
                return False
        else:
            print("Error")
            return True

    def getLoesung(self):
        if self.numb2 != 0:
            num1 = round(self.numb1, 2)
            num2 = round(self.numb2, 2)
            solution = num1 / num2
            new_sol = round(solution, 2)
        else: 
            new_sol = 0
        return new_sol

    def isDecimal(self):
        if int(self.getLoesung()) == float(self.getLoesung()):
            return "="
        else:
            return "~"

class Quizteil:
    def __init__(self, aufgabe, belohnungszahl: Belohnungszahl) -> None:
        self.aufgabe = aufgabe
        self.belohnung = belohnungszahl

    def getAufgabe(self):
        return self.aufgabe

    def belohnen(self):
        return self.belohnung

def initQuiz(runde: int):
    global difficulty, modes, appended
    myMode = modes[difficulty]
    myquiz = []
    belohnungszahlen = []
    classes = [Addition, Substract, Multiply]

    for i in range(4):
        belohnungszahlen.append(Belohnungszahl(codes[runde][i]))

    for operation in range(4):
        myNums = []
        appended = myMode["n"]

        if operation == 3:
            set1 = myMode['/1']
            set2 = myMode['/2']
            if set1 != None and set2 != None:
                myNums = [myMode['/3'], random.randint(set1, set2)]
                task = Divide(myNums[0], myNums[1], nums = myMode["n"])
        else:
            if operation == 0:
                set1 = myMode['+1']
                set2 = myMode['+2']
            elif operation == 1:
                myNums.append(myMode['-3'])
                appended -= 1
                set1 = myMode['-1']
                set2 = myMode['-2']
            elif operation == 2:
                set1 = myMode['*1']
                set2 = myMode['*2']
            if set1 != None and set2 != None:
                myClass = classes[operation]
                for _ in range(appended):
                    myNums.append(random.randint(set1, set2))
                try:
                    task = myClass(myNums[0], myNums[1], myNums[2], myNums[3], nums = myMode["n"])
                except IndexError:
                    try:
                        task = myClass(myNums[0], myNums[1], myNums[2], nums = myMode["n"])
                    except IndexError:
                        task = myClass(myNums[0], myNums[1], nums = myMode["n"])
        if set1 != None and set2 != None:
            myquiz.append(Quizteil(task, belohnungszahlen[operation]))
        else:
            myquiz.append(belohnungszahlen[operation])

    return myquiz

# helper functions
def mySleep(myTu:turtle.Turtle = standby, reach:list = [], duration: int = 0):
    if duration != 0:
        time_end = time.time() + duration
        while time.time() <= time_end:
            standby.circle(10)
    if reach != []:
        while True:
            standby.circle(10)
            if myTu.xcor() == reach[0] and myTu.ycor() == reach[1]:
                break
    at.pendown()

def gotoAT(tu: turtle.Turtle):
    tu.penup()
    tu.goto(at.xcor(), at.ycor())
    tu.pendown()

def convert_to_int(converting: list):
    global res
    if len(converting) != 0:
        if converting[0] != "(":
            if converting[0] == ",":
                converting.insert(0, 0)
            try:
                res = int("".join(map(str, converting)))
            except ValueError:
                pos = converting.index(",")
                converting.remove(",")
                length = len(converting)
                multi = length - pos
                res = int("".join(map(str, converting)))
                for _ in range(multi):
                    res = res / 10

        elif converting[0] == "(":
            converting.remove("(")
            converting.remove(")")
            
            try:
                res = int("".join(map(str, converting)))
            except ValueError:
                pos = converting.index(",")
                converting.remove(",")
                length = len(converting)
                multi = length - pos
                res = int("".join(map(str, converting)))
                for _ in range(multi):
                    res = res / 10
            finally:
                res * -1
    else: 
        res = 0

    return res

def init_num(tu: turtle.Turtle, step_init: int):
    global myTurtle, step_eingabe
    myTurtle = tu
    step_eingabe = step_init

def check_legal():
    global room_number
    if room_number != 2:
        verlasseRaum()
    else:
        checkeRaum2()

# Handle Keyboard input
def write1():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(1, step_eingabe, myTurtle)
    eingabe.append(1)
    listen_num()
def write2():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(2, step_eingabe, myTurtle)
    eingabe.append(2)
    listen_num()
def write3():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(3, step_eingabe, myTurtle)
    eingabe.append(3)
    listen_num()
def write4():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(4, step_eingabe, myTurtle)
    eingabe.append(4)
    listen_num()
def write5():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(5, step_eingabe, myTurtle)
    eingabe.append(5)
    listen_num()
def write6():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(6, step_eingabe, myTurtle)
    eingabe.append(6)
    listen_num()
def write7():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(7, step_eingabe, myTurtle)
    eingabe.append(7)
    listen_num()
def write8():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(8, step_eingabe, myTurtle)
    eingabe.append(8)
    listen_num()
def write9():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(9, step_eingabe, myTurtle)
    eingabe.append(9)
    listen_num()
def write0():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw(0, step_eingabe, myTurtle)
    eingabe.append(0)
    listen_num()
def writeKomma():
    global myTurtle, step_eingabe, eingabe, komma
    stop_listen_num()
    draw.draw(",", step_eingabe, myTurtle)
    eingabe.append(",")
    komma = True
    listen_num()
def writeMinus():
    global myTurtle, step_eingabe, eingabe
    draw.draw("-", step_eingabe, myTurtle)
    eingabe.append("-")
def write_klammer_auf():
    global myTurtle, step_eingabe, eingabe
    stop_listen_num()
    draw.draw("(", step_eingabe, myTurtle)
    eingabe.append("(")
    writeMinus()
    listen_num()
def write_klammer_zu():
    global myTurtle, step_eingabe, eingabe, klammer_zu
    stop_listen_num()
    draw.draw(")", step_eingabe, myTurtle)
    eingabe.append(")")
    klammer_zu = True
    convert_to_int(eingabe)
    listen_num()
def goOn():
    global eingabe, klammer_zu
    stop_listen_num()
    klammer_zu = True
    convert_to_int(eingabe)
    listen_num()
def new_Num():
    global myTurtle, step_eingabe, eingabe, klammer_zu, komma
    if klammer_zu == True:
        eingabe.clear()
        klammer_zu = False
        komma = False
        listen_num()
def delete():
    global klammer_zu, myTurtle
    klammer_zu = True
    myTurtle.clear()
    new_Num()
    gotoAT(myTurtle)
def go_up():
    stop_listen_player()
    player.sety(player.ycor() + player_step)
    check_legal()
    listen_player()
def go_right():
    global player_orienatation
    stop_listen_player()
    if player_orienatation != Directions.RIGHT.value:
        Init_Turtle.bewegeSpieler(player, Directions.RIGHT.value)
        player_orienatation = Directions.RIGHT.value
    player.setx(player.xcor() + player_step)
    check_legal()
    listen_player()
def go_down():
    stop_listen_player()
    player.sety(player.ycor() - player_step)
    check_legal()
    listen_player()
def go_left():
    global player_orienatation
    stop_listen_player()
    if player_orienatation != Directions.LEFT.value:
        Init_Turtle.bewegeSpieler(player, "a")
        player_orienatation = Directions.LEFT.value
    player.setx(player.xcor() - player_step)
    check_legal()
    listen_player()

def listen_player():
    screen.listen()
    screen.onkeypress(go_up, Directions.UP.value)
    screen.onkeypress(go_up, Directions.ARROW_UP.value)
    screen.onkeypress(go_right, Directions.RIGHT.value)
    screen.onkeypress(go_right, Directions.ARROW_RIGHT.value)
    screen.onkeypress(go_down, Directions.DOWN.value)
    screen.onkeypress(go_down, Directions.ARROW_DOWN.value)
    screen.onkeypress(go_left, Directions.LEFT.value)
    screen.onkeypress(go_left, Directions.ARROW_LEFT.value)

def stop_listen_player():
    screen.listen()
    screen.onkeypress(None, Directions.UP.value)
    screen.onkeypress(None, Directions.ARROW_UP.value)
    screen.onkeypress(None, Directions.RIGHT.value)
    screen.onkeypress(None, Directions.ARROW_RIGHT.value)
    screen.onkeypress(None, Directions.DOWN.value)
    screen.onkeypress(None, Directions.ARROW_DOWN.value)
    screen.onkeypress(None, Directions.LEFT.value)
    screen.onkeypress(None, Directions.ARROW_LEFT.value)

def listen_num():
    global eingabe, komma, klammer_zu
    if klammer_zu == False:
        screen.listen()
        screen.onkeypress(write0, "0")
        screen.onkeypress(write1, "1")
        screen.onkeypress(write2, "2")
        screen.onkeypress(write3, "3")
        screen.onkeypress(write4, "4")
        screen.onkeypress(write5, "5")
        screen.onkeypress(write6, "6")
        screen.onkeypress(write7, "7")
        screen.onkeypress(write8, "8")
        screen.onkeypress(write9, "9")
        screen.onkeypress(delete, 'BackSpace')
        if eingabe.count("(") == 1 and len(eingabe) >= 3:
            screen.onkeypress(write_klammer_zu, 'Return')
        if eingabe.count("(") == 0:
            screen.onkeypress(goOn, 'Return')
        if komma == False:
            screen.onkeypress(writeKomma, "comma")
        if eingabe.count("(") == 0 and len(eingabe) == 0:
            screen.onkeypress(write_klammer_auf, "minus")

def stop_listen_num():
    screen.listen()
    screen.onkeypress(None, "0")
    screen.onkeypress(None, "1")
    screen.onkeypress(None, "2")
    screen.onkeypress(None, "3")
    screen.onkeypress(None, "4")
    screen.onkeypress(None, "5")
    screen.onkeypress(None, "6")
    screen.onkeypress(None, "7")
    screen.onkeypress(None, "8")
    screen.onkeypress(None, "9")
    screen.onkeypress(None, "comma")
    screen.onkeypress(None, "minus")
    screen.onkeypress(None, 'Return')
    screen.onkeypress(None, 'BackSpace')

# GUI
def gotoFinish1(player: turtle.Turtle):
    if player.xcor() >= -210:
        Init_Turtle.bewegeSpieler(player, "a")
    else:
        Init_Turtle.bewegeSpieler(player, "d")
    player.goto(-210, -10)
    player.goto(-210, -140)

def returnCode(quiz: list, solutions: list):
    i = 0
    correct = True
    for myQuizteil in quiz:
        try:
            richtig = myQuizteil.getAufgabe().calculate(solutions[i])
        except:
            richtig = True
        
        if not richtig:
            correct = False
        i = i + 1

    for myQuizteil in quiz:
        if correct:
            try:
                if myQuizteil.belohnen().getWert() != None:
                    draw.draw(myQuizteil.belohnen().getWert(), step)
            except:
                if myQuizteil.getWert() != None:
                    draw.draw(myQuizteil.getWert(), step)
        else:
            wrong = random.randint(0, 9)
            draw.draw(wrong, step)

def initCheckeRaum2(play: Turtle, xL: float, xR: float, yT: float, yB: float, spec: list):
    global player, xLeft, xRight, yTop, yBottom, special
    player = play
    xLeft = xL
    xRight = xR
    yTop = yT
    yBottom = yB
    special = spec

def checkeRaum2():
    # links, rechts, oben, unten
    global player, xLeft, xRight, yTop, yBottom, special
    connection = special[0]
    bottom_room = special[1]

    if player.ycor() < yBottom + 55 and player.ycor() > connection[3] + 10 and player.xcor() >= connection[0] + 15:
        player.speed(0)
        player.setx(connection[0] + 20)
        player.speed(2)
    if player.xcor() <= connection[0] + 10 and player.ycor() >= bottom_room[2] + 10 and player.ycor() < bottom_room[2] + 15:
        player.speed(0)
        player.sety(bottom_room[2] + 5)
        player.speed(2)
    if player.xcor() <= connection[0] + 10 and player.ycor() <= yBottom + 55 and player.ycor() > yBottom + 35:
        player.speed(0)
        player.sety(yBottom + 60)
        player.speed(2)
    if player.ycor() <= bottom_room[2] + 5 and player.xcor() <= bottom_room[0]:
        player.speed(0)
        player.setx(bottom_room[0] + 5)
        player.speed(2)
    if player.xcor() <= xLeft + 10:
        player.speed(0)
        player.setx(xLeft + 15)
        player.speed(2)
    if player.xcor() >= xRight - 10:
        player.speed(0)
        player.setx(xRight - 15)
        player.speed(2)
    if player.ycor() >= yTop - 35:
        player.speed(0)
        player.sety(yTop - 40)
        player.speed(2)
    if player.ycor() <= bottom_room[3] + 55:
        player.speed(0)
        player.sety(bottom_room[3] + 60)
        player.speed(2)

def initVerlasseRaum(play: Turtle, xL: float, xR: float, yT: float, yB: float):
    global player, xLeft, xRight, yTop, yBottom
    player = play
    xLeft = xL
    xRight = xR
    yTop = yT
    yBottom = yB

def verlasseRaum():
    global player, xLeft, xRight, yTop, yBottom
    if player.xcor() <= xLeft + 10:
        player.speed(0)
        player.setx(xLeft + 15)
        player.speed(2)
    if player.xcor() >= xRight - 10:
        player.speed(0)
        player.setx(xRight - 15)
        player.speed(2)
    if player.ycor() >= yTop - 35:
        player.speed(0)
        player.sety(yTop - 40)
        player.speed(2)
    if player.ycor() <= yBottom + 55:
        player.speed(0)
        player.sety(yBottom + 60)
        player.speed(2)

def gibAufgabe(quiz: list, step: int):
    global res, klammer_zu, eingabe, appended, willContinue
    recycle = []

    at.penup()
    at.goto(-100, 0)
    at.pendown()

    for myQuizteil in quiz:
        continuing = True
        try:
            operators = myQuizteil.getAufgabe().whereEqual()
        except:
            try:
                operators = myQuizteil.getAufgabe().isDecimal()
            except AttributeError:
                continuing = False
                
        if continuing:
            if myQuizteil.getAufgabe().operator == "+":
                et = et1
            elif myQuizteil.getAufgabe().operator == "-":
                et = et2
            elif myQuizteil.getAufgabe().operator == "*":
                et = et3
            elif myQuizteil.getAufgabe().operator == "/":
                et = et4
            init_num(et, task_step)
            res = 6300000
            if myQuizteil.getAufgabe().operator == "/":
                draw.encode(myQuizteil.getAufgabe().numb1, myQuizteil.getAufgabe().operator, task_step, at)
                draw.encode(myQuizteil.getAufgabe().numb2, myQuizteil.getAufgabe().operator, task_step, at, operators)
            else:
                draw.encode(myQuizteil.getAufgabe().numb1, myQuizteil.getAufgabe().operator, task_step, at, operators[0])
                draw.encode(myQuizteil.getAufgabe().numb2, myQuizteil.getAufgabe().operator, task_step, at, operators[1])
                if appended >= 3:
                    draw.encode(myQuizteil.getAufgabe().numb3, myQuizteil.getAufgabe().operator, task_step, at, operators[2])
                    if appended >= 4:
                        draw.encode(myQuizteil.getAufgabe().numb4, myQuizteil.getAufgabe().operator, task_step, at, operators[3])

            gotoAT(et)
            new_Num()
            listen_num()
            while True:
                standby.goto(et.xcor(), et.ycor())
                if res != 6300000:
                    break
            stop_listen_num()
            klammer_zu == False
            eingabe = []

            if res == myQuizteil.getAufgabe().getLoesung() or round(res, 2) == round(myQuizteil.getAufgabe().getLoesung(), 2) or round(res, 1) == round(myQuizteil.getAufgabe().getLoesung(), 1) or round(res) == round(myQuizteil.getAufgabe().getLoesung()):
                at.color("green")
                at.pensize(2)
                et.clear()
            else:
                at.color("red")
                at.penup()
                at.goto(et.xcor(), et.ycor())
                at.forward(task_step)
                at.pendown()
                willContinue = False

            draw.encode(myQuizteil.getAufgabe().getLoesung(), myQuizteil.getAufgabe().operator, task_step, at, "Nope")
            at.color("black")
            at.pensize(1)

            recycle.append(res)

            at.penup()
            at.goto(-100, at.ycor() - step * 2)
            at.pendown()

    return recycle

# ------------------------------------------------------------------
# Hauptprogramm:
et = et1

difficulty = draw.set_difficulty()

player = Init_Turtle.initPlayer()
player.back(250)
player.speed(1)
player.showturtle()

init_num(et, task_step)

for turns in range(3):
    global room_number, finish
    while True:
        if willContinue:
            room_number = turns
            room_list = Init_Turtle.initRoom(turns)
            room = room_list[0]
            barrier = room_list[len(room_list) - 2]
        time.sleep(1)

        willContinue = True

        draw.draw(10, step)

        finish = room_list[5]
        draw.setFinish(finish, step / 3, fin)

        if turns != 2:
            initVerlasseRaum(player, room_list[1], room_list[2], room_list[3], room_list[4])
        elif turns == 2:
            special_room = room_list[6]
            initCheckeRaum2(player, room_list[1], room_list[2], room_list[3], room_list[4], special_room)

        listen_player()

        aufgabe = initQuiz(turns)

        recycled = gibAufgabe(aufgabe, step)

        returnCode(aufgabe, recycled)

        if willContinue:
            barrier.clear()

        mySleep(duration = 5)

        stop_listen_player()

        if turns != 2 or not willContinue:
            at.clear()
            fin.clear()
            for myEt in ets:
                myEt.clear()

        if willContinue:
            if turns == 0:
                Init_Turtle.bewegeSpieler(player, "a")
                player.goto(-385, 65)
                player.back(60)
                player.right(90)
                player.forward(150)
                player.left(90)

                room.clear()
                player.hideturtle()

                player.goto(-250, 0)
                player.showturtle()
            elif turns == 1:
                gotoFinish1(player)
            elif turns == 2:
                if player.ycor() >= -25:
                    gotoFinish1(player)
                Init_Turtle.bewegeSpieler(player, "a")

                player.goto(-335, -140)

            break

stop_listen_player()

wide_step1 = turtle.window_width() / 2
wide_step2 = wide_step1 * -1
wide = wide_step2 - step

player.speed(1)
while player.xcor() > wide:
    player.back(10)

# 1. Code schöner machen