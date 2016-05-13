annualInterestRate = 0.2
balance = 4213
monthlyPaymentRate = 0.01

'''
MIR - MonthlyInterestRate
MMP - MinimumMonthlyPayment
MUB - MonthlyUnpaidBalance
UBEM - UpdatedBalanceEachMonth 
'''

MIR = annualInterestRate/12.0
MMP = monthlyPaymentRate * PreviousBalance
MUB = PB - MMP
UBEM = MUB + MIR * MUB

zaplacono = 0
for i in range(1,13):
    MMP = 
