'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.

=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.2
'''
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

# Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
    if length <= 0 or width <= 0:
        print("Error: Number must be positive.")
    else:
        area = length * width
        print(f"The area of the rectangle is: {area}")
except ValueError:
    print("Error: Please enter numeric values only.")


