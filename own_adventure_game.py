
name = input("Type your name: \n")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? \n").lower()
if answer == "left":
    answer_2 = input("You come to a river, you can walk around it or swim across. To walk around it, type walk. To swim across it, type swim: \n ").lower()

    if answer_2 == "swim":
        print("You swam across and were eaten by an aligator")
    elif answer_2 == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer_3 = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back)\n").lower()
    if answer_3 == "back":
        print("You go back and get lost. You loose the game")
    elif answer_3 == "cross":
        answer_4 = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) \n").lower()

        if answer_4 == "yes":
            print("You talk to the stranger and he rewards you with lots of gold. You WIN!!")
        elif answer_4 == "no":
            print("You ignore the stranger and they are offended. You lose!")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid answer. You lose!")

print("Thank you", name, "for trying.")