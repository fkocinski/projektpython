import turtle
#zrob ruch kul wystrzal popraw ruszanie sie postaci wymiary okna uzyj grafik tla przeszkody 
#wprowadz zycia , punkty menu
#tracer keyup
#okno wyswietlanie jego tytul kolor wymiary
okno = turtle.Screen()
okno.title("Strzelamy")
okno.bgcolor('black')
okno.setup(1000,800)
okno.tracer(0)

#plansza (biala obramowka rysowanie)
#plansza = turtle.Turtle()
#plansza.speed(0)
#plansza.color("white")
#plansza.penup()
#plansza.setposition(-300,-300)
#plansza.pendown()
#plansza.pensize(4)
#for sciana in range (4):
    #plansza.fd(600)
    #plansza.lt(90)
#plansza.hideturtle()

#postac1 (wyswietlanie ksztalt kolor pozycja w przyszlosci obrazek)
postac1 = turtle.Turtle()
postac1.speed(0)
postac1.shape("triangle")
postac1.color("red")
postac1.penup()
#.pensize(3) rozmiar strzalki
postac1.goto(0,-250)
postac1.direction = 'stop'

p = postac1.xcor()
q = postac1.ycor()


#postac2 (wyswietlanie ksztalt kolor pozycja w przyszlosci obrazek)
postac2 = turtle.Turtle()
postac2.speed(0)
postac2.shape("triangle")
postac2.color("blue")
postac2.penup()
postac2.goto(0,250)
postac2.direction = 'stop'

P = postac2.xcor()
Q = postac2.ycor()

#bronpostac1
kula1 = turtle.Turtle()
kula1.speed(0)
kula1.shape('triangle')
kula1.color('white')
kula1.penup()
kula1.goto(p,q)
kula1.shapesize(0.4,0.4)
kula1.direction = 'stop'
kula1.setheading(90)
kula1.hideturtle()
predkosckula1=5
kula1stan = 'ready'


kula2 = turtle.Turtle()
kula2.speed(0)
kula2.shape('circle')
kula2.color('blue')
kula2.penup()
kula2.goto(p,q)
kula2.shapesize(0.4,0.4)
kula2.direction = 'stop'
kula2.setheading(90)
kula2.hideturtle()
predkosckula2=5
kula2stan = 'ready'


#bronpostac2
kula3 = turtle.Turtle()
kula3.speed(0)
kula3.shape('triangle')
kula3.color('red')
kula3.penup()
kula3.goto(P,Q)
kula3.shapesize(0.4,0.4)
kula3.direction = 'stop'
kula3.setheading(270)
kula3.hideturtle()
predkosckula3=5
kula3stan = 'ready'


kula4 = turtle.Turtle()
kula4.speed(0)
kula4.shape('circle')
kula4.color('green')
kula4.penup()
kula4.goto(P,Q)
kula4.shapesize(0.4,0.4)
kula4.direction = 'stop'
kula4.setheading(270)
kula4.hideturtle()
predkosckula2=5
kula2stan = 'ready'

#ruch kul


#ruszanie sie postaci
def ruchLewo1():
    postac1.direction = 'left'
    

def ruchPrawo1():
    postac1.direction = 'right'

def ruchLewo2():
    postac2.direction = 'left'

def ruchPrawo2():
    postac2.direction = 'right'

def ruchPostaci1():
    if postac1.direction == 'left':
        x = postac1.xcor()
        if x < -490:
            x =-490
        postac1.setx(x-0.1)

    if postac1.direction == 'right':
        x = postac1.xcor()
        if x > 480:
            x = 480
        postac1.setx(x+0.1)

def ruchPostaci2():
    if postac2.direction == 'left':
        x = postac2.xcor()
        if x < -490:
            x =-490
        postac2.setx(x-0.1)

    if postac2.direction == 'right':
        x = postac2.xcor()
        if x > 480:
            x = 480
        postac2.setx(x+0.1)

def wyjscie():
    okno.bye()
#przyciski
okno.listen()
okno.onkeypress(ruchLewo1,'a')
okno.onkeypress(ruchPrawo1,'s')
okno.onkeypress(ruchLewo2,'Left')
okno.onkeypress(ruchPrawo2,'Right')

okno.onkey(wyjscie, "Escape")

    

#nieskonczona petla aby okno nie znikalo zaraz po wyswietleniu
while True:
    okno.update()
    ruchPostaci1()
    ruchPostaci2()
    pass

#raport 1: były pewne problemy ponieważ nie mogłem zdecydować się na ostateczną wersje projektu.
# 

#Co do tej pory
# W 1 wersji utworzyłem otwierające się okno , które nie zamyka się (nieskończona pętla)
#oraz które możemy zamknąć klawiszem escape oraz x w rogu okienka.Nadałem rozmiar i kolory okienku.Następnie utworzyłem dwie postaci (poki co figury) nadałem im kolory i obróciłem
#napisałem funkcje które mają odpowiadać za ich ruch w lewa i w prawa strone.Jeden z graczy steruje za pomoca lewej i prawej strzalki a drugi za pomoca w oraz s
#za pomoca kodu pod hasztagiem przyciski umozliwilem uruchamianie funkcji ruszania za pomoca klawiszy , jednoczesnie zaczalem prace nad tym aby gracz nie wyjechal "poza okno"
#zdefiniowalem bron oraz kule ktore beda wystrzeliwane (ich ksztalty kolory rozmiary oraz pozycje)

#Co planuje
#poki co moim celem jest sprawienie aby gracz mogl wystrzeliwac kule , utworzenie mniejszej ramki w ktorej moga poruszac sie gracze , oraz dopasowanie parametrow predkosci 
# oraz rozmiarow elementow . Chce tez stworzyc przeszkody w ktore gracze beda mogli strzelac oraz umozliwic unicestwienie przeciwnika.Planuje tez skrocic kod w miejsach gdzie jest to mozliwe 
#i zrobic go bardziej czytelnym