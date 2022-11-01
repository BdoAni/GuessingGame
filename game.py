import random
"""A number-guessing game."""
# print('hi')
# Put your code here
def guessing_game():
    user_name = input("Howdy, what's your name? ")
    while len(user_name) < 2:
        user_name=input(f"{user_name} is not a valid name. ")
    random_number=random.randint(1,100)
    print(random_number)
    user_guess=None
    num_guesses = 0
    print(f"{user_name}, I'm thinking of a number between 1 and 100!")
    print("Try to guess my number.")
    while random_number != user_guess:
        user_guess=int(input('Your guess? '))
        while user_guess < 1 or user_guess > 100:
            num_guesses += 1
            user_guess = int(input("That is a bad guess! Guess a number between 1 and 100!   "))
        if user_guess>random_number:
            print('Your guess is too high, try again')
            num_guesses += 1
        elif user_guess < random_number:
            print("Your guess is too low, try again.")
            num_guesses +=1
        else: 
            num_guesses +=1
            print(f'Well done, {user_name}! You found my number in {num_guesses} tries!')
            return num_guesses
            

continue_play = True
best_score=999999
while continue_play:
    new_score = guessing_game()
    if new_score < best_score :
        best_score = new_score
        print(f'Your best score so far is {best_score}' )
    user_cont=(input(f'Do you want to play more? Y / N')).upper() 
    if user_cont == 'N':
            print(f'game over! Your best score is {best_score}!!!')
            continue_play=False        

