'''
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''

try:
    hours = float(input("Please enter the time duration in hours to convert to minutes and seconds: "))

    minutes = hours * 60
    seconds = hours * (60 ** 2)

    if hours > 0:
        print(f"Time duration converted to minutes: {minutes} minutes")
        print(f"Time duration converted to seconds: {seconds} seconds")
    else:
        print("Error: Please enter positive numeric values only.")

except ValueError:
    print("Error: Please enter positive numeric values only.")