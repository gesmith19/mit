# test case 1
balance = 3329
annualInterestRate = 0.2

# test case 2
#balance = 4773
#annualInterestRate = 0.2


monthlyInterestRate = (annualInterestRate)/12.0
lo = balance/12
hi = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
newbalance = balance
#lo = round(lo,2)
#hi = round(hi,2)
print 'lo ' + str(lo)
print 'hi ' + str(hi)

total = lo + hi
print 'total ' + str(total)
monthlyPayment = (hi + lo) / 2.0
#monthlyPayment = round(monthlyPayment,2)
print 'mp ' + str(monthlyPayment)
count = 0

while (newbalance !=0.0 and count < 15):
    
    newbalance = balance  # initialise for another year
#    monthlyPayment +=10   #increment payment
    num = 1               # set month to be 1
    while num <= 12 and newbalance >0:
        newbalance -= monthlyPayment
        interest = newbalance * (annualInterestRate / 12)
        interest = round(interest,2)
        newbalance += interest
        newbalance = round(newbalance,2)
        num += 1
    newbalance = round(newbalance,2)
    print 'end of year ' + 'newbalance ' + str(newbalance)
    if (newbalance >  -0.01 and newbalance < 0.01):

        
        newbalance = 0.0
        break 
    elif newbalance < 0:
        hi = monthlyPayment
    else:
        lo = monthlyPayment
    lo = round(lo,2)
    hi = round(hi,2)
    print 'hi ' + str(hi) + ' lo ' + str(lo)
    monthlyPayment = (hi + lo) / 2.0
    monthlyPayment = round(monthlyPayment,2)
    print 'mp ' + str(monthlyPayment)
#    newbalance = balance
    count += 1
    print 'count ' + str(count)
