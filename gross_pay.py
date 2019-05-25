hrs = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))

if hrs <= 40:
    # Normal rating for hours <= 40
    pay = hrs*rate
else:
    # Give the employee 1.5 times the hourly rate for hours worked above 40 hours
    pay = 40*rate + (hrs-40)*1.5*10

print('Pay:', pay)
