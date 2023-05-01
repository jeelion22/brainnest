"""
3. Write a list comprehension that takes a list 
of strings and returns a new list with only 
the strings that contain at least one vowel, in reverse order. 
"""

lst = ["applE", "xyz", "Orange", "pythOn"]

new_lst = [
    item[::-1] for item in lst if any(vow.upper() in item.upper() for vow in "aeiou")
]

print(new_lst)
