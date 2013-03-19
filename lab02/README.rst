Wnioskowanie statystyczne w sprawdzaniu poprawności pisowni
===========================================================

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
jego prawdopodobieństwo wystąpienia

.. image:: http://latex.codecogs.com/gif.latex?P%28c%29%3D%5Cfrac%7BN_c%7D%7BM%7D

wynosi zatem 0, czyli nigdy nie będzie on nigdy odpowiednim kandydatem do poprawki.
Aby uniknąć tego typu
zjawiska zakładamy, że każdy wyraz wystąpił co najmniej raz.
Aby jednak suma wszystkich P(c) równa wynosiła 1, należy zwiększyć mianownik w w/w ułamku o ilość wszystkich wyrazów,
a zatem "wygładzone" prawdopodobieństwo będzie równe:

.. image:: http://latex.codecogs.com/gif.latex?P%28c%29%3D%5Cfrac%7BN_c+1%7D%7BM+N%7D



Wejście i wyjście programu spellcheckera
----------------------------------------

Pisząc program spellcheckera proszę zwrócić uwagę na to, aby był on odpowiednio zoptymalizowany. To znaczy 
sprawdzenie pojedynczego napisu powinno trwać nie więcej niż około 0.5 s na nowoczesnej maszynie.

Porgram na standardowym wejściu powinien przyjmować listę wyrazów zakodowanych w formacie UTF-8, po jednym wyrazie na linię 
(proszę wykonać odpowiedni stripping białych znaków na początku i końcu napisu dla pewności). Np::
  
  peis
  kompóter
  maka



Program powinien generować na standardowym wyjściu listę propozycji poprawnych napisów (wyrazów). Lista napisów powinna być 
rozdzielona znakiem przecinka. Białe znaki są nieistotne. Np::

  pies, pejs
  komputer
  mąka, mąką, mała


Typowe wywołanie programu to::

  cat mistakes.txt | ./spellchecker


Testowanie jakości spellcheckera
--------------------------------

Jakość sugerowanych poprawek przez spellcheckera można zmierzyć programem spellrank.py. Program ten analizuje wyjście 
generowane przez program spellcheckera i ocenia każdy pojedynczy przypadek następująco:

* oceniana jest ILOŚĆ odpowiedzi oraz POZYCJA dobrej odpowiedzi na liście, tzn. im mniej spellchecker zaproponuje wariantów tym lepiej, im wcześniej dobra odpowiedź pojawia się na liscie wariantów tym lepiej,
* w najlepszym przypadku, gdy lista odpowidzi jest 1 elementowa i zawiera ono dobrą propozycję, program oceniający przyznaje 1.0 punkt,
* lista opdowiedzi nie może być dłuższa niż 5 elementów (włącznie), jeśli jest dłuższa program oceniający automatycznie przyznaje 0 punktów za to zadanie,
* w innych przypadkach program oceniający odejmuje odpowiedni ułamek punktów uwzględniając średnią ważoną pozycji (60%) oraz długości listy (40%).

Typowe uruchomienie programu oceniającego wygląda następująco::

  cat mistakes.txt | ./spellchecker | pjn/lab02/spellrank/spellrank.py -f correct.txt


Program oceniający posiada także tryb verbose aktywowany przełącznikiem ``-v``.

Maksymalna ilość punktów do zdobycia jest zawsze równa liczbie przypadków (linii w pliku testowym). Im więcej punktów uzyska spellchecker tym lepiej.

Materiały:
----------
- sjp.txt - słownik polskich wyrazów z którego korzysta m.in. aspell
- bledy.txt - plik z błedami służące do wyznaczenia P(w|c)
- `Milionowy Podkorpus Języka Polskiego <http://nkjp.pl/index.php?page=14&lang=0>`_ który posłuży do wyznaczenia P(c)
- Dorosz K., Automatyka 2008/1, `Automatyczne sprawdzanie poprawności pisowni w języku polskim oparte na odległości Levenshteina <http://journals.bg.agh.edu.pl/AUTOMATYKA/2008-01/Auto03.pdf>`_
