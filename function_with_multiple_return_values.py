"""
in this program iam going to add multiple strings to one string and then return two values from a function
"""


def add_strings(first, second):
    value = first + " " + second
    return value, first


func_output, first_name = add_strings("Ajay", "Harika")
print(func_output)
print(first_name)
