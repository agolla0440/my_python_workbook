# This is the part where I contain the strings in a variable in a list format.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


vegetables = ["broccoli", "tomato", "cabbage", "carrot", "lettuce", "celery", "potato",
              "spinach", "ginger", "onion"]
# This is the part where I print my vegetables(strings) from the sixth vegetable to the second vegetable
# based of the requirement
print(len(vegetables))
# print("My vegetables list from the sixth vegetable to the second vegetable.:",
#       vegetables[6], ",", vegetables[5], ",", vegetables[4], ",", vegetables[3], ",", vegetables[2])
# This is the part where I break at the 4th vegetable because in the constraint it asked me to slice the
# list, and print the following items in the original order.
for x in vegetables:
    print(f"This is the vegetables list: {x}")

# list, and print the following items in the original order.
print("\n")
# vegetables.reverse()
for x in vegetables:
    print(f"This is the reverse order of the list: {x}")
list_of_vegetable_list = list(divide_chunks(vegetables, 3))
print(len(list_of_vegetable_list))
for smaller_veg_list in list_of_vegetable_list:
    print("I'm in the smaller_veg_list")
    for veggie in smaller_veg_list:
        print("vegetable:", veggie)
