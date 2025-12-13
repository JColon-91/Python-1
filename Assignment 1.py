'''

Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.

=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.

'''

###############
# INPUT
################
try:
    # Prompt the user to enter the principal amount
    principal = float(input("Enter the principal amount: "))

    # Ask the user to enter the interest rate
    rate = float (input("Enter the interest rate (in percentage): "))

    # Ask the user for the time period
    time = float (input("Enter the time period (in years):"))

    ############
    #PROCESSING
    ############

    # calculate the simple interest
    simple_interest = (principal + rate * time) / 100

    #########
    #OUTPUT
    #######

    print(f"The calculated simple interest is: {simple_interest}")

    ########
    # Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
    ########

except ValueError:
    print("Error: Non-numeric input entered! Please enter a number!")
