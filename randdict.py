
import random
kulki = {'a':2, 'b':2,'c':2,'d':2,'e':1,'f':2,'g':2,'h':2,'i':2,'j':2,'k':2,'l':2 }
ListaKulki = {}
for i in kulki:
    ListaKulki[i] = kulki[i]
print 'listakulki:'
print kulki
print ListaKulki
print 'USUWAMY z nowego slownika i porownujemy'
"""
1 sposob:
    remove = [k for k in mydict if k == val]
    for k in remove: del mydict[k]
2 sposob ***:
    mydict = { k : v for k,v in mydict.iteritems() if k != val }
3 zamiast keys() mozemy uzyc items(), jezeli chcemy operowac na wartosciach, a nie na kluczach np:
    for k in mydict.keys():
        if k == 'two':
            del mydict[k]
 LUB:
    for k, v in mydict.items():
        if v == 3:
            del mydict[k]
"""
wwi=1
for i in ListaKulki.keys():
    del ListaKulki[i]
    wwi += 1
    if wwi >7:
        break
print ' Nowa ListaKulki: '
print ListaKulki

gr1 = random.sample(kulki.items(),4)
print "Lista losowych 4 ze slownika"
print gr1
print gr1[0]
print gr1[0][1]+gr1[1][1]
print sum(j for i,j in gr1)
nowydict = {k:v for k,v in kulki.items()}
print nowydict
print kulki
