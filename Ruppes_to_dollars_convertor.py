selection = input("Please select the currency u would like us to convert,(D) or (R): ")
amount = int(input("Amount: "))
if selection.upper() == "D":
    convertor = 70 * amount
    print(f"Your amount is {convertor} in rupees.")
elif selection.upper() == "R":
    convertor = amount/70.0
    print(f"Your amount is {convertor} in dollars.")
    



