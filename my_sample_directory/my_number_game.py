"""
This is a simple guessing game that was built using python.
"""

print("Hi, their, welcome to the Guessing game choose any number between 2 - 10, you will have three attempts.Good luck!")
secret_number = 3
guess_count = 0
maximum_guess_count = 3
while guess_count < maximum_guess_count:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations, you won!")
        break
else:
    print("Sorry you failed.")



