balance = 4773
annualInterestRate = 0.2
MIR = annualInterestRate/12
inc = 10
while balance > 0:
    balance = 4773
    for i in range(12):
        balance = balance - inc
        odsetki = balance*MIR
        pozostaly = balance + odsetki
        balance = pozostaly
    inc += 10
print 'Lowest Payment: ' + str(inc - 10)