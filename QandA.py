print("welcome to my game")
playing = input("do you want to play? y or n : ")

if playing.lower() != "y":
    quit()
print("Okay lets play : :)\n")
score =0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect")
print(f"You got {score} questions correct or {(score/4)*100} %")
