import random
"""A number-guessing game."""
# print('hi')

# Put your code here
def guessing_game():
    user_name = input("Howdy, what's your name?")
    random_number=random.randint(1,100)
    print(random_number)
    user_guess=None
    num_guesses = 0
    print(f"{user_name}, I'm thinking of a number between 1 and 100!")
    print("Try to guess my number.")
    while random_number !=user_guess:
        user_guess=int(input('Your guess?'))
        if user_guess>random_number:
            print('Your guess is too high, try again')
            num_guesses += 1
        elif user_guess < random_number:
            print("Your guess is too low, try again.")
            num_guesses +=1
        else: 
            num_guesses +=1
            print(f'congratulations {user_name} number guess: {num_guesses}')
            

guessing_game()