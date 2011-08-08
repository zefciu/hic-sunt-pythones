=========================================================
Hic sunt pythones - magiczna strona pythona
=========================================================
--------------------------------------
Streszczenie
--------------------------------------
Chcąc przedstawić Pythona jako programowalny język programowania omawiam dwa
zagadnienia: deskryptory i metaklasy. Deskryptory są specjalnymi obiektami
należącymi do klasy i zmieniającymi sposób dostępu do członków jej
instancji. Są one wszechobecne w Pythonie i korzystamy z nich nawet o tym
nie wiedząc. Metaklasy to ,,klasy klas''. Dzięki nim możemy dodać własną
logikę do procesu tworzenia klas i dziedziczenia. Wykorzystanie tych
elementów języka pozwoli nam tworzyć obiekty o niedostępnych normalnie
możliwościach, jednocześnie proste i intuincyjne w obsłudze.

------------------------------------------------
(treść artykułu)
------------------------------------------------

Czasami w ramach PR-u różnych trudnych i zawiłych języków programowania słyszymy
pewne przeciwstawienie ,,programowalnych języków programowania'' językom
prostym, ale ,,sztywnym'', nie dającym programiście swobody. Kiedy czynimy
pierwsze kroki w Pythonie, może nam się wydawać, że zalicza się on do tej
drugiej grupy. Nic bardziej mylnego. Pod warstwą prostoty umożliwiającą każdemu
szybkie wdrożenie znajduje się skomplikowany mechanizm, w którym praktycznie
wszystko można zmienić i zastąpić. 

Deskryptory
=================

Czym jest deskryptor?
------------------------------

Descryptorem jest każdy obiekt, który definiuje metodę ``__get__()``
Dodatkowo deskryptor może definiować też metody ``__set__()`` i
``__delete__()``. Metody te określają specjalny sposób traktowania atrybutów
obiektów klasy, do której należą. Deskryptory definiujące metodę
``__set__()`` nazywane są **deskryptorami danych**, z czym wiąże się nieco inne
ich traktowanie. Aby zrozumieć działanie deskryptorów należy poznać sposób, w
jaki Python obsługuje dostęp do atrybutu obiektu.

Algorytm dostępu do atrybutu
----------------------------------------
Załóżmy, że mamy obiekt ``obj`` typu ``Сls``. Próba uzyskania ``obj.att``
sprawi, że Python będzie próbował następujących rzeczy (dla uproszczenia
pomijamy klasy bazowe dla ``Cls``).

#. Jeśli istnieje ``Cls.__dict__['att']`` i jest to deskryptor **danych**,
   zostaje zawołana jego metoda ``__get__()`` i zwrócony wynik.

#. Jeśli istnieje ``obj.__dict__['att']``, zostanie on zwrócony.

#. Jeśli istnieje ``Cls.__dict__['att']`` i jest to deskryptor **niedanych**,
   zostaje wywołana jego metoda ``__get__()`` i zwrócony wynik.

#. Jeśli istnieje ``Cls.__dict__['att']``, zostanie on zwrócony.

#. Rzucony zostaje wyjątek ``AttributeError``.

Z kolei przy przypisaniu ``obj.att = 'value'``:

#. Jeśli istnieje ``Cls.__dict__['att']`` i jest to deskryptor **danych**,
   zostaje zawołana jego metoda ``__set__()``.

#. ``obj.__dict__['att']`` zostaje ustawione na ``value``.

Algorytm ten może wydawać się zawiły, jednak ma on swoje uzasadnienie. Przede
wszystkim należy zauważyć, że:

#. Deskryptory muszą być przypisane do **klasy** a nie instancji.

#. Jeśli wykonamy przypisanie atrybutu będącego deskryptorem *niedanych*,
   ukrywamy ten deskryptor i próba odczytania wartości atrybutu już nie wiąże
   się z wywołaniem deskryptora, a zwraca po prostu wartość, którą
   przypisaliśmy.

#. Deskryptory **danych** mają zawsze najwyższy priorytet i ich wywołanie zawsze
   zastępuje normalny dostęp do ``__dict__()`` obiektu.



Deskryptory, które już znamy
------------------------------------
Korzystając z Pythona na co dzień nie mogliśmy nie spotkać się z pewnymi
deskryptorami, które są jego integralną częścią. Najpopularniejszymi są:

