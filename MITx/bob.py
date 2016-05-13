s = 'azcbobobegghakl'
x = 0
liczba_bob = 0
for i in s:
    if s[x:x+3] == 'bob':
       liczba_bob += 1
    x += 1
print 'Number of times bob occurs is: ' + str(liczba_bob)
