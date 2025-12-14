'''
Challenge: Use nested loop structures to print the pattern efficiently and neatly.
Allow the user to specify the character used for the pattern.

=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern
and then prints a pattern of asterisks (*) in the form of a right triangle.
'''

#ask the user for the number of rows
rows = int(input("Enter the number of rows for the triangle: "))

#ask the user for the character to use
char = input("Enter the character to use in the pattern: ")

#Outer loop for each row
for row_count in range(1, rows + 1):
    #inner loop to print character in each row
    for char_pattern in range(row_count):
        print(char, end="") #print on the same line
    print() #move to the next line after each row
