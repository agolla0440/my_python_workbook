weight = int(input("Weight: "))
unit = input("(L)b: or (K)g: ")
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"Your weight is {convert} in kilograms")
elif unit.upper() == "K":
    convert = weight // 0.45
    print(f"Your weight is {convert} in pounds")
