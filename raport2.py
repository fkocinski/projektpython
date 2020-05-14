import turtle
import random

okno = turtle.Screen()
okno.title("Strzelamy")
okno.bgcolor('black')
okno.setup(1000,800)
okno.tracer(0)


plansza = turtle.Turtle()
plansza.speed(0)
plansza.color("white")
plansza.penup()
plansza.setposition(-300,-300)
plansza.pendown()
plansza.pensize(4)

for sciana in range (4):
    plansza.fd(600)
    plansza.lt(90)
plansza.hideturtle()

postac1 = turtle.Turtle()
postac1.speed(0)
postac1.shape("triangle")
postac1.color("red")
postac1.penup()
postac1.setposition(0,-250)
postac1.setheading(90)

postac2 = turtle.Turtle()
postac2.speed(0)
postac2.shape("triangle")
postac2.color("blue")
postac2.penup()
postac2.setposition(0,250)
postac2.setheading(270)

cele1=[]
liczbacele=5
cele = turtle.Turtle()
cele.color("green")
cele.shape("circle")
cele.penup()
cele.speed(0)
cele.setposition(0,0)
for i in range (liczbacele):
    cele1.append(turtle.Turtle())
    
for cel in cele1:
    cele.color("green")
    cele.shape("circle")
    cele.penup()
    cele.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    cele.setposition(x,y)





predkoscpostaci = 5


def ruchPostaci1lewo():
        x = postac1.xcor()
        if x < -280:
            x = -280
        postac1.setx(x-predkoscpostaci)


def ruchPostaci1prawo():
        x = postac1.xcor()
        if x > 280:
            x = 280
        postac1.setx(x+predkoscpostaci)

def ruchPostaci2lewo():
        x = postac2.xcor()
        if x < -280:
            x = -280
        postac2.setx(x-predkoscpostaci)


def ruchPostaci2prawo():
        x = postac2.xcor()
        if x > 280:
            x = 280
        postac2.setx(x+predkoscpostaci)

def ruchCele():
    okno.listen()
    predkosccele = 0.1
    x = cele.xcor()
    if x > 280:
        predkosccele*= -1
    if x < -280:
        predkosccele*= -1
    cele.setx(x+predkosccele)
    
    
#kule
kule = turtle.Turtle()
kule.color("yellow")
kule.shape("triangle")
kule.penup()
kule.speed(0)
kule.setheading(90)        
kule.shapesize(0.5,0.5)
kule.hideturtle()


#stan ready - gotowy
stankuli="gotowa"
#ogien - kual wystrzelona
def strzal():
    global stankuli
    if stankuli == "gotowa":  
        stankuli = "wystrzelona"
        x = postac1.xcor()
        y = postac1.ycor() + 10
        kule.setposition(x,y)
        kule.showturtle()

def ruchKuli():
    global stankuli
    if stankuli == "wystrzelona": 
        yk=kule.ycor()
        predkosckuli=1
        yk+=predkosckuli
        kule.sety(yk)
    if kule.ycor()>275:
        kule.hideturtle()
        stankuli="gotowa"


#def zderzenie (kula,)

#def zderzenie()

        

    


def wyjscie():
    okno.bye()

def przyciski():
    okno.listen()
    okno.onkeypress(ruchPostaci1lewo,'a')
    okno.onkeypress(ruchPostaci1prawo,'s')
    okno.onkeypress(ruchPostaci2prawo,'Right')
    okno.onkeypress(ruchPostaci2lewo,'Left')
    okno.onkey(wyjscie, "Escape")
    okno.onkey(strzal,'space')


    

#nieskonczona petla aby okno nie znikalo zaraz po wyswietleniu
while True:
    
    okno.update()
    przyciski()
    ruchCele()
    ruchKuli()
    

   
    
    pass

#raport 2 : zmienilem troche sposob poruszania sie postaci , teraz po kliknieciu przycisku postac zmienia polozenie o kilka pikseli aby caly czas podazac w jednym kierunku nalezy przytrzymac ten 
#klawisz.Nadal mam problem z poruszaniem obu postaci w tym samym czasie (program gubi sie ktora funkcja jest uruchamiana tak jakby nie mozna bylo jednoczesnie uruchomic dwoch) , dodałem 
#opcje strzelania pociskiem ktorego polozenie poczatkowe = polozenie ,dodalem tez funkcje ktora powoduje ze nastepna kule mozna wystrzelic dopiero gdy jedna zniknie z mapy (doleci do granicy).
#dodalem pojawiajacego sie przeciwnika ale juz koncze petle ktora ma za zadanie tworzyc ich wielu, ich pozycje sa losowe z pewnego przedzialu. Graczy zrotowalem o 90 stopni aby trojkat 
#(nie lezal na boku) , koncze funkcje odbijania przeciwnikow od scian planszy gdy dojda do jej krawedzi , oraz zaczalem definiowac funkcje kolizja ktora ma sprawdzac czy przeciwnik zostal zestrzelony

#Plany : Postarac sie umozliwic poruszanie 2 graczy na raz , dokonczyc petle tworzaca wielu przeciwnikow , zdefiniowac funkcje odbijajaca od krawedzi przeciwnikow oraz zderzenia i kolizje
#jezeli nie bedzie mozliwe poruszanie 2 graczy na raz zostawic 1 , w pozniejszym etapie dodac instrukcje gry lub proste menu przycisk start stop