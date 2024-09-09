import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("[Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please type a number greater than 0 next time")
            quit()
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess < random_number:
        print("You got it wrong. You were below the number!")
    else:
        print("You got it wrong. You were above the number!")


print(f"You did " + str(guesses) + " guesses today!")
print("You did", guesses,"guesses today!")