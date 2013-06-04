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
ponieważ nie uwzględnia kolejności występowania wyrazów w tekście, a jedynie fakt ich wystąpienia

Można następnie porównać dwa teksty w postaci wektorowej korzystając już ze znanej metryki cosinusowej: 

.. image:: http://latex.codecogs.com/gif.latex?COSINE(t_i%2Ct_j)%3D1-%5Cfrac%7B%7Ct_i%20%5Ccdot%20t_j%7C%7D%7B%7Ct_i%7C%7Ct_j%7C%7D


* Jeśli w1:n oznacza ciąg wyrazów w1, w2, ... , wn
* Jaka jest wartość P(w1:n)
