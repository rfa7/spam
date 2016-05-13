balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#Monthly interest rate
MIR = annualInterestRate/12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#MMP = monthlyPaymentRate * balance
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#MUB = balance - MMP
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#UBM = MUB + (MIR * MUB)
month  = 0
total = 0
for i in range(12):
    month += 1
    MMP = monthlyPaymentRate * balance
    MUB = balance - MMP
    UBM = MUB + (MIR * MUB)
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(MMP,2))
    print 'Remaining balance: ' + str(round(UBM,2))
    balance = UBM
    total += MMP 
print 'Total paid: ' + str(round(total,2))
print 'Remaining balance: ' + str(round(UBM,2))