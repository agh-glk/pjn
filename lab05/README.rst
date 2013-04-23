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

* Zbudować na podstawie CLP słownik 'a tergo' (od tyłu - spis wyrazów ułożony w kolejności alfabetycznej liter liczonych od końca).

* Rozpiąć dany słownik na strukturze trie w postaci forma -> napis który należy odciąć aby uzyskać formę podstawową, napis który należy dokleić aby otrzymać formę podstawową. 
Na przykład: domem -> ("em",""), psem -> ("sem","ies")

* Dla badanego wyrazu odnaleźć formę(formy) w słowniku których wspólny podciąg dopasowany od tyłu jest najdłuższy
* W przypadku gdy otrzymamy kilka takich form, wybrać te którym odpowiada najliczniejszy zbiór identycznych przekształceń.

Przykład - powiedzmy że stemujemy wyraz spoza słownika "zazazem". 

Jeśli najbardziem dopasowane będą formy  

* domem -> ("em",""), 
* psem -> ("sem","ies"), 
* kotem -> ("em","") 

to dla stemmingu "zazazem" wybierzemy przekształcenie ("em","") jako najczęściej występujące.

Materiały
---------

* `PLP <https://github.com/agh-glk/plp>`_
* `Stemmer Portera <http://snowball.tartarus.org/algorithms/porter/stemmer.html>`_ 
