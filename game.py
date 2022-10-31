import random
"""A number-guessing game."""
# print('hi')

# Put your code here
def guessing_game():
    user_name = input("Hello player! What's your name?")
    random_number=random.randint(1,100)
    print(random_number)
    user_guess=None
    num_guesses = 0
    while random_number !=user_guess:
        user_guess=int(input("What number is your guess???"))
        if user_guess>random_number:
            print('Too high')
            num_guesses += 1
        elif user_guess < random_number:
            print("Too low")
            num_guesses +=1
        else: 
            print(f'congratulations {user_name} number guess: {num_guesses}')

guessing_game()