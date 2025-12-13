'''
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''

try:
    #  Input section below

    x1 = float(input("Enter x1 coordinates: "))
    y1 = float(input("Enter y1 coordinates: "))
    x2 = float(input("Enter x2 coordinates: "))
    y2 = float(input("Enter y2 coordinates: "))

    # Processing listed below
    dx_squared = (x2 - x1) ** 2
    dy_squared = (y2 - y1) ** 2
    distance_squared = dx_squared + dy_squared
    distance = distance_squared ** 0.5

    # This is the output below
    print (f"The distance between 2 points is: {distance}")

    # Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
except ValueError:
    print("Error: Please enter numeric values only.")
