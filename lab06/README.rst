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

Problem – w korpusie będzie prawdopodobnie bardzo mało wystąpień w1:n-1

Możemy potraktować generację słów składających się na zdanie jako proces Markowa i przyjąć założenie
Markowa - tylko N najbliższych słów ma wpływ na to jakie będzie wn :


Bigram: bierzemy pod uwagę tylko poprzednie słowo
Trigram: bierzemy pod uwagę dwa poprzedzające słowa
Tetragram: ... cztery itd.

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
