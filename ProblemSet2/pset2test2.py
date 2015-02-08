'''
Write a program to calculate the credit card balance after one year if a person 
only pays the minimum monthly payment required by the credit card company each 
month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining 
balance, and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy

Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
'''

# test case 1
#balance = 3329
#annualInterestRate = 0.2

# test case 2
balance = 4773
annualInterestRate = 0.2


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
   