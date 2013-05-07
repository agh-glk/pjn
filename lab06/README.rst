Łańcuchy Markova - generacja tekstu
===================================

Cel ćwiczenia
-------------

Celem ćwiczenia jest zapoznanie się z praktycznym zastosowaniem łańcuchów Markova dla generacji tekstów, 
w oparciu o założenie pewnego prawdopodobieństwa występowania znaku, przy warunkach występowania określnych
znaków go poprzedzajacych.


Opis ćwiczenia
--------------

Zakładamy, że model probablistyczny języka, pozwalający obliczyć prawdopodobieństwo zdania

* Jeśli w1:n oznacza ciąg wyrazów w1, w2, ... , w3
* Jaka jest wartość P(w1:n)

Możemy próbować określać prawdopodobieństwo wystąpień poszczególnych liter albo wyrazów.


Aby obliczyć P(w1:n) możemy wykorzystać regułę łańcuchową, wtedy:

.. image:: http://latex.codecogs.com/gif.latex?P(w_1_:_n)=P(w_1_:_n_-_1)P(w_n|w_1_:_n_-_1)=P(w_1_:_n_-_2)P(w_n_-_1|w_1_:_n_-_2)P(w_n|w_1_:_n_-_1)=%20itd.%20=%20P(w_1)P(w_2|w_1)P(w3|w_1_:_2)P(w_4|w_1_:_3)%20...%20P(w_n_-_1|w_1_:_n_-_2)P(w_n|w_1_:_n_-_1)


Problem – w korpusie będzie prawdopodobnie bardzo mało wystąpień w1:n-1

Możemy potraktować generację słów składających się na zdanie jako proces Markowa i przyjąć założenie
Markowa - tylko N najbliższych słów ma wpływ na to jakie będzie wn :

.. image:: http://latex.codecogs.com/gif.latex?P(w_n|w_1_:_n_-_1)%20\approx%20P(w_n|w_n_-_N_+_1_:_n_-_1)

Bigram: bierzemy pod uwagę tylko poprzednie słowo
Trigram: bierzemy pod uwagę dwa poprzedzające słowa
Tetragram: ... cztery itd.

Wtedy:

.. image:: http://latex.codecogs.com/gif.latex?P(w_1_:_n)%20\approx%20\prod_{k=1,n}%20P(w_k|w_{k-N+1:%20k-1})


Przykłady zastosowań:

* Rozpoznawanie pisma, mowy
* Poprawianie błędów ortograficznych
* Tłumaczenie automatyczne
* Analiza stylu pisania (wykrywanie plagiatów, autorstwa tekstów itp.)
* Generowanie dużej ilości danych tekstowych


Plan ćwiczenia
--------------
1. Zbudować model N-gramowy kolejności występowania liter albo wyrazów w tekstach uczących dla N w zakresie od 1 do 10 i zebrać statystyki dla tekstów.
2. Zastosować nauczone modele do generacji przypadkowych tekstów.
3. Określić wpływ wartości N na jakość generowanego tekstu.

Materiały
---------

* C.D.Manning, H.Schutze, "Foundations of Statistical Natural Language Processing"
* Max Out, "Łańcuchy Markowa - teoria, przykłady, praktyka, projekt", Software 2.0, 4/2001
* Pliki z katalogu /usr/local/teksty
