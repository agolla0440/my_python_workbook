"""
in this program iam going to add one string to multiple strings
"""


def add_strings(first, second):
    value = first + " " + second
    return value


name = add_strings("Durga", "Gollapalli")
print("the value of the function is:", name)
second_name = add_strings("Sridevi", "Gollapalli")
print("the value of the function is:", second_name)
