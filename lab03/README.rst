Lab03
=====

Cel ćwiczenia:
--------------
Stworzyć metrykę tekstową w celu dokonania klasteryzacji zbioru napisów

Opis ćwiczenia:
---------------
W poprzednim ćwiczeniu spotkaliśmy się z metryką edycyjną operującą na przestrzeni napisów. Nie jest to naturalnie 
jedyny sposób na poszukiwanie napisów "podobnych" - podobnych technik jest stosowanych wiele różnych, 
w zależności od zastosowania.

Jednym ze sposobów na poszukiwanie podobieństwa w przestrzeni napisów, jest dokonanie transformacji pozwalającej na 
przekształcenie porównywanych napisów na wartość np. liczbową pozwalającą na łatwiejsze operowanie na nich.
Przykładem takiego mechanizmu jest algorytm fonetyczny 
`SOUNDEX <http://en.wikipedia.org/wiki/Soundex>`_ obecny w większości baz danych.
Przekształca on dany napis w kombinację litery i cyfr w celu uproszczenia jego zapisu.
Został on stworzony na potrzeby spisów powszechnych w Stanach Żjednoczonych jeszcze pod koniec XIX w. w celu
ułatwienia spisywania obywateli o nazwiskach których pisownia odbiega znacznie od pisowni angielskiej.

Analogicznym algorytmem jest 
`Metaphone <http://en.wikipedia.org/wiki/Metaphone>`_
który pomaga indeksować wyrazy w pisowni angielskiej według ich fonetyki.

Są to metody które dokonują transformacji napisów do mniejszego zbiory - obarczone są zatem błędem z tym związanym.

Innym podejściem jest próba budowy metryk (bądź funkcji które przynajmniej spełniają część założeń metryki) które 
są relatywnie proste obliczeniowo (np. w stosunku do pełnej metryki edycyjnej).

