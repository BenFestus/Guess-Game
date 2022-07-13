import sys

#Function checks if guess made by use is correct
def check_guess(guess, answer):
    global score
    still_guessing = True
    guesses = 0

    #After initial guess, user has two more chances 
    while still_guessing and guesses < 2:
        #If guess is same as answer
        if guess.lower() == answer.lower():
            print('Correct Guess! \n')
            score = score + 1
            still_guessing = False
        #If guess is incorrect
        else:
            print('Incorrect Guess!')
            guess = input('Guess again -- ')
            guesses = guesses + 1
    
    #Displays the correct answer if user has guessed two more times and is still incorrect
    if guesses == 2:
        print('The answer is', answer, '\n')

#Function stores the list of questions
def get_questions():
    print('You have three chances to guess the correct answer. Goodluck👍 \n')

    guess1 = input('What is the name of the largest oceanic mammal? -- ')
    #Compare user's guess with answer using the check guess function
    check_guess(guess1, 'blue whale')

    guess2 = input('How many continents are there on Earth? -- ')
    check_guess(guess2, '7')

    guess3 = input('Which of these is a fish? \n A. Shark \n B. Whale \n C. Cat \n D. Orangutan \n Type A, B, C, D -- ')
    check_guess(guess3, 'A')

    #Display's user's score
    print('Your score is', score)


score = 0

print('\t WELCOME TO GUESS GAME 🤩\n')
print('\t 1. START GAME \n \
\t 2. EXIT \n ')

while True:

    user_response = input('Type 1 to start and 2 to exit -- ')
    if user_response == '1':
        #Calls get questions fuction if user wants to start game
        get_questions()
        
        #Ask if user wants to restart
        restart = input('Do you want to restart? Type y/n -- ')
        print()
        if restart == 'y':
            #Calls get questions function if user chooses to restart
            get_questions()
        else:
            sys.exit()

    else:
        sys.exit()

