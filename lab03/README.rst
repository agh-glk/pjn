Metryki tekstowe
================

Cel ćwiczenia:
--------------
Stworzyć jest stworzyć metodę używającą ansamble dowolnych metryk tekstowych w celu dokonania klasteryzacji zbioru napisów.

Opis ćwiczenia:
---------------
W poprzednim ćwiczeniu zapoznaliśmy się z metryką edycyjną operującą na przestrzeni napisów. Nie jest to naturalnie 
jedyny sposób na poszukiwanie napisów "podobnych" -  w zależności od zastosowania stosowanych jest wiele 
różnych podobnych technik.

Jednym ze sposobów na poszukiwanie podobieństwa w przestrzeni napisów jest dokonanie transformacji pozwalającej na 
przekształcenie porównywanych napisów na wartość np. liczbową pozwalającą na łatwiejsze operowanie na nich.
Przykładem takiego mechanizmu jest algorytm fonetyczny 
`SOUNDEX <http://en.wikipedia.org/wiki/Soundex>`_ obecny w większości baz danych.
Przekształca on dany napis w kombinację litery i cyfr w celu uproszczenia jego zapisu.
Został on stworzony na potrzeby spisów powszechnych w Stanach Zjednoczonych jeszcze pod koniec XIX w. w celu
ułatwienia spisywania obywateli o nazwiskach, których pisownia odbiega znacznie od pisowni angielskiej.

Analogicznym algorytmem jest 
`Metaphone <http://en.wikipedia.org/wiki/Metaphone>`_,
który pomaga indeksować wyrazy w pisowni angielskiej według ich fonetyki.

Metody te dokonują transformacji stratnych, to znaczy niektóre różne napisy mogą zostać przekształcone na takie same napisy 
- metody te obarczone są zatem pewnym błędem.

Innym podejściem jest próba budowy metryk (bądź funkcji które przynajmniej spełniają część założeń metryki), które 
są relatywnie proste obliczeniowo (np. w stosunku do pełnej metryki edycyjnej).

Taką metryką jest metryka LCS - Longest Common Substring, która porównuje dwa napisy na podstawie długości 
ich najdłuższego wspólnego podciągu. Dla f(x,y) - funkcji zwracającej najdłuższy wspólny podciąg napisów x i y, 
|x| - długości napisu x
to w/w metrykę zdefiniujemy jako:

.. image:: http://latex.codecogs.com/gif.latex?LCS(x%2Cy)%3D1-%5Cfrac%7B%7Cf(x%2Cy)%7C%7D%7Bmax(%7Cx%7C%2C%7Cy%7C)%7D

Metryka powyższa jest jednak dla pewnych zastosowań zbyt wrażliwa na przestawienia elementów napisu - 
np. jeśli w adresie przestawimy miejscami miejscowość z ulicą - to nadal będzie to ten sam adres, ale metryka 
LCS pokaże nam znaczną zmianę. 

Często stosowanym rozwiązaniem jest zastosowanie metryki N-gramowej (ściśle mówiąc nie są to dokładnie metryki -
ponieważ warunek trójkąta nie jest spełniony - ale w praktyce możemy tu nadal mówić nieformalnie o metryce).
Metryki N-gramowe opierają się na badaniu zbioru N-gramów, czyli podciągów o długości N. Jeśli rozbijemy napisy x i y 
na odpowiadające im N-gramy to możemy porównać te zbiory przy pomocy tzw. współczynnika Dice'a:

.. image:: http://latex.codecogs.com/gif.latex?DICE(x%2Cy)%3D1-%5Cfrac%7B2%5Ctimes%20%7CNgrams(x)%5Ccap%20Ngrams(y)%7C%7D%7B%7CNgrams(x)%7C%2B%7CNgrams(y)%7C%7D

Można także dokonać prostego przejścia z reprezentacji za pomocą zbiorów na reprezentacje wektorową. 
Jeśli przyjmiemy, że w całym tekście znajduje się K wszystkich możliwych różnych N-gramów, to można wyobrazić sobie 
wektor o wymiarze K, w którym każda współrzędna odpowiada jednemu z N-gramów. Następnie każdy dowolny napis 
(zbiór N-gramów) można zareprezentować wektorowo w taki sposób, że wszystkie współrzędne wektora 
odpowiadające tym N-gramom napisu posiadają wartość 1 a pozostałe wartość 0 (zamiast 1 można użyć także innych
wartości, np krotność, ważność N-gramu, itp). 

Taka reprezentacja umożliwia nam bardziej precyzyjne mierzenie odległości (podobieństwa) pomiędzy wektorami wyrażonej poprzez 
tzw. metrykę cosinusową:

.. image:: http://latex.codecogs.com/gif.latex?COSINE(x%2Cy)%3D1-%5Cfrac%7B%7CNgrams(x)%20%5Ccdot%20Ngrams(y)%7C%7D%7B%7CNgrams(x)%7C%7CNgrams(y)%7C%7D

Kropka oznacza tu iloczyn skalarny wektorów. Wartość otrzymana stanowi zaś cosinus kąta między wektorami 
N-gramów (stąd nazwa). 

Czasami warto podbijać wartość (krotność) pewnych N-gramów na szczególnych pozycjach napisu (np. na początku).

