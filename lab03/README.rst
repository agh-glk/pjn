Metryki tekstowe
================

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
Został on stworzony na potrzeby spisów powszechnych w Stanach Zjednoczonych jeszcze pod koniec XIX w. w celu
ułatwienia spisywania obywateli o nazwiskach których pisownia odbiega znacznie od pisowni angielskiej.

Analogicznym algorytmem jest 
`Metaphone <http://en.wikipedia.org/wiki/Metaphone>`_
który pomaga indeksować wyrazy w pisowni angielskiej według ich fonetyki.

Są to metody które dokonują transformacji napisów do mniejszego zbiory - obarczone są zatem błędem z tym związanym.

Innym podejściem jest próba budowy metryk (bądź funkcji które przynajmniej spełniają część założeń metryki) które 
są relatywnie proste obliczeniowo (np. w stosunku do pełnej metryki edycyjnej).

Taką metryką jest metryka LCS - Longest Common Substring która porównuje dwa napisy na podstawie długości 
ich najdłuższego wspólnego podciągu. Dla f(x,y) - funkcji zwracającej najdłuższy wspólny podciąg napisów x i y, 
|x| - długości napisu x
to w/w metrykę zdefiniujemy jako:

.. image:: http://latex.codecogs.com/gif.latex?LCS(x%2Cy)%3D%5Cfrac%7B%7Cf(x%2Cy)%7C%7D%7Bmax(%7Cx%7C%2C%7Cy%7C)%7D

Metryka powyższa jest jednak dla pewnych zastosowań zbyt wrażliwa na przestawienia elementów napisu - 
np. jeśli w adresie przestawimy miejscami miejscowość z ulicą - to nadal będzie to ten sam adres, ale metryka 
LCS pokaże nam znaczną zmianę. 

Często stosowanym rozwiązaniem będzie zastosowanie metryki N-gramowej (ściśle mówiąc nie są to dokładnie metryki -
ponieważ warunek trójkąta nie jest spełniony - ale w praktyce możemy tu nadal mówić nieformalnie o metryce).
Metryki N-gramowe opierają się na badaniu zbioru N-gramów, czyli podciągów o długości N. Jeśli rozbijemy napisy x i y 
na odpowiadające im N-gramy to możemy porównać te zbiory przy pomocy tzw. współczynnika Dice'a:

.. image:: http://latex.codecogs.com/gif.latex?DICE(x%2Cy)%3D%5Cfrac%7B2%5Ctimes%20%7CNgrams(X)%5Ccap%20Ngrams(y)%7C%7D%7B%7CNgrams(X)%7C%2B%7CNgrams(y)%7C%7D

Albo też, jeśli traktować zbiory N-gramów jako wektory gdzie indeksami są poszczególne N-gramy, a wartościami współrzędnych 
krotności wystąpienia N-gramów, możemy wprowadzić tzw. metrykę cosinusową:

.. image:: http://latex.codecogs.com/gif.latex?COSINE(x%2Cy)%3D%5Cfrac%7B%7CNgrams(X)%20%5Ccdot%20Ngrams(y)%7C%7D%7B%7CNgrams(X)%7C%7CNgrams(y)%7C%7D

Kropka oznacza tu iloczyn skalarny wektorów. Wartość otrzymana stanowi zaś cosinus kąta między wektorami N-gramów (stąd nazwa).


Zadanie:
--------
Korzystając z opisanych w/w mechanizmów pogrupować linie z pliku lines.txt na zbiory odpowiadające poszczególnym firmom.

Należy w tym celu operować na całej linii jako na 1 napisie, najprawdopodobniej 
