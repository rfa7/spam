balance = 736
annualInterestRate = 0.2

PB = balance
MIR = (annualInterestRate) / 12.0
MMP = PB / 12.0
total = 0
licz = 0
for i in range(12):
    z = 12 - i
    if i == 0:
        MMP = PB/12.0
        MUB = PB - MMP
        UMB = MUB + (MIR*MUB)
    else:
        MMP = UMB/z
        MUB = UMB - MMP
        UMB = MUB + (MIR*MUB)
    total += MMP
    licz += 1
AvgTotal = total/12.0
if AvgTotal > round(AvgTotal):
   AvgTotal = round(AvgTotal) + 10
print AvgTotal      
print 'Lowest Payment: ' + str(round(AvgTotal,-1))

