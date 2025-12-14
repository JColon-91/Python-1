'''
Challenge: Implement the sorting algorithm without using any built-in sorting functions.
Bonus: if you add the exceptions in on your own, you will get 50 extra pts
====================================
Description: Develop a function called sort_list that takes a list of numbers as input
and returns a new list containing the same elements sorted in ascending order.
'''

def sort_list(list1, list2):
    return list1 + list2


L1 = (2, 4, 6, 8)
L2 = (1, 3, 5, 7, 9)

try:
    results = sort_list(L1, L2)

    if not results:
        raise ValueError()

    ascending = sorted(results)
    print("Concatenated list (ascending):", ascending)

except ValueError:
    print("No data!")
