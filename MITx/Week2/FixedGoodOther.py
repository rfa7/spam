balance = 4773
annualInterestRate = 0.2
MIR = annualInterestRate/12
inc = 10
bal = balance
while bal > 0:
    bal = balance
    for i in range(12):
        bal = bal - inc
        odsetki = bal*MIR
        pozostaly = bal + odsetki
        bal = pozostaly
    inc += 10
print 'Lowest Payment: ' + str(inc - 10)