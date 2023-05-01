"""
1.Write a list comprehension to find all the numbers 
between 1 and 1000 that are divisible by 7
 but not by 5
"""

lst = [i for i in range(1000) if i % 7 == 0 if i % 5]

print(lst)
