cont = True

# Convert hours to float
while cont:
    hrs = input('Enter Hours:')
    try:
        hours = float(hrs)
        cont = False
    except:
        print('Error: Please eater a numeric input')

# Convert Rate to float
cont = True
while cont:
    rate = input('Enter Rate:')
    try:
        rate = float(rate)
        cont = False
    except:
        print('Error: Please eater a numeric input')

print(hours)
if hours <= 40:
    # Normal rating for hours <= 40
    pay = hours*rate
else:
    # Give the employee 1.5 times the hourly rate for hours worked above 40 hours
    pay = 40*rate + (hours-40)*1.5*10
print('Pay:', pay)
