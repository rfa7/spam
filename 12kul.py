'''
gra 12 KUL - 3 wazenia
Jedna z kul waży mniej lub więcej niż pozostałe.
12 kul, a-l, dzielimy je na 3 losowe grupy.
Dwie pierwsze grupy ważymy.
Jeżeli grupy ważą tyle samo:
    - zajmujemy się 3 grupą
Jeżeli ich waga nie jest taka sama:
    - zapamiętujemy wynik ważenia

'''
import random
kulki = {
        'a':2, 'b':2,'c':2,'d':2,'e':1,'f':2,'g':2,'h':2,'i':2,'j':2,'k':2,'l':2
}

#TEST
print kulki['a'] + kulki['b']

#Funkcja waga zwraca w wyniku CIEZSZA KULKE, a jesli waza tyle samo - zwraca 0
def waga(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 0

#Test wazenia OK
print 'Wynik wazenia: ' + str(waga(kulki['a'],kulki['b']))

gr1 = []
gr2 = []

#losowe4 = random.sample(kule,4)
losowe4 = random.sample(kulki,4)
print 'losowe kule to: ' + str(losowe4)
razem = 0
for i in losowe4:
    razem += kulki[i]

print 'ich suma to: ' + str(razem)
for x in losowe4:
#    print x
#    print kule
#    kule.remove(x)
#    print 'USUNIETO!!!!'
    gr1.append(x)
    del kulki[x]

print kulki
print gr1
