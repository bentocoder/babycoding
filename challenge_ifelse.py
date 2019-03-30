# Write a small program asking for name and age
# when both values have been entered, check if the person
# is the right person to go on a 18-30 holiday ( they must be above 18 and under 31)
# If they are welcome them to the holiday else print a messagedenying them entry.

name = input('Please state your given name')
age = int(input('Please enter your correct age'))

#checking whether both input values have been provided correctly or not

if 18 < age < 31:
    print('Welcome to the holiday')
else:
    print('We are sorry to be not able to offer admission.')