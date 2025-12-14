"""
Challenge: Optimize the function to handle large input numbers efficiently.

=====================================================
Description: Develop a function called is_prime that takes a positive integer as input
and returns True if it is a prime number, and False otherwise.
"""

def is_prime(n: int) -> bool:

    if n < 2:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    e = 5
    while e * e <= n:
        if n % e == 0 or n % (e + 2) == 0:
            return False
        e += 6

    return True

print("3 =",is_prime(3))
print("100 =",is_prime(100))

