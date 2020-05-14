# projektpython
Projekt nad którym będę pracował będzie grą.Napisze go w pythonie przy użyciu biblioteki turtle której cały czas uczę się z poradników internetowych.Mój pomysł to coś w rodzaju space soldiers .Jednak aby gra była unikalna będzie na niej 2 graczy po dwóch stronach planszy, ich taktyka będzie różna , będzie można strzelać do stworów poruszających się lewo prawo za mniejszą ilość punktów , lub do siebie za większą ilość , gracz ma za zadanie zdobyć wiecej punktów od przeciwnika.jednek z nich porusza się strzałkami , a drugi wsad.
import turtle
import random



#raport 2 : zmienilem troche sposob poruszania sie postaci , teraz po kliknieciu przycisku postac zmienia polozenie o kilka pikseli aby caly czas podazac w jednym kierunku nalezy przytrzymac ten 
#klawisz.Nadal mam problem z poruszaniem obu postaci w tym samym czasie (program gubi sie ktora funkcja jest uruchamiana tak jakby nie mozna bylo jednoczesnie uruchomic dwoch) , dodałem 
#opcje strzelania pociskiem ktorego polozenie poczatkowe = polozenie ,dodalem tez funkcje ktora powoduje ze nastepna kule mozna wystrzelic dopiero gdy jedna zniknie z mapy (doleci do granicy).
#dodalem pojawiajacego sie przeciwnika ale juz koncze petle ktora ma za zadanie tworzyc ich wielu, ich pozycje sa losowe z pewnego przedzialu. Graczy zrotowalem o 90 stopni aby trojkat 
#(nie lezal na boku) , koncze funkcje odbijania przeciwnikow od scian planszy gdy dojda do jej krawedzi , oraz zaczalem definiowac funkcje kolizja ktora ma sprawdzac czy przeciwnik zostal zestrzelony

#Plany : Postarac sie umozliwic poruszanie 2 graczy na raz , dokonczyc petle tworzaca wielu przeciwnikow , zdefiniowac funkcje odbijajaca od krawedzi przeciwnikow oraz zderzenia i kolizje
#jezeli nie bedzie mozliwe poruszanie 2 graczy na raz zostawic 1 , w pozniejszym etapie dodac

#raport 3:w poprzednim raporcie utworzylem przeciwnika , teraz w petli tworze ich dowolna liczbe. Oprocz tego program losuje poczatkowe polozenie y oraz x przeciwnika kazdego osobno.Naprawilem bledy z czescia kodu ktory odpowiadal za to , ze przeciwnik nie wychodzi poza plansze (odbija sie mnozy jego predkosc razy -1) Dokonczylem i poprawilem funkcje ktora odpowiadala za kolizje kuli i przeciwnika , wszystko dziala poprawnie dla kazdego zestrzelonego przeciwnika.Ponadto po zestrzeleniu przeciwnika znika on i pojawia sie w nowej innej pozycji a kula znika (mozna ja wystrzelic ponownie).
Moje plany to zrobienie funkcji ktora sprawdza kolizje przeciwnika i gracza(po takiej kolizji wyswietla sie napis game over i gra sie konczy) oprocz tego dodac licznik punktow ktory pokazuje ilu przeciwnikow zestrzelilismy.Moje prace zaczne od dodania funkcji ktora powoduje ze przeciwnik odbijajac sie od sciany bedzie znizal sie o pewna liczbe kratek w dol.Pewne problemy napotkalem przy wstawianiu obrazu zamiast figur , tla i dzwieku do gry.Postaram sie popracowac nad tym problemem.
