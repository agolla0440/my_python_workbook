import random

friends = ["Mike", "Jhon", "Alex", "Mitch"]
selector = random.choice(friends)
if selector == "Mitch":
    print(selector)
    print("He won't be receiving a prize today, because he is absent.")

else:
    print("The lucky winner is...")
    print(selector)
