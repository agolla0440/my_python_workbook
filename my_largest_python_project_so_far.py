print("Hi welcome to Ajay's 2020 trivia quiz.")
option = input("Are you ready to play, (yes/no): ")
score = 0
tracker = 5
if option.lower() == "yes":
    statement = "Oh, Great!, hope you do well"
    print(f"{statement}")
    ans_1 = input("First Question, What is Ajay's favorite color?: ")
    if ans_1.lower() == "red":
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
    ans_2 = input("Second Question, What is Ajay's dream job?: ")
    if ans_2.lower() == "software engineer":
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
    ans_3 = input("Third Question, Which state does Ajay want to live in when he grows up?: ")
    if ans_3.lower() == "california":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_4 = input("Fourth Question, Which country was Ajay born in?: ")
    if ans_4.lower() == "india":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_5 = input("Fifth Question, What is Ajay's favorite food?: ")
    if ans_5.lower() == "chicken wings" or ans_5.lower() == "chicken biryani":
        score += 1
        print("Correct")
    else:
        print("Incorrect")
    print('Thank you for playing you got', score, "questions correct. ")
    player = (score/tracker) * 100
    print("score", str(player) + "%")
    print("Thank you for playing, Goodbye!")
print("Hello World ")
