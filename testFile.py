print("Hello World! ")

name = input('Please enter your name?')
age: str = int(input('Enter your age'))

print('Your name is {0} , age is {1} years'.format(name, age))

if not(age < 18):
    print("Your age is {0} years. You are eligible".format(age))
    print("For casting ballot, Put an X in the box")
else:
    print("Please come back in {0} years for casting vote".format(18 - age))

# elements = [ 10 ,20 , 0 , 45 , 60]
# x = bytearray(elements)
#
# for i in x: print(i)
#
# x[0] = 98
# x[1] = 99
#
# for i in x: print(i)
