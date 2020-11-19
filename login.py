option = input("(C)reate: or (L)ogin: ")
if option.upper() == "C":
    email = input("Email: ")
    print(f"This is your email, {email}")
    print("Email verified")
    username = input("Username: ")
    if (len(username)) < 5:
        print("The username must be at least 5 characters long, try again later.")
    else:
        print(f"This is your username, {username}")
    password = input("Password: ")
    if (len(password)) < 5:
        print("The password must be at least 5 characters long, try again later")
    else:
        print(f"This is your password, {password}")
        print("You have successfully made your account!")
elif option.upper() == "L":
    the_username = input("Username: ")
    the_password = input("Password: ")
    if (len(the_username)) < 5:
        print("The username seems to be incorrect")
    if (len(the_password)) < 5:
        print("The password seems to be incorrect, ")
        print("The login was unsuccessful")
    else:
        print("Login successful, welcome to your database")
