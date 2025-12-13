'''
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.

===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.
'''

year = input("Enter a year to determine if it's a leap year or not: ")

if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")

else:
    print("Please enter a positive number for the year.")
