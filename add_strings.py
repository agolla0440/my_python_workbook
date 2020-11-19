"""
in this program iam going to add multiple strings to one string
"""


def add_strings(first, second):
    value = first + " " + second
    return value 


name = add_strings("Ajay", "Gollapalli")
print("the value of the function is: ", name)
second_name = add_strings("Harika", "Gollapalli")
print("the value of the function is: ", second_name)
