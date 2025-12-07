import random

print("!---THE PERFECT GUESS GAME---!")
print("Computer: I have chosen the number and you have to guess that number Between (1-100) OK...")

comp = random.randint(1, 100)
a = -1
guesses = 1
while (a != comp):
    a = int(input("Guess the Number: "))
    if(a > comp):
        print("Not Correct ... Lower Number Please!")
        guesses += 1
    elif (a < comp):
        print("Not Correct ... Higher Number Please!")
        guesses += 1

print(f"Computer: CONGRATULATIONS 👏\n\tYou have correctly guess the Number {comp} in {guesses} Attempts")
