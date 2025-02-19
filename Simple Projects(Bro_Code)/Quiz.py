questions = (("1.Which of the following is one of the basic approaches for joining tables?"),
             ("2.Which country will host the BRICS Youth Entrepreneurship Meeting in March 2025?"),
             ("3.Which village has been declared Gujarat's first Biodiversity Heritage Site?"),
             ("4.Where was the inaugural Raisina Middle East Conference held in 2025?"))

options = (("A.Subqueries", "B.Union Join", "C.Natural join", "D.All of the above"),
           ("A.India", "B.Brazil", "C.China", "D.South Africa"),
           ("A.Mandvi", "B.Guneri", "C.Bhuj", "D.Anjar"),
           ("A.Abu Dhabi", "B.Riyadh", "C.Doha", "D.Dubai"))

answers = ("B", "A", "C", "B")
guesses = []
score = 0
question_num = 0

for ques in questions:
    print("-----------------------------------------")
    print(ques)
    for opt in options[question_num]:
        print(opt)

    print()
    while True:
        guess = input("Enter the option: ").upper()
        if guess in ["A", "B", "C", "D"]:
            break
        else:
            print("Enter the valid option")

    print()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")

    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is correct")

    question_num += 1
print()
print("-----------")
print("   Result  ")
print("-----------")

print("Anwers: ", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")

print()
res = int(score / len(questions) * 100)
print()
print(f"Your Result: {res}%")

if res <= 25:
    print("Poor!")
elif res <= 50:
    print("Not Bad")
elif res <= 75:
    print("Good")
else:
    print("Excellent")