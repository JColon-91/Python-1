'''
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.

=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
'''

try:

    math_score = float(input("Please enter you score for math: "))
    science_score = float(input("Please enter you score for science: "))
    reading_score = float(input("Please enter you score for reading: "))

    average = (math_score + science_score + reading_score)/3

    if average > 100:
        print("Please use a number from 0 to 100")
    elif average >= 90:
       print(f"Your class average is {average:.2f}, which is a A")
    elif average >= 80:
        print(f"Your class average is {average:.2f}, which is a B")
    elif average >= 70:
        print(f"Your class average is {average:.2f}, which is a C")
    elif average >= 60:
        print(f"Your class average is {average:.2f}, which is a D")
    else:
        print(f"Your class average is {average:.2f}, which is a F")

# Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
except ValueError:
    print("Please use a number from 0 to 100")