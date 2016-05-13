def gcdIter(a,b):
    '''
    a,b - liczby calkowite dodatnie
    zwraca: dodatnia liczbe najwiekszy dzielnik obu liczb (a,b)
    '''
    if a==b:
        return a
    if a < b:
        x = a
        while x > 0:
            if a%x == 0 and b%x ==0:
                return x
            else:
                x -= 1
    if b < a:
        x = b
        while x > 0:
            if a%x == 0 and b%x ==0:
                return ;
            else:
                x -= 1



