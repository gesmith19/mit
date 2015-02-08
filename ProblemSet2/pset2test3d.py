'''
To recap the problem: we are searching for the smallest monthly payment such 
that we can pay off the entire balance within a year. What is a reasonable 
lower bound for this payment value? $0 is the obvious anwer, but you can do 
better than that. If there was no interest, the debt can be paid off by monthly 
payments of one-twelfth of the original balance, so we must pay at least this
much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off 
the entire balance at the end of the year. What we ultimately pay must be 
greater than what we would've paid in monthly installments, because the interest 
was compounded on the balance we didn't pay off each month. So a good upper 
bound for the monthly payment would be one-twelfth of the balance, after having 
its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search to find the smallest 
monthly payment to the cent (no more multiples of $10) such that we can pay off 
the debt within a year. 
'''

# Paste your code into this box
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