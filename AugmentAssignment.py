
number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]
# The only binary operation we can do with strings is addition and repetition. That is + and * respectively.

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

