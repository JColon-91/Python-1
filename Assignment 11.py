'''
Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters
a non-numeric input.

=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user.
The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.
'''

print("Please enter a positive integer! ")
user_input = input("Enter a number: ")

# Validate the input and make sure to repeat until the user enters a number

while not user_input.isdigit() or int(user_input) <= 0:
    print("Invalid input. Please enter a positive number! ")
    user_input = input("Enter the number here: ")

#convert the input to a number
number = int(user_input)

print("Collatz Sequence: ", number)

# generate a loop that will run until it becomes 1
while number != 1:
    print (number, end = " -> ")
    if number % 2 == 0: # if the number is even then divide it by 2
        number = number // 2
    else:
        # if the number is odd then do the following below:
        number = number * 3 + 1

    print (number)
