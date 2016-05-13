balance = 3329
annualInterestRate = 0.2

PB = balance

#Monthly interest rate
MIR = (annualInterestRate) / 12.0
'''
#Monthly unpaid balance
MUB = (PB) - (MMP)
#Updated balance each month
UMB = (MUB) + (MIR*MUB)
'''
#Monthly minimum paymant
MMP = PB / 12.0
total = 0
licz = 0
for i in range(12):
    z = 12 - i
    print 'z = ' + str(z)
    if i == 0:
        MMP = PB/12.0
        MUB = PB - MMP
        UMB = MUB + (MIR*MUB)
        
    else:
        MMP = UMB/z
        MUB = UMB - MMP
        UMB = MUB + (MIR*MUB)
        
    
    
    print UMB
    total += MMP
    print 'total =' + str(total)
    
    licz += 1
    print 'licz = ' + str(licz)
    print 'MMP = ' +str(MMP)
    print '------------'
print total
AvgTotal = total/12.0
#Fixed = 
print AvgTotal
print round(AvgTotal,-1)

