'''
Problem Set 2 question 1

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

Finally, print out the total amount paid that year and the remaining balance at 
the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate 
x Monthly unpaid balance)

'''
# test case 1
# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

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