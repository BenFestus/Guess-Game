def check_guess(guess, answer):
    global score
    still_guessing = True
    guesses = 0
    while still_guessing and guesses < 3:
        if guess.lower() == answer.lower():
            print('CORRECT ANSWER!')
            score = score + 1
            guesses = guesses + 1
            still_guessing = False
            break
        else:
            print('INCORRECT')
            guesses = guesses + 1
            guess = input('Try again - ')
        
    if guesses == 3:
        print('The correct answer is', answer)
        
            

score = 0

print('WELCOME TO GUESS GAME')

guess = input('What is the largest animal? - ')
check_guess(guess, 'blue whale')

print('Your score is', score)