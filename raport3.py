import turtle
import math
import random

#tworzy okno
okno = turtle.Screen()
okno.title("Kosmici")
okno.bgcolor('black')


#tworzy biala ramke gdzie beda postaci i przeciwnicy
ramka = turtle.Turtle()
ramka.speed(0)
ramka.color("white")
ramka.penup()
ramka.setposition(-300,-300)
ramka.pendown()
ramka.pensize(3)
for sciana in range(4):
    ramka.fd(600)
    ramka.lt(90)
ramka.hideturtle()

punkty=0

punktyrysuj = turtle.Turtle()
punktyrysuj.speed(0)
punktyrysuj.color("white")
punktyrysuj.penup()
punktyrysuj.setposition(-290,-280)


#tworzy gracza
gracz = turtle.Turtle()
gracz.color("blue")
gracz.shape("triangle")
gracz.penup()
gracz.speed(0)
gracz.setposition(0,-250)
gracz.setheading(90)

#przeciwnik


#kule
kula = turtle.Turtle()
kula.hideturtle()
kula.color("yellow")
kula.shape("triangle")
kula.penup()
kula.speed()
kula.setheading(90)
kula.shapesize(0.5,0.5)


#stan kuli stezal gotowa


przeciwnikpredkosc = 3
graczpredkosc = 5
kulapredkosc = 10 
liczbaprzeciwnikow = 5

przeciwnicy=[]
for x in range (liczbaprzeciwnikow):
    przeciwnicy.append(turtle.Turtle())
    
for przeciwnik in przeciwnicy:   
    przeciwnik.color("red")
    przeciwnik.shape("square")
    przeciwnik.penup()
    przeciwnik.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    przeciwnik.setposition(x,y)

def ruchlewo():
    x = gracz.xcor()
    x -=graczpredkosc
    if x < -280:
        x = -280
    gracz.setx(x)

def ruchprawo():
    x = gracz.xcor()
    x +=graczpredkosc
    if x > 280:
        x = 280
    gracz.setx(x)

stankuli="gotowa"

def strzal():
    global stankuli
    if stankuli == "gotowa":
        stankuli = "strzal"
        x = gracz.xcor()
        y = gracz.ycor() + 10
        kula.setposition(x,y)
        kula.showturtle()
def kolizja(x1,x2):
    odleglosc = math.sqrt(math.pow(x1.xcor()-x2.xcor(),2)+math.pow(x1.ycor()-x2.ycor(),2))
    if odleglosc < 15:
        return True 
    else:
        return False

turtle.listen()
turtle.onkey(ruchlewo,"Left")
turtle.onkey(ruchprawo,"Right")
turtle.onkey(strzal,"space")

while True:
    for przeciwnik in przeciwnicy:
        x = przeciwnik.xcor()
        x += przeciwnikpredkosc
        przeciwnik.setx(x)

        if przeciwnik.xcor() > 280:
            for p in przeciwnicy:
                y = p.ycor()
                y-=40
                p.sety(y)
            przeciwnikpredkosc *=-1
        if przeciwnik.xcor() < -280:
            for p in przeciwnicy:
                y = p.ycor()
                y -=40
                p.sety(y)
            przeciwnikpredkosc *= -1
        if kolizja(kula,przeciwnik):
            kula.hideturtle()
            stankuli="gotowa"
            kula.setposition(0,-400)
            x=random.randint(-200,200)
            y=random.randint(100,250)
            przeciwnik.setposition(x,y)
            punkty+=10
            punktynapis = " Wynik : %s" %punkty
            punktyrysuj.clear()
            punktyrysuj.write(punktynapis,False,align="left",font=("Arial",14,"normal"))
       
    
    if stankuli =="strzal":
        y = kula.ycor()
        y += kulapredkosc
        kula.sety(y)

    if kula.ycor()>275:
        kula.hideturtle()
        stankuli="gotowa"

    
x = raw_input("enter")

