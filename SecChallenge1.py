# Create a program that takes an ip address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address contains of numbers, separated from each other with a full stop.
# But the program should count how many ever are entered
# Examples of the input you may get are:
#
#     127.0.0.1
#     .192.168.0.1
#     10.0.123456.255
#     172.16
#     255
#
# So your program should work with invalid IP addresses.
# We're just interested in the number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test.
#     .123.45.678.91
#     123.4567.8.9
#     123.156.289.10123456
#     10.10t.10.10
#     12.9.34.6.12.90
#     '' - Press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements , so although
# you could use other techniques(such as splitting the string up), thats not the approach we are looking for.

ipAddress = input("Please enter an ip address: \n")

segment = 1
segment_length = 0
char = ''

for char in ipAddress:
    if char == '.':
        print("Segment {} contains {} characters.".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . then we haven't printed the final segment.
if char != '.':
    print("Segment {} contains {} characters.".format(segment, segment_length))


