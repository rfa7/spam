# -*- coding: utf-8 -*-
'''
zapytaj o liczbę
poproś o określenie czy wskazana liczba spełnia oczekiwania, czy jest też za
duża lub za mała
'''

print('Pomyśl liczbę od 0 do 100')
min = 0
max = 100
ans = (min+max)/2

def pytanie():
    x = str(raw_input('Czy liczba ' + str(ans) + ' jest właściwa? T-tak, D-za duża, M-za mała: '))
    return x
x = pytanie()
def zlaOdp():
    while x != 'd'or x != 'm' or x != 't':
        print('Podano niewłaściwą odpowiedź - możliwe T,D,M. Spróbuj ponownie')
        return pytanie() 
if x  == 'T':
    print('OK')
elif x == 'D':
    print('xxxxxD')
    min = ans
elif x =='M':
    print('asdfasdfaM')
    max = ans
else:
    zlaOdp()
