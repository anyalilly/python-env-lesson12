# Anya prob 3
"""
Understanding:
take any number and tell the user whether it's even or odd
Input: Number
 Output: Whether it's even or odd, true or false
Edge case: zero, irrational numbers, fractions
solution: limit to only integers, and give error message when input isn't an integer
"""
"""
integer input
mod % 2
print
boolean variable
"""
""""
psuedocode:
ask user for integer
check if integer can be divided by two
if true then print true
else print false
"""

integer = int(input('Enter any whole number: '))

if integer < 1:
    print('Error, please enter a whole number.')
else:
 if integer % 2 == 0:
    print('True, is even.')
 else:
    print('False, is not even.')
