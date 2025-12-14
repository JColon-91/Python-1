"""
Challenge: Ensure that the function works correctly with tuples of different lengths.
Bonus: if you add the exceptions in on your own, you will get 50 extra pts

=============================================
Description: Create a function called concat_tuples that takes two tuples as input and returns a
new tuple containing all elements from both input tuples.
"""

def concat_tuples(tuple1,tuple2):
    return tuple1 + tuple2

t1 = (1,2,3)
t2 = (4,5,6,7)

try:
    results = concat_tuples(t1,t2)

    if not results:
        raise ValueError()

except ValueError:
    print("No data to concatenate!")

else:
    print("Concatenated list:", results)

finally:
    print()
