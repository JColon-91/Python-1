'''
Challenge: Write the function using recursion.

===================================
Description: Create a function named is_palindrome that takes a string as input
and returns True if it is a palindrome, and False otherwise.
'''

def is_palindrome (s: str) -> bool:
    clean = ''.join(c.lower() for c in s if c.isalnum()) # isalnum = function will ignore punctuation/spaces/case sensitivity
    return clean == clean[::-1] # :: comparing w/ reverse input

print(is_palindrome("racecar"))