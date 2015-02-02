monthlyInterestRate = (annualInterestRate)/12.0

# set initial values
lo = balance/12
hi = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

newbalance = balance
monthlyPayment = (hi + lo) / 2.0

#print ' '
#print 'initial balance ' + str(balance)
#print 'initial hi ' + str(hi) + ' initial lo ' + str(lo)
#print 'initial mp ' + str(monthlyPayment)

while (newbalance > 0.1 or newbalance < -0.1):
    
    newbalance = balance  # initialise for another year
    num = 1               # set month to be 1
    while num <= 12:
        newbalance -= monthlyPayment
        interest = newbalance * (annualInterestRate / 12)
        newbalance += interest
        num += 1
#    print 'end of year ' + 'newbalance ' + str(newbalance)

        
    if newbalance < -0.1:      # balance negative means paying too much
        hi = monthlyPayment
        monthlyPayment = (hi + lo) / 2.0
    elif newbalance > 0.1:     # balance positive means not paying enough
        lo = monthlyPayment
        monthlyPayment = (hi + lo) / 2.0
        
#    print 'hi ' + str(hi) + ' lo ' + str(lo)
#    print 'mp ' + str(monthlyPayment)

print 'Lowest Payment: ' + str(round(monthlyPayment,2))