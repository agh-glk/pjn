Wnioskowanie statystyczne w przetwarzaniu języka naturalnego
============================================================

Cel ćwiczenia:
--------------
Stworzyć spellchecker w oparciu o mechanizmy wnioskowania statystycznego

Opis ćwiczenia:
---------------

Stworzenie spellchera opiera się na znalezieniu elementów ze słownika najbliższych poprawianemu napisowi - np. dla napisu "pics" najbliższym wyrazem ze słownika będzie forma "pies". 

"Bliskość" definiujemy przy pomocy odpowiedniej metryki. W przypadku spellcheckerów jest to najczęściej _metryka Levenshteina: http://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina zwana także odległością edycyjną.  

Wyniki jednak często są niejednoznaczne, należałoby zatem wprowadzić porządek w wynikach – tzn. wyznaczyć wyraz ze słownika stanowiący najbardziej prawdopodobną poprawkę. Formalnie: Dla poprawki (wyrazu ze słowika) "c" i wejściowego wyrazu do poprawy "w" znaleźć: 

.. image:: http://latex.codecogs.com/gif.latex?argmax_cP%28c%7Cw%29



Z Twierdzenia Bayesa mamy:

argmaxc P(c|w) = argmaxc P(w|c) P(c) / P(w)

P(w) będzie prawdopodobieństwem wystąpienia danego napisu. Dla każdego jest identyczny – więc nie jest potrzebny do szacowania.

P(c) będzie prawdopodobieństwem wystąpienia danej poprawki.  Do wyznaczenia tego należy skorzystać z analizy frekwencyjnej wyrazów w korpusie.

Jako P(w|c) ustalamy prawdopodobieństwo wystąpienia określonego błędu. Ustalmy to prawdopodobieństwo na podstawie prawdopodobieństwa wystąpienia błędu w określonej znormalizowanej odległości Levenstheina, gdzie:
 * 1/4 – odległość “polonica” czyli żuk ↔ zuk
 * 1/4 – odległość “błąd ortograficzny rz/ż ó/u ę/en ą/om ch/h” typu żuk ↔ rzuk, mózg ↔ muzg itp. 
 * ½ – czeski błąd – zamiana dwu sąsiednich liter miejscami pies ↔ peis

Pozostałe elementy liczymy normalnie

Zliczyć prawdopodobieństwa wystąpienia błędu w określonej odległości na podstawie analizy pliku z błędami.
Przy zliczaniu frekwencji i kategorii odległości błędów zastosować wygładzanie Laplace'a o wartości 1. 

Materiały:
----------

- sjp.txt - słownik polskich wyrazów z którego korzysta m.in. aspell