Zadanie:
--------
W pliku lines.txt znajdują się nazwy firm międzynarodowych wprowadzonych przez ludzi. Okazuje się, że nawet tak
formalnie skodyfikowane napisy jak nazwy firm potrafią być wprowadzane przez ludzi w sposób dalece wariantywny. 
Różnorodność sposobów zapisu tych nazw powoduje przez to duże trudności w automatycznej kategoryzacji, które nazwy
odnoszą się do tej samej jednej firmy.

Korzystając z opisanych w/w mechanizmów oceny podobieństwa napisów należy napisać program, który będzie potrafił
pogrupować linie z pliku lines.txt na zbiory odpowiadające poszczególnym firmom.

Należy w tym celu operować na całej linii jako na 1 napisie. Aby podnieść skuteczność mechanizmu najlepiej wykonać 
szereg dodatkowych kroków pre-processingu - np. usunąć znaki niealfanumeryczne, 
usunąć wyrazy o wysokiej częstości (typu LTD, Z O.O., OOO, 000, LLC, nazwy miast, krajów itp.), 
usunąć znaczenie białych znaków oraz wielkich liter, itp.

Na tak przetworzonych napisach znaleźć najbliżej leżące w określonej metryce. Przykładowy mechanizm może 
mieć następujące działanie:

- zaczynamy od najkrótszego napisu

- dla danego napisu wybieramy te napisy które są odległe o nie dalej niż ustalone epsilon (np. 0.2) i wiążemy w jeden "cluster"

- powtarzamy w/w operację aż do wyczerpania niesklastrowanych napisów.


Można stosować dowolną liczbę podejść, łączyć je w ansambl w celu uzyskania polepszenia uzyskanego wyniku.


Wejście i wyjście programu
--------------------------

Program na standardowe wejście powinien przyjmować plik z nazwami firm (kodowanie UTF-8). Jedna linia reprezentuje jedną
nazwę firmy. 

Program powinen generować na standardowe wyjście listę firm pogrupowanych wg. konkretnej rzeczywistej firmy. Grupy należy 
rozdzielić linią zawierającą dowolną niezerową ilością znaków #. Np::

  Firma 1
  Firma 1 aa
  Firma 1 bbb
  
  ###
  
  Firma 2 
  Firma 2 ...
  
  ###
  
  Firma 3


Typowe uruchomienie programu::

  $ cat lines.txt | ./program


Ocena jakości programu
----------------------

Pomocnym programem testującym jakość zwracanych wyników jest zamieszczony z kodem laboratorium program rank.py.
Program ten uruchamia się z jedny parametrem ``-n`` (``--norm``), którego jako wartość należy podać ścieżkę do pliku
ze wzorcowym podziałem (plik ``norm.txt``). Program na standardowe wejście oczekuje danych z programów generujących
klastry.

Typowe użycie::

  $ cat lines.txt | ./program | rank.py -n norm.txt

Program wypisuje na standardowe wyjście ocene w skali od 0 do 1 będącą średnią 
miar `F-measure <http://en.wikipedia.org/wiki/F-measure>`_ policzonych dla poszczególnych linii pliku ``lines.txt`` osobno. 
Wartość 1.0 oznacza najlepszą notę (w tym przypadku pełną zgodność klastrów).

Wchodząc w szczegóły, dla każdej nazwy z pliku ``lines.txt`` porównywana jest precyzja i pełność (precision and recall) 
na podstawie zbioru wygenerowanego przez program oraz zbioru odczytanego z pliku wynikowego. Następnie 
dla tego napisu liczona jest miara F-measure, będąca po prostu średnią harmoniczną miar precyzji i pełności.

Jesli przyjmiemy, że program zaklasyfikował dany napis (linię) do zbioru A, a w pliku wzorcowym został on 
zaklasyfikowany do zbioru B, to pojęcia precyzji i pełności względem zbiorów A i B definiujemy następująco. 

Precyzja:


.. image:: http://latex.codecogs.com/gif.latex?precision=\frac{|A\cap&space;B|}{|\overline{A}|} 


Pełność:


.. image:: http://latex.codecogs.com/gif.latex?recall=\frac{|A\cap&space;B|}{|\overline{B}|}



Innymi słowy precyzja określa jak duży procent napisów zklasyfikowanych do A było poprawnie zklasyfikowanych, 
a pełność określa jak duży jest procent poprawnie zklasyfikowanych napisów przez program względem wszystkich poprawnych
napisów w zbiorze wzorcowym B.

Miara precision-recall daje dobrą orientacje na temat jakości danej metody, natomiast konieczne jest analizowanie
obu czynników precyzji i pełności wspólnie (z wartości czynników osobno ciężko wysnuć jakiekolwiek wnioski na temat 
ogólnej jakości). Bardzo często natomiast potrzebujemy posługiwać się pojedynczą wartością (tak jak w przypadku 
programu oceniającego ``rank.py``, chcemy mieć jedną wartość liczbową od 0 do 1, która powie jaką jakość ma dany 
program klasteryzujący względem przykładu wzorcowego). W takiej sytuacji można posiadając precyzję i pełność 
łatwo policzyć miarę F-measure:


.. image:: http://upload.wikimedia.org/math/9/9/1/991d55cc29b4867c88c6c22d438265f9.png


Program ``rank.py`` liczy F-measure dla każdego pojedynczego przykładu, a następnie wylicza średnią arytmetyczną
z wszystkich tak otrzymanych miar.
