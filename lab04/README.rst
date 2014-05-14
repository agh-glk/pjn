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
ich częstości występowania. Przykład::

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

Plan ćwiczenia
--------------

W celu uzyskania lepszej jakości w rozpoznawaniu wyrazów należy użyć słownika fleksyjnego dla języka polskiego.
Każdy napis z tekstu należy spróbować rozpoznać jako formę fleksyjną w słowniku fleksyjnych, i następnie przetwarzać już tylko formę bazową tego wyrazu.

Na serwerze wierzba dostępna jest biblioteka CLP (w postaci biblioteki *.so) wraz z wrapperem PLP w języku Python.

1. Policzyć częstotliwości wystepowania wyrazów w pliku tekstowym (w j. polskim).
2. Wyznaczyć granicę, idąc od najrzadziej występujących słów, w momencie gdy zostało już opisane 50% wyrazów w tekście.
3. Wyznaczyć stałą ``k`` z prawa Zipfa dla tego tekstu. Można zastosować metodę najmniejszych kwadratów do sfitowania w/w funkcji hiperbolicznej. Zaprezentować wyniki na wykresie.
4. Wyestymować parametry ``B``, ``d`` i ``P`` uściślenia Mandelbrota. Zaprezentować na wykresie.
5. Czynności 3 oraz 4 powtórzyć na losowo wygenerowanym tekście.

Materiały
---------

* C.D.Manning, H.Schutze, "Foundations of Statistical Natural Language Processing"
* J.Sambor, „Słowa i liczby. Zagadnienia językoznawstwa statystycznego”, PAN, 1972
* `PLP <https://github.com/agh-glk/plp>`_
