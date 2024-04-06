name = input("Type your name: ")
print(f"Welcone {name}, to this adventure!")

answer =input("You are on a dirt road , it has come to an end and you can go left or right. Which way you wanna go? :").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across, type swim or walk??").lower()
    if answer == "swim":
        print("You swam across and got eaten by a monster")
    elif answer == "walk":
        print("You walked for many miles and ran out of water, enjoy hell")
    else:
        print("Not a valid option,You lost !!")

elif answer == "right":
    answer=input("You come to a bridge,it looks wobbly , do you want to cross or go back?: ")
    if answer == "back":
        print("You go back and got eaten by a crow")
    elif answer == "cross":
        answer=input("You cross the bridge and you meet a strange.Do you talk to them? yes or no ? ")
        if answer == "yes":
            print("You talked to the strange and he tells you to stop playing this stupid game and you won coz its over, you just wasted your time LOL GG ")
        elif answer == " no":
            print("Bad call ,stranger murdered you and all the worst ,whatever yawn you dead ,you lost bye")
        else:
            print("Not a valid option,You lost !!")
    else:
        print("Not a valid option,You lost !!")

else:
    print("Not a valid option, You lost")

print(f"Thank you for playing {name}")
