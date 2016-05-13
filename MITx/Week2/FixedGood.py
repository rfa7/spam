balance = 3329
annualInterestRate = 0.2
#initialBalance = balance 
MonthlyInterestRate = annualInterestRate/12.0 
lowestRepayment = 10
while (balance > 0): 
    for i in range(12):
        if i == 0:
            MonthlyUnpaidBalance = (balance - lowestRepayment)
            newbalance = (MonthlyInterestRate*MonthlyUnpaidBalance) + MonthlyUnpaidBalance
        else:
            MonthlyUnpaidBalance = (newbalance - lowestRepayment)
            newbalance = (MonthlyInterestRate*MonthlyUnpaidBalance) + MonthlyUnpaidBalance
#            print 'lowest ' + str(lowestRepayment)
    if (newbalance < 0):
        break
    else:
        #initialBalance = balance
        lowestRepayment += 10
print 'Lowest Payment: ' + str(lowestRepayment)
