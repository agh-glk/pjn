Podobieństwo tekstów
=====================

Cel ćwiczenia
-------------

Celem ćwiczenia jest zapoznanie się z podstawowymi metodami wektorowego przetwarzania tekstu, a 
w szczególności z mechanizmem Latent Semantic Analysis



Opis ćwiczenia
--------------

Model Wektorowy Tekstu jest modelem algebraicznym wykorzystywanym dla reprezentacji tekstu. Teksty reprezentowane 
są przez wektory:


.. image:: http://latex.codecogs.com/gif.latex?t_i=(w_1,w_2,...,w_n)

Gdzie i-ty wektor t reprezentuje i-ty tekst w postaci wag przypisanych dla poszczególnych wyrazów w nim występujących, 
1 pozycja wektora na każdy z wyrazów słownika, z odpowiednią wagą. Tego typu reprezentacja nosi także nazwę Bag Of Words,
ponieważ nie uwzględnia kolejności występowania wyrazów w tekście, a jedynie fakt ich wystąpienia.

Można następnie porównać dwa teksty w postaci wektorowej korzystając już ze znanej metryki cosinusowej: 

.. image:: http://latex.codecogs.com/gif.latex?COSINE(t_i%2Ct_j)%3D1-%5Cfrac%7B%7Ct_i%20%5Ccdot%20t_j%7C%7D%7B%7Ct_i%7C%7Ct_j%7C%7D

Takie podejście ma pewne wady, a mianowicie:

* Wyrazy bardzo często występujące w tekście, bądź występujące tylko w 1 tekście nie niosą z sobą informacji a mają mocny wpływ na podobieństwo (patrz: prawo Zipfa)
* Zgodność tekstów sprowadza się do dokładnej zgodności wyrazów

Z pierwszym problem radzimy sobie zazwyczaj w następujący sposób:

* W słowniku przechowywujemy jedynie wyrazy które występują w więcej niż 1 tekście
* Usuwamy wyrazy które występują w więcej niż 70% tekstów
* W macierzy A której wiersze reprezentują teksty a kolumny wyrazy, wartość w danej komórce zawiera wagę danego wyrazu w danym tekście. 

Istnieje wiele sposobów wyznaczenia takiej wagi. Najbardziej popularną jest metryka TF-IDF 
(Term Frequency - Inverted Document Frequency) powstała przez iloczyn składnika TF i IDF. Jako TF można ustalić tf(t,d) = 1
jeśli wyraz t występuje w dokumencie d, 0 w przeciwnym wypadku. Miara IDF określa "rzadkość" danego wyrazu:

.. image:: http://latex.codecogs.com/gif.latex?IDF(t)%3Dlog%5Cfrac%7B%7CD%7C%7D%7B%7C%5C{d:t%5Cin%20d%5C}%7C%7D

Dla D - zbioru wszystkich dokumentów.

TF-IDF(t,d) określamy jako TF-IDF(t,d)=TF(t,d)*IDF(t).

Te zmiany jednak nadal pozostawiają nas w obrębie porównywania _dokładnej_ zgodności wyrazów.

W celu uogólnienie podejścia, dokonuję się często przekształcenia oryginalnej macierzy term-document A o wymiarach n x m dokonując jej rozkładu 
na wektory własne

.. image:: http://latex.codecogs.com/gif.latex?A%3D%20U%20%5CSigma%20V^%5Ctop

Gdzie macierz U o wymiarach n x l jest macierzą pojęć (term) przedstawionych w nowym układzie współrzędnych a V o wymiarach m x l analogiczną macierzą wyrazów. Środkowa macierz
sigma jest macierzą przekątniową l wartości własnych. Wymiary nowego układ współrzędnych wyznaczonych przez wektory własne nosi nazwę
_concepts_ albo ogólniej _topics_.

Taką reprezentację można przekształcić do postaci przybliżonej

.. image:: http://latex.codecogs.com/gif.latex?A'%3D%20U'%20%5CSigma'%20V'^%5Ctop

Tworzymy macierze U' o wymiarach n x l', V' o wymiarach m x l' wybierając jedynie l' (l' << n) największych wartości własnych.

Można teraz poszukiwać podobieństw tekstu korzystając z metryki cosinusowej, ale w odniesieniu do wektorów w nowej przestrzeni.

Taka reprezentacja nie dość, że jest znacznie bardziej oszczędna (l' jest zazwyczaj rzędu setek), to okazuje się, że 
dla wyszukiwania podobnych treści jest znacznie skuteczniejsza (usuwa "szum").

Metoda ta, znana jako Latent Semantic Analysis ma pewną jednak wadę - koncepty jako wektory nie mają "ludzkiej" interpretacji
ze względu na choćby zawarte w nich wartości ujemne. Często stosuje się zatem dla modelowania tematów metody które nie mają
tej wady, nawet kosztem utraty dokładności reprezentacji. Takim modelem jest np. Latent Dirichlet Allocation (LDA).

Zadanie:
--------

1. Przedstawić zbiór notatek PAP w postaci modelu Bag Of Words po sprowadzeniu do form podstawowych korzystając ze
stemmera słownikowego

2. Zbudować model LSA i LDA korzystając np. z pakietu gensim 
(tutorial : http://radimrehurek.com/gensim/tutorial.html zawiera praktycznie całość zadania z wyjątkiem dostarczenia 
danych wejściowych)

3. Napisać program który dla danej notatki PAP przedstawi dla niej N najbardziej zbliżonych tematycznie notatki, wypisze jej
najistotniejsze "topici" w modelu LSA i LDA.

Notatki PAP znajdują się na wierzbie na ścieżce /usr/local/teksty/polskie_iso/wspolczesne/Prasa/pap-all.not






