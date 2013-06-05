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

* Wyrazy bardzo często występujące w tekście, bądź występujące tylko w 1 tekście nie niosą z sobą informacji
* Zgodność tekstów sprowadza się do dokładnej zgodności wyrazów

Z pierwszym problem radzimy sobie zazwyczaj w następujący sposób:

* W słowniku przechowywujemy jedynie wyrazy które występują w więcej niż 1 tekście
* Usuwamy wyrazy które występują w więcej niż 70% tekstów
* W macierzy A której wiersze reprezentują teksty a kolumny wyrazy, wartość w danej komórce zawiera wagę danego wyrazu w danym tekście. 

Istnieje wiele sposobów wyznaczenia takiej wagi. Najbardziej popularną jest metryka TF-IDF 
(Term Frequency - Inverted Document Frequency) powstała przez iloczyn składnika TF i IDF. Jako TF można ustalić tf(t,d) = 1
jeśli wyraz t występuje w dokumencie d, 0 w przeciwnym wypadku. Miara IDF określa "rzadkość" danego wyrazu:

.. image:: http://latex.codecogs.com/gif.latex?IDF(t)%3Dlog%5Cfrac%7B%7CD%7C%7D%7B%7C%5C{d:t%5Cind%5C}%7C%7D

.. image:: http://latex.codecogs.com/gif.latex?COSINE(t_i%2Ct_j)%3D1-%5Cfrac%7B%7Ct_i%20%5Ccdot%20t_j%7C%7D%7B%7Ct_i%7C%7Ct_j%7C%7D

