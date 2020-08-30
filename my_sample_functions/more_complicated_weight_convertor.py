weight = int(input("Weight: "))
unit = input("(L)b: or (K)g; ")
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"Your weight is {convert} in kilograms")
elif unit.upper() == "K":
    convert = weight / 0.45
    print("Your weight is ", convert, "in pounds")
    print(f"Your weight is {convert} in pounds")
i = 2
while i <= 5:
    print(i)
    i = i + 1
    print("done")


