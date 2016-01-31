print('wybierz liczbe od 0 do 100')
min = 0
max = 100
ans = (min + max)/2
print('czy szukana liczba jest ' + str(ans) + '?')
o = raw_input('Odpowiedz t - tak, d - liczba jest za duza, m - liczba jest za mala: ')
guess = 0
while o != 't' or o != 'z':
    if o == 'd':
        max = ans
        ans = (min + max)/2
        o = raw_input('czy szukana liczba jest ' + str(ans) +' Odpowiedz t/d/m: ')
        guess += 1
    elif o == 'm':
        min = ans
        ans = (min + max)/2
        o = raw_input('czy szukana liczba jest ' + str(ans) +' Odpowiedz t/d/m: ')
        guess += 1
    elif o == 't':
        print('')
        print('========================================')
        print('Liczba poszukiwan: ' + str(guess))
        print('szukana liczba to: ' + str(ans) + '. Gratulacje!')
        print('========================================')
        break
    elif o == 'z':
        print('Koniec. Do zobaczenia!')
        break
    else:
        print('czy szukana liczba jest ' + str(ans) + '?')
        o = raw_input('Odpowiedz t - tak, d - liczba jest za duza, m - liczba jest za mala: ')
