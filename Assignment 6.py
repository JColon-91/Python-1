'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''

try:
    USD = float(input("Please enter currency in USD ($) to convert to EUR (€): "))
    EUR = USD * .8680

    print(f"${USD:.2f} = €{EUR:.2f}")

except ValueError:
    print("Error: Please enter positive numeric values only.")