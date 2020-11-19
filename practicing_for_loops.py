fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("List item: ", x)
    print(f"Item length: {len(x)}")
print("The last fruit before appending:", fruits[-1])
fruits.append("orange")
print("We are getting the index for the banana in the list", fruits.index("banana"))
print("The second fruit is:", fruits[1])
print("The first fruit is:", fruits[0])
print("The last fruit is:", fruits[-1])
