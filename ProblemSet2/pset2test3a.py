balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
high = (balance * (1 + monthlyInterestRate)**12)/12.0
low = balance/12
fixedPayment2 = (high + low)/2
searching = True

def adequatePayment(balance,monthlyInterestRate,fixedPayment2):
    '''
    balance - the outstanding balance on the credit card
    monthlyInterestRate -  monthly interest rate as a decimal
    '''
    month = 1
    while month <= 12:
        balance -=  fixedPayment2 #Update the outstanding balance by removing the payment,
        balance += monthlyInterestRate*balance #then charging interest on the result.
        month += 1
    return balance

while searching:
    z = adequatePayment(balance,monthlyInterestRate,fixedPayment2)
    if  round(z) < 0:
        high = fixedPayment2
        fixedPayment2 = (high + low)/2
    elif round(z) > 0:
        low = fixedPayment2
        fixedPayment2 = (high + low)/2
    elif round(z) == 0:
        searching = False
        print 'Lowest Payment:',round(fixedPayment2,2)