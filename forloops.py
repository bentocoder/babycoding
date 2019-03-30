
# for i in range(1,20):
#     print("i is now {}".format(i))

# number = "9,223,372,036,854,775,807"
# for i in range(0,len(number)):
#     print(number[i])
#
# number = "9,223,372,036,854,775,807"
# for i in range(0,len(number)):
#     if number[i] in '0123456789':
#         print(number[i],end = '  ')

# for loops in char number / advanced examples
# One of the most important interface in python is iterable. Iterable has three descendants sequence , generator and mapping.
# A sequence is a iterable with random access.You can ask for any items of the sequence without having to consume the items before it. With this property you can build slices.
# If access is done via keys rather than integer positions then you have a MAPPING. dict is basic mapping.

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The Number is {0}".format(newNumber))
