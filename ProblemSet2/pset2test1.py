# Paste your code into this box
num = 1
newbalance = balance
total = 0

while num <= 12:
    minPayment = newbalance * monthlyPaymentRate
    newbalance -= minPayment
    interest = newbalance * (annualInterestRate / 12)
    newbalance += interest
    total += minPayment

    
    print 'Month: ' + str(num)
    print 'Minimum monthly payment: ' + str(round(minPayment,2))
    print 'Remaining balance: ' + str(round(newbalance,2))
    
    num += 1
    
    
print 'Total paid: ' + str(round(total,2))
print 'Remaining balance: ' + str(round(newbalance,2))   