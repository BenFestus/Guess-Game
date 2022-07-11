#Function checks if guess is right
def check_guess(guess, answer):
    global score
    still_guessing = True
    guesses = 0
    while still_guessing and guesses < 3:
        if guess.lower() == answer.lower():
            #Print correct answer if answer is correct
            print('CORRECT ANSWER!')
            #Add 1 to score
            score = score + 1
            guesses = guesses + 1
            still_guessing = False
            break
        else:
            print('INCORRECT')
            guesses = guesses + 1
            guess = input('Try again - ')
        
    if guesses == 3:
        #Print the correct answer when user has guessed three times
        print('The correct answer is', answer)
   

score = 0

print('WELCOME TO GUESS GAME')

#Ask user to guess
guess = input('What is the largest animal? - ')
#Check if guess is correct
check_guess(guess, 'blue whale')

guess = input('What is the fastest land animal? - ')
check_guess(guess, 'Cheetah')

guess = input('Is shark a fish? (True or False) - ')
check_guess(guess, 'true')

print('Your score is', score)