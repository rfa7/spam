zmienna = 10
www = 0
zet = 10
while zmienna > 0 :
    if www > 20:
        print 'www to ' +str(www)
        break
    zmienna = 10
    for i in range(5):
        zmienna -= 1
        www += 1
        #print i
        print 'zmienna to ' +str(zmienna)
        