kwota = 1000
a =  kwota/2
test = 0
while kwota >10:
	for i in range(5):
		kwota /= 2
		test += 1
		print test
		print 'kwota= ' + str(kwota)
	print kwota
#	break

