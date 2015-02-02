'''
Now write a program that calculates the minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each 
month, but instead is a constant amount that will be paid each month.
'''
num = 1
newbalance = balance
monthlyPayment = 0

while newbalance > 0:
    newbalance = balance  # initialise for another year
    monthlyPayment +=10   #increment payment
    num = 1               # set month to be 1
    while num <= 12 and newbalance >0:
        newbalance -= monthlyPayment
        interest = newbalance * (annualInterestRate / 12)
        newbalance += interest
        num += 1
#    print 'end of year ' + 'newbalance ' + str(newbalance) + 'payment ' + str (monthlyPayment)
#    print 'num ' + str(num)
print 'Lowest Payment: ' + str(monthlyPayment)