import random

number = random.randint(1,10)
print(number)

correct = False

while not correct:
    userGuess=input("What is your guess? ")
    if(userGuess == number):
        ("Correct!")
        elif(userGuess < number):
            print("Too low!")

