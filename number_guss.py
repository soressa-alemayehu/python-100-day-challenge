from random import randint


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10")


choose = input("choose a difficulty. Type 'easy', 'hard':")
number = randint(1,10)
print(number)

HARD_LEVEL_ATTEMPT = 3
EASY_LEVEL_ATTEMPT = 4
answer = 0
attempts = 0



if choose == 'easy':
    attempts = EASY_LEVEL_ATTEMPT
if choose == 'hard':
    attempts = HARD_LEVEL_ATTEMPT


while answer != number:
    
    print(f"you have {attempts} attempts remaining to guess the number")
    answer = int(input("guess the number: "))

    if answer > number:
        print("to high")
    if answer < number:
        print("too low")
    attempts -= 1
    if attempts == 0:
        print("you do not go it")
        break
if answer == number:
    print(f"you got it the answer is {answer}")