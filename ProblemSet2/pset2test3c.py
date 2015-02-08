# test case 1
#balance = 3329
#annualInterestRate = 0.2

#test case 2
#balance = 4773
#annualInterestRate = 0.2

#balance = 320000 
#annualInterestRate = 0.2
#Lowest Payment: 29157.09

balance = 999999
annualInterestRate = 0.18
#Lowest Payment: 90325.03

#balance = 1000
#annualInterestRate = 0.2



monthlyInterestRate = (annualInterestRate)/12.0
lo = balance/12
hi = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
newbalance = balance


monthlyPayment = (hi + lo) / 2.0


count = 0

gap = hi - lo

while (newbalance !=0 and gap > 0.01):
    
    newbalance = balance  # initialise for another year
    num = 1               # set month to be 1
    while num <= 12:
        newbalance -= monthlyPayment
        interest = newbalance * (annualInterestRate / 12)
        newbalance += interest
        num += 1

    if newbalance == 0.0:
        break
       
    if newbalance < 0:
        hi = monthlyPayment
    else:
        lo = monthlyPayment
        
    monthlyPayment = (hi + lo) / 2.0
    gap = hi - lo

    newbalance = balance
    count += 1


print 'Lowest Payment: ' + str(round(monthlyPayment,2))