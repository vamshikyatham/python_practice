print("Wellcome to the quiz!")
play = input("Do you want to play quiz ? \n ANS=")
if play.lower() != "yes":
    quit()
score = 0
question = input("""1)How many wheels for Bike ?
options:
A:2
B:3
C:4
D:5
ANS:""")
if question.upper() == "A":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
question = input("""2)How many wheels for Car ?
options:
A:2
B:3
C:4
D:5
ANS:""")
if question.upper() == "C":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
question = input("""3)How many wheels for Auto ?
options:
A:2
B:3
C:4
D:5
ANS:""")
if question.upper() == "B":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
question = input("""4)How many wheels for Cycle ?
options:
A:2
B:3
C:4
D:5
ANS:""")
if question.upper() == "A":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
print(f"You got {score} questions correct")
print(f"You got {(score/4)*100}%")
