x = "Hello world"
print(type(x))
x = 29
print(type(x))
x = 2.9
print(type(x))
x = True
print(type(x))
x = (20, 40, 60, 80)
print(type(x))
x = [20, 40, 60, 80]
print(x.__len__())
print(len(x))
x = range(9)
for i in x:
    print(i)
x = {"name": "John", "age": 36, "is_male": True}
print(type(x["is_male"]))
print(x)
print(x["age"])
