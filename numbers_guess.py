import random


top_of_range = input("Type a number please to determine the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger then 0 next time ")
        quit()
else:
    print('Please type a number next time')
    quit()



random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print('You got it !!\n')
        break
    elif user_guess > random_number:
         print("You were above the number\n")
    else:
        print("You were below number\n")
print(f"You got it in {guesses} guesses")

