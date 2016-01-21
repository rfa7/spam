# -*- coding: utf-8 -*-
'''
gra 12 KUL - 3 wazenia
Jedna z kul waży mniej lub więcej niż pozostałe.
*****Import modułu losowania
*****Utworzenie słownika (dictionary) kulki
*****Funkcja 'waga' zwracająca cięższą stronę lub 0  gdy strony są równe
*****
*****12 kul, a-l, dzielimy je na 3 losowe grupy: gr1, gr2, gr3.
Dwie pierwsze grupy (gr1, gr2) ważymy.
Jeżeli grupy ważą tyle samo:
    - zajmujemy się 3 grupą
        1. dzielimy na 2 grupy po 2 kulki i dobieramy 3 grupę z 2 pozostałych kulek - grupę bazową
        LUB
        1. wybieramy dowolne 3(z tej grupy gr3) i ważymy je z grupą bazową, zapamiętujemy wynik.
            -jeżeli == >>>ważymy pozostałą kulkę z jedną bazową i otrzymujemy wynik
            -jeżeli != >>> ważymy dowolne 2 z nich
                -jeżeli == >>> szukaną kulką jest kulka 3 i jej waga została wskazana w poprzednim ważeniu
                -jeżeli != >>> szukaną kulką jest kulka która zachowuje się jak w pkt. 1.
        
Jeżeli ich waga nie jest taka sama:
    - zapamiętujemy wynik ważenia
    - tworzymy 3 grupy w następujący sposób:
        grA tworzą pierwsze 3 kule z gr1, grB tworzą pierwsze 3 kulki z gr2, grC tworzą 4-te kulki z gr1 i gr2 oraz pierwsza (dowolna) kulka z gr3
    -WAZYMY grA i grB. Jeżeli grupy ważą tyle samo:
        - zajmujemy się grC:
            - WAZYMY dwie kulki: jedną z gr3 (dowolną) i jedną z gr1. Jeżeli kulka z gr1 przyjmuje wynik ważenia identyczny z ważeniem pierwszym, oznacza to, że to ta kulka waży inaczej niż pozostałe tzn. jest lżejsza lub cięższa, zgodnie z ważeniami 1 i 3 (pierwszym i trzecim). Jeżel natomiast kulki ważą tyle samo, oznacza to, iż szukaną kulką o innej wadze jest kulka 4-ta z gr2. Jej waga została wskazana w pierwszym ważeniu.
'''

import random
kulki = {'a':2, 'b':2,'c':2,'d':2,'e':1,'f':2,'g':2,'h':2,'i':2,'j':2,'k':2,'l':2 }

#TEST
#print kulki['a'] + kulki['b']


#Funkcja waga zwraca w wyniku CIEZSZA KULKE, a jesli waza tyle samo - zwraca 0
def waga(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 0

#Test wazenia OK
#print 'Wynik wazenia: ' + str(waga(kulki['a'],kulki['b']))

gr1 = random.sample(kulki,4)
for x in gr1:
    del kulki[x]
gr2 = random.sample(kulki,4)
for x in gr2:
    del kulki[x]
gr3 = random.sample(kulki,4)
for x in gr3:
    del kulki[x]

#losowe4 = random.sample(kule,4)
#losowe4 = random.sample(kulki,4)
#print 'losowe kule to: ' + str(losowe4)
print 'AKTUALNY SLOWNIK kulki to: ' + str(kulki)

razem = 0
for i in losowe4:
    razem += kulki[i]
print 'ich suma to: ' + str(razem)

#for x in losowe4:
#    print x
#    print kule
#    kule.remove(x)
#    print 'USUNIETO!!!!'
#    gr1.append(x)
#    del kulki[x]

print kulki
print gr1 
print 'TESTGCOMMIT'
