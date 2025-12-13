'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
'''

# The input section solution is below
weight_input = input("Enter your weight in kilos: ")
height_input = input("Enter your height in meters: ")

# Conversion to float is calculated below
weight = float(weight_input)
height = float(height_input)

#  Calculate the BMI | Processing below
bmi = weight / (height ** 2)

# Output below
print(f"The BMI is: {bmi}")

#Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
if bmi < 18.5:
    print("Your BMI is underweight")
elif bmi < 25:
    print("Your BMI is normal")
elif bmi < 30:
    print("Your BMI is overweight")
else:
    print("Your BMI is obese")