Funkcja:
    Funkcje są deskryptorami nie-danych. Ich ``__get__()`` odpowiada za
    stworzenie obiektu, który przy wywołaniu funkcji jako metody przekaże jej
    odpowiedni ``self``. Jeżeli więc chcemy stworzyć obiekty, które będą w pełni
    emulować funkcje należy zdefiniować dla nich zarówno ``__call__()`` jak i
    ``__get__()``. Funkcje są deskryptorami *niedanych* Możemy je nadpisać w
    instancji.

member_descriptor:
    Te deskryptory tworzone są, jeśli przy tworzeniu nowostylowej klasy ustawimy
    dla niej atrybut \type{__slots__}. Odpowiadają one za dostęp do tak
    zdefiniowanych atrybutów.

property: 
    Jeśli nie potrzebujemy pełnej obiektowej mocy deskryptorów, możemy jest
    tworzyć *ad-hoc* w definicji klasy przy użyciu klasy ``property``. Klasa ta
    tworzy zawsze *deskryptory danych*. Jeśli nie zdefiniujemy funkcji ``fset``,
    domyślny ``__set__()`` zwróci błąd.

Przykładowa implementacja
--------------------------------

Poniższy deskryptor danych dopuszcza jedynie wartości całkowite. Dodatkowo w
przypadku braku ustawienia wartości podaje wartość domyślną::

    import random as rnd
    import string

    class IntegerDescriptor(object):
        def __init__(self, default=0):
            self.name = ''.join(
                (rnd.choice(string.ascii_lowercase) for i in range(10))
            )
            self.default = default
      
        def __get__(self, inst, cls):
            return inst.__dict__.get(self.name, self.default)
    
        def __set__(self, inst, v):
            v = int(v) # May raise TypeError
            inst.__dict__[self.name] = v
    
        def __delete__(self, inst):
            del inst.__dict__[self.name]

Przykład użycia::
    >>> from integer_des import IntegerDescriptor
    >>> class A(object):
    ...     x = IntegerDescriptor(default=1)
    ... 
    >>> a = A()
    >>> a.x
    1
    >>> a.x = 10
    >>> a.x
    10
    >>> a.x = 3.14159
    >>> a.x
    3
    >>> a.x = 'abcd'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "integer_des.py", line 15, in __set__
        v = int(v) # May raise TypeError
    ValueError: invalid literal for int() with base 10: 'abcd'



Metaklasy
=======================

Czym jest metaklasa?
----------------------------------------

W języku Python wszystko jest obiektem i wszystko też należy do jakiejś klasy.
Klasy są obiektami *wywoływalnymi* (przy wywołaniu zwracają instancję) będącymi
najczęściej instancjami klasy ``type`` (ta zaś jest instancją samej siebie) lub
jej klasy potomnej. ``type`` jest więc podstawową metaklasą i prawie wszystkie
klasy nowostylowe, których używamy do niej należą (choć w bibliotece
standardowej mamy na przykład metaklasę ``ABCMeta``, do której należą  
klasy abstrakcyjne).
 
Tworzenie własnych metaklas daje nam możliwość dodawania własnej logiki do
procesu tworzenia klas i dziedziczenia. Konstruktor metaklasy przyjmuje cztery
argumenty. Pierwszy: (oznaczać będziemy go ``cls`` zamiast ``self`` to
podobnie jak w przypadku normalnych obiektów konstruowana właśnie klasa. Drugi
(``clsname``), to nazwa klasy. Trzeci (``bases``) to entka klas bazowych.
Czwarty (``dict_``) - słownik zawierający zawartych w definicji członków klasy. 

Znaną nam dobrze konstrukcję::

    class MojaKlasa(Bazowa1, Bazowa2):
        klucz1 = wartosc1
        klucz2 = wartosc2

możemy rozumieć, jako "cukier syntaktyczny" dla::

    MojaKlasa = type('MojaKlasa', (Bazowa1, Bazowa2), {
        'klucz1': wartosc1,
        'klucz2': wartosc2,
    })

Wiedząc, w jaki sposób wołany jest konstruktor metaklasy możemy go nadpisać i
dodawać dowolną logikę, która ma być wykonana w momencie tworzenia klas.
