Wnioskowanie statystyczne w przetwarzaniu języka naturalnego
============================================================

Cel ćwiczenia:
--------------
Stworzyć spellchecker w oparciu o mechanizmy wnioskowania statystycznego

Opis ćwiczenia:
---------------

Stworzenie spellchera opiera się na znalezieniu elementów ze słownika najbliższych poprawianemu napisowi - np. dla napisu "pics" najbliższym wyrazem ze słownika będzie forma "pies". 

"Bliskość" definiujemy przy pomocy odpowiedniej metryki. W przypadku spellcheckerów jest to 
najczęściej `metryka Levenshteina <http://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina>`_ zwana także odległością edycyjną.  

Wyniki jednak często są niejednoznaczne, należałoby zatem wprowadzić porządek w wynikach – 
tzn. wyznaczyć wyraz ze słownika stanowiący najbardziej prawdopodobną poprawkę. 
Formalnie: Dla poprawki (wyrazu ze słowika) "c" i wejściowego wyrazu do poprawy "w" znaleźć: 

.. image:: http://latex.codecogs.com/gif.latex?argmax_cP%28c%7Cw%29

takie "c" dla którego prawdopodobieństwo, że to właśnie "c" jest właściwą poprawką dla "w" jest maksymalne. 

Z Twierdzenia Bayesa mamy:

.. image:: http://latex.codecogs.com/gif.latex?argmax_cP%28c%7Cw%29%3Dargmax_c%5Cfrac%7BP%28w%7Cc%29P%28c%29%7D%7BP%28w%29%7D


- P(w) będzie prawdopodobieństwem wystąpienia danego napisu. Dla każdego c jest identyczny – więc nie jest potrzebny do szacowania.

- P(c) będzie prawdopodobieństwem wystąpienia danej poprawki.  Do wyznaczenia tego należy skorzystać z analizy frekwencyjnej wyrazów w korpusie (tzn. przykładowym zbiorze tekstów).

Jako P(w|c) ustalamy prawdopodobieństwo wystąpienia określonego rodzaju błędu. 
Ustalmy to prawdopodobieństwo na podstawie prawdopodobieństwa wystąpienia błędu w określonej znormalizowanej odległości Levenstheina. Z typami błędów
można zapoznać się w `[Dorosz, 2008] <http://journals.bg.agh.edu.pl/AUTOMATYKA/2008-01/Auto03.pdf>`_, tj:

* 1/4 – odległość “polonica” czyli żuk ↔ zuk,
* 1/4 – odległość “błąd ortograficzny rz/ż ó/u ę/en ą/om ch/h” typu żuk ↔ rzuk, mózg ↔ muzg itp. 
* 1/4 - odległość "pomyłki typograficzne",
* ½ – czeski błąd – zamiana dwu sąsiednich liter miejscami pies ↔ peis

Pozostałe elementy liczymy normalnie.

Zliczyć prawdopodobieństwa wystąpienia błędu w określonej odległości na podstawie analizy pliku z błędami.

Przy zliczaniu frekwencji i kategorii odległości błędów zastosować `wygładzanie Laplace'a o wartości 1 <http://en.wikipedia.org/wiki/Additive_smoothing>`_.

Wygładzanie to stosujemy przy zliczaniu np. wyrazów w korpusie w celu wyznaczenia P(c). Intuicja stojąca za 
wygładzaniem jest następująca: 

Niech N - będzie ilością wyrazów w słowniku, M - ilością wyrazów w korpusie, Nc - ilość wystąpień wyrazu c w korpusie.

Załóżmy, że dany wyraz c nie wystąpił ani razu w korpusie - bez wygładzania 
jego P(c) = Nc/M wynosi zatem 0, czyli nigdy nie będzie on nigdy odpowiednim kandydatem do poprawki. 
Aby uniknąć tego typu
zjawiska zakładamy, że każdy wyraz wystąpił co najmniej raz. 
Aby jednak suma wszystkich P(c) równa wynosiła 1, należy zwiększyć mianownik w w/w ułamku o ilość wszystkich wyrazów, 
a zatem "wygładzone" P(c) będzie równe (Nc+1)/(M+N).


Materiały:
----------
- sjp.txt - słownik polskich wyrazów z którego korzysta m.in. aspell
- bledy.txt - plik z błedami służące do wyznaczenia P(w|c)
- `Milionowy Podkorpus Języka Polskiego <http://nkjp.pl/index.php?page=14&lang=0>`_ który posłuży do wyznaczenia P(c)
- Dorosz K., Automatyka 2008/1, `Automatyczne sprawdzanie poprawności pisowni w języku polskim oparte na odległości Levenshteina <http://journals.bg.agh.edu.pl/AUTOMATYKA/2008-01/Auto03.pdf>`_
