balance = 320000
annualInterestRate = 0.2
MIR = (annualInterestRate)/12
low = balance / 12
high = (balance * (1 + MIR)**12) / 12
ans = (high + low)/2
eps = 0.01
dlug = balance
while abs(balance) > eps:
#    xx = balance
    ans = (high + low)/2
    for i in range(12):
        dlug = dlug - ans
        odsetki = dlug*MIR
        pozostaly = dlug + odsetki
        dlug = pozostaly
    #print 'Balance is ' +str(balance)
    if dlug > 0:
        low = ans
    else:
        high = ans
#    if 0.2>balance>=0:
print 'Lowest Payment: ' + str(round(ans,2))
#        break 
    
