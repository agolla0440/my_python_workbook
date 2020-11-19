height = int(input("What is your height in inches?: "))
option = input("What would you like us to convert that into, (feet) or (cm): ")
if option.lower() == "feet":
    conversion = height // 12
    print(f"Your height in feet is, {conversion}")
elif option.lower() == "cm":
    conversion = height * 2.54
    print(f"Your height in centimeters is, {conversion}")
