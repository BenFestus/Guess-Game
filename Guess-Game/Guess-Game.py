#Function that checks if guess is correct
def check_guess(guess, answer):
    global score
    still_guessing = True
    guesses = 0

    #As long as user is still guessing and guesses is less than 2
    while still_guessing and guesses < 2:
        if guess.lower() == answer.lower():
            #Print correct answer when guess is correct
            print('Correct answer')
            #Add 1 to score
            score = score + 1
            #Since user is correct, still_guessing is False
            still_guessing = False
            break
        else:
            #Print incorrect when guess is incorrect
            print('Incorrect guess')
            guess = input('Try Again! - ')
            #Add 1 to the number of guesses 
            guesses = guesses +  1

    if guesses == 2:
        #Print the correct answer when user has guessed two more times and is wrong
        print('The correct answer is', answer)

    

score = 0

print('Welcome to Guess Game')

guess = input('What is the capital of Nigeria? - ')
check_guess(guess, 'Abuja')
print()

guess = input('What is the largest ocean mammal? - ')
check_guess(guess, 'blue whale')
print()

guess = input('How many continents are there presently? - ')
check_guess(guess, '7')
print()

guess = input('What is the slowest land animal? - ')
check_guess(guess, 'snail')
print()

guess = input('How many moons does Earth have? - ')
check_guess(guess, '1')
print()

guess = input('What is the fastest land animal? - ')
check_guess(guess, 'cheetah')
print()

print('Your score is', score)