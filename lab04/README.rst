Prawo Zipfa
===========

Cel ćwiczenia:
--------------
Zapoznanie się z teoretyczną właściwością statystyczną tekstu opisaną prawem Zipfa oraz jej
empiryczne wyznaczenie z dowolnego tekstu.

Opis ćwiczenia:
---------------

Zipf w swojej książce "Human Behavior and the Principle of Least Effort" zamieścił prawo,
które można by określić mianem zasady Pareto w lingwistyce. Postulował on, że częstotliwość występowania
wyrazu w tekście jest odwrotnie proporcjonalna do numeru rankingu powstałego przez uporządkowanie wyrazów względem
ich częstości występowania. 


.. image:: http://home.agh.edu.pl/~korzycki/freq.png


Wynika z tego, że wyrazy które występują często obejmują woe


.. image:: http://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Moby_Dick_Words.gif/628px-Moby_Dick_Words.gif



Przykład::

    .--------------------|----------------------.
    | częstotliwość      |  205 |  115 |     56 |
    |--------------------|----------------------|
    | wyraz              |  kot | pies |  mysz  |
    |--------------------|----------------------|
    | ranking            |    1 |    2 |     3  |
    \--------------------|----------------------/

Inaczej mówiąc, wyraz na 50. pozycji w rankingu będzie występował trzykrotnie częściej niż wyraz na
pozycji 150. Zatem jeśli ``f`` określa częstotliwość, a ``r`` pozycję w rankingu, to winna istnieć stała ``k``
taka że:


.. image:: http://latex.codecogs.com/gif.latex?f\cong\frac{k}{r}


Prawo Zipfa oddaje pewien charakter statystyczny wielu problemów związanych z modelowaniem zachowań ludzkich (np. działa także w stosunku do ilości i wielkości miast wyrażonej w liczbie mieszkańców, i wiele innych...) natomiast
nie jest możliwe precyzyjne odwzorowanie na całej dziedzinie problemu. Mandelbrot podał uszczegółowienie tego prawa wyrażając go za pomocą modelu relacji opartego na funkcji wykładniczej.

Dokładniej, dla pewnych stałych ``B``, ``d``, ``P`` relacja między ``r`` a ``f`` wynosi:

.. image:: http://latex.codecogs.com/gif.latex?log(f)=log(P)-B\cdot%20log(r+d)


.. image:: http://home.agh.edu.pl/~korzycki/zipf.png


Plan ćwiczenia
--------------

W celu uzyskania lepszej jakości w rozpoznawaniu wyrazów należy użyć słownika fleksyjnego dla języka polskiego.
Każdy napis z tekstu należy spróbować rozpoznać jako formę fleksyjną w słowniku fleksyjnych, i następnie przetwarzać już tylko formę bazową tego wyrazu.

Zadaniem samodzielnym będzie:

1.  Zebranie samodzielne wybranych tekstów z wybranych języków (np. polski, angielski, esperanto)  z korpusu dostępnego ma serwerze dydaktycznym. Przeprowadzenie w miarę możliwości stemmingu w/w tekstów.
2a. Stworzenie listy zawierającej krotność wystąpienia poszczególnych wyrazów w wybranych tekstach. Posortowanie tej listy wg w/w krotności.
2b. Stworzenie listy zawierającej krotność wystąpienia pierwiastka długości wyrazów w wybranych tekstach. Posortowanie tej listy wg w/w krotności.
3.  Stworzenie wykresów dla poszczególnych języków gdzie na osi rzędnych znajdzie się w/w krotność, na osi odciętych pozycja na w/w list.
4. Sfitowanie przy pomocy wybranego narzędzia do w/w danych funkcji wynikającej z prawa Zipfa oraz poprawki Mandelbrota.
5. Zliczenie elementów mogących zostać uznanych za Hapax Legomena. Zidentyfikowanie ranków wyrazów które obejmują 50% tekstu.
6. Czynności powtórzyć na losowo wygenerowanym tekście.

Materiały
---------

* C.D.Manning, H.Schutze, "Foundations of Statistical Natural Language Processing"
* J.Sambor, „Słowa i liczby. Zagadnienia językoznawstwa statystycznego”, PAN, 1972
* `PLP <https://github.com/agh-glk/plp>`_
