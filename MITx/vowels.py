
vowels = 'aeiou'
s = 'azcbobobegghakl'
suma = 0
for i in s:
    if i in vowels:
        suma += 1

print 'Number of vowels: ' + str(suma)
