"""
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.

===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
"""

def is_palindrome(s: str) -> bool:
    clean = ''.join(c.lower() for c in s if c.isalnum())

    if not clean:
        raise ValueError

    left = 0
    right = len(clean) - 1

    # Loop to compare characters from both ends
    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1

    return True

while True:
    try:
        user_input = input(
            "Enter a string to check for a palindrome (or type 'exit' to end task): "
        )

        if user_input.lower() == "exit":
            print("Task ended!")
            break

        result = is_palindrome(user_input)

        if result:
            print("This is a palindrome.")
        else:
            print("This is not a palindrome.")

    except (TypeError, ValueError) as v:
        print("Error! Please enter a string!", v)
