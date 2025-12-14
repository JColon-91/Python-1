'''
Challenge: Optimize the function to handle large input lists efficiently.
Bonus: if you add the exceptions in on your own, you will get 50 extra pts
==============================
Description: Develop a function called find_common_elements that takes two lists
as input and returns a new list containing elements that are common to both input lists.
'''


def find_common_elements(list1, list2):
    return list(set(list1) & set(list2)) #common elements between both list, use these # and create a new list

Jessica = [1, 2, 3, 4, 5, 6, 7, 15]
Generated = [10, 0, 20, 50]


try:
    result = find_common_elements(Jessica, Generated)

    if not result:
        raise ValueError()

except ValueError: #bonus - purposely removed all common input elements for this to run
    print("No common elements found.")

else:
    print("Common elements between both lists:", result)

finally:
    print()





