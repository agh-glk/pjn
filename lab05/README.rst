Naiwny Stemmer
==============

Cel ćwiczenia:
--------------
Zapoznanie się z zagadnieniem sprowadzania nieznanych wyrazów (tzn. nie znajdujących się w słowniku CLP) 
do formy podstawowej 

Opis ćwiczenia:
---------------

Język polski cechuje się niezwykle bogatą fleksją - dany wyraz może być reprezentowany w tekście 
przez wiele jego form gramatycznych.

Stanowi to pewne utrudnienie przy obróbce algorytmicznej nieprzetworzonego tekstu. Aby rozpoznać które
formy w tekście odpowiadają danemu wyrazowi, należy poddać tekst procesowi stemmingu tzn. sprowadzenia form tekstowych
do formy podstawowej danego wyrazu (np. dla czasownika będzie to bezokolicznik, 
dla rzeczownika mianownik liczby pojedynczej itd.)

Algorytm który tego dokonuje jest trywialny w przypadku gdy potrafimy odnaleźć daną forme w słowniku fleksyjnym. 
Problem nie jest jednak tak prosty w sytuacji gdy nie posiadamy słownika, bądź badany wyraz który się w nim nie znajduje.

Jednym z pierwszych algorytmów stemmingu był zaproponowany przez Martina Portera w 1980r. algorytm dla j.angielskiego.
Ten algorytm sprowadzał się do kilkunastu prostych reguł przekształcania napisów. Na przykład: dla form imiesłowowych 
kończących się na -ed algorytm obcinał tą końcówkę sprowadzając przykładowo formę "looked" 
do formy bezokolicznikowej "look". 

Zbudowanie jednak takich reguł dla języka polskiego byłoby bardzo żmudne - dlatego do ich budowy posłużymy się słownikiem
fleksyjnym.

Plan ćwiczenia
--------------


Materiały
---------

* `PLP <https://github.com/agh-glk/plp>`_
* `Stemmer Portera <http://snowball.tartarus.org/algorithms/porter/stemmer.html>`_ 
