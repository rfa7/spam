balance = 320000
annualInterestRate = 0.2
MIR = (annualInterestRate)/12
low = balance / 12
high = (balance * (1 + MIR)**12) / 12
ans = (high + low)/2
eps = 0.01
nbalance = balance
while abs(nbalance) > eps:
    nbalance = balance
    ans = (high + low)/2
    for i in range(12):
        nbalance -= ans
        odsetki = nbalance*MIR
        nbalance += odsetki
        print nbalance
    #print 'Balance is ' +str(balance)
    if nbalance > 0:
        low = ans
    else:
        high = ans
#    if 0.2>balance>=0:
print 'Lowest Payment: ' + str(round(ans,2))
#        break 
    
