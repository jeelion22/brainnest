"""
2. Write a list comprehension to flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
"""

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

new_lst = [elmnt for lst in nested_list for elmnt in lst]

print(new_lst)
