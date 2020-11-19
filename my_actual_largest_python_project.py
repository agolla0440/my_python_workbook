print("Hello, welcome to the MATH trivia.")
option = input("Are you ready to play (yes/no)?: ")
score = 0
tracker = 10
if option.lower() == "yes":
    statement = "Great choice! Be prepared to be tested based on your prior knowledge of (+,-,*, and /)"
    print(f"{statement}")
    ans_1 = int(input("First question, what is the product of 2 + 2: "))
    if ans_1 == 4:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
    ans_2 = int(input("Second question, What is the product of 4/2: "))
    if ans_2 == 2 or ans_2 == 2/1:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
    ans_3 = int(input("Third question, What is the product of 12 * 18: "))
    if ans_3 == 216:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_4 = int(input("Fourth question, What is the product of 12**2: "))
    if ans_4 == 144:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_5 = int(input("Fifth question, What is the solution for this equation (55 * 4) + 20: "))
    if ans_5 == 240:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_6 = int(input("Sixth Question, What is the product of, 9 - 5 + 2 - 6: "))
    if ans_6 == 0:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_7 = int(input("Seventh Question, When x = 24 what is the product of x * 5: "))
    if ans_7 == 120:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_8 = int(input("What is the solution of this question, (5/5) + (6/2): "))
    if ans_8 == 3:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    ans_9 = int(input("What "))

