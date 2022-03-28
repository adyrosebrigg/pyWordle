import PySimpleGUI as sg
import random
import time
from datetime import date, timedelta

with open('words') as file:
    words = file.read().splitlines()

with open('guesses') as file:
    guesses = file.read().splitlines()

yesterday = str(date.today() - timedelta(days=1))
today = str(date.today())

random.seed(yesterday)
yword = random.choice(words).upper()

random.seed(today)
word = random.choice(words)

attemptnum = 1
prevguesses = []

# Define the layout

# A column where game input will take place:
gamecol = sg.Column([
    
    # Guess 1 buttons
    [sg.Button(k='word1_1', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word1_2', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word1_3', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word1_4', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word1_5', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white')
    ],
    
    # Guess 2 buttons
    [sg.Button(k='word2_1', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word2_2', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word2_3', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word2_4', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word2_5', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white')
    ],
    
    # Guess 3 buttons
    [sg.Button(k='word3_1', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word3_2', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word3_3', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word3_4', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word3_5', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white')
    ],
    
    # Guess 4 buttons
    [sg.Button(k='word4_1', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word4_2', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word4_3', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word4_4', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word4_5', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white')
    ],
    
    # Guess 5 buttons
    [sg.Button(k='word5_1', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word5_2', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word5_3', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word5_4', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white'),
     sg.Button(k='word5_5', s=(3,1), font=('Cascadia Mono', 29), disabled=True, disabled_button_color='white')
    ],
    
    # The input element, hidden but silently referenced and kept in focus.
    [sg.Input(k='attempt', s=19, p=7, font=('Cascadia Mono', 28), change_submits=True, enable_events=True, focus=True)],
        
    # This is an invisible dummy button that is bound to return, so pressing return always submits.
    [sg.Button('guess', visible=False, bind_return_key=True)]
    
    # Set additional params for gamecol
    ], p=0, s=(440, 480), background_color='black'
    )

# A column where help, log messages, and other data will be shown:
helpcol = sg.Column([
    
    # Header text with welcome message
    [sg.Text('Welcome to pyWordle!', font=('Cascadia Mono', 21), background_color='black', p=(0, 12))],
    
    
    # Message log view
    [sg.Multiline(p=(11, 22), s=(37, 7), no_scrollbar=True, disabled=True, k='log', autoscroll=True )],
    
    # Keyboard display to show already guessed letters.
    # Columns used here as spacers between rows.
    [sg.Frame(" Guessed Letters: ", [
        
        [sg.Column([[]], background_color='black', s=(250, 10))],
        
        [sg.Button('q'), sg.Button('w'), sg.Button('e'), sg.Button('r'), sg.Button('t'),
             sg.Button('y'), sg.Button('u'), sg.Button('i'), sg.Button('o'), sg.Button('p')],
        
        [sg.Column([[]], background_color='black', s=(250, 10))],
        
        [sg.Button('a'), sg.Button('s'), sg.Button('d'), sg.Button('f'),
             sg.Button('g'), sg.Button('h'), sg.Button('j'), sg.Button('k'), sg.Button('l')],

        [sg.Column([[]], background_color='black', s=(250, 10))],

        
        [sg.Button('z'), sg.Button('x'), sg.Button('c'), sg.Button('v'),
             sg.Button('b'), sg.Button('n'), sg.Button('m'), sg.Column([[]], background_color='black')]
        
        # Set additional params for keyboard frame
        ], s=(300, 200), p=10, font=('Cascadia Mono', 14), background_color='black', element_justification = "center",
        )]
    
    # Set additional params for helpcol
    ], p=0, s=(330, 450), background_color='black'
    )

# Define the final layout, combining the above columns
layout = [[sg.Column([[gamecol, helpcol]], background_color='black')]]

# Create the Window
window = sg.Window('pyWordle', layout, size=(800, 485), background_color='black', button_color='grey',
                   font=('Cascadia Mono', 10), finalize=True)

# A function to log messages to the user window
def log_message(message):
    window['log'].update(' - '+message+'\n', append=True)
    
log_message('Yesterday\'s word: {}'.format(yword))

# A function to update the keyboard keys as needed
def update_keyboard(guess):
    for letter in guess:
        window[letter].update(disabled=True, button_color='black')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user clicks exit
        break
    
    if 'attempt' in event:
        t = "".join(values[event].upper().split())[:5].ljust(5)
        
        for position in range(5):
            if attemptnum < 6:
                window['word{}_{}'.format(attemptnum, position + 1)].update(t[position].upper())
    
    if 'guess' in event:
        # Once the game's been finished, bypass this if
        if attemptnum > 5:
            continue
        
        # Get the guess from the input box
        guess = "".join(values['attempt'].lower()[:5].split())
        
        # Clear the input box for future use
        window['attempt'].update('')
        
        # Validate the input
        valid = False
        
        if len(guess) != 5:
            log_message('Guess exactly 5 letters, please.')
            
        elif guess[0] not in 'abcdefghijklmnopqrstuvwxyz':
            log_message('Guess only letters, please.')
            
        elif guess[1] not in 'abcdefghijklmnopqrstuvwxyz':
            log_message('Guess only letters, please.')
            
        elif guess[2] not in 'abcdefghijklmnopqrstuvwxyz':
            log_message('Guess only letters, please.')
            
        elif guess[3] not in 'abcdefghijklmnopqrstuvwxyz':
            log_message('Guess only letters, please.')
            
        elif guess[4] not in 'abcdefghijklmnopqrstuvwxyz':
            log_message('Guess only letters, please.')
            
        elif guess not in words and guess not in guesses:
            log_message('Not a dictionary word, try again.')
            
        elif guess in prevguesses:
            log_message('You already guessed that word, try another.')
        
        else:
            # Word is valid
            valid = True
        
        # If we made a bad guess, clear the current row for retry
        if not valid:
            for position in range(5):
                window['word{}_{}'.format(attemptnum, position + 1)].update('')
            continue
        
        # If we made a GOOD guess, assign colors to boxes
        for char in range(5):
            if guess[char] == word[char]:
                window['word{}_{}'.format(attemptnum, char + 1)].update(button_color='green')
                time.sleep(0.3)
            elif guess[char] in word:
                window['word{}_{}'.format(attemptnum, char + 1)].update(button_color='darkgoldenrod')
                time.sleep(0.3)
            window.finalize()
        
        # Update the keyboard display in the left pane to show guessed letters
        update_keyboard(guess)
        
        # Log a successful guess to list prevguesses
        prevguesses = prevguesses + [guess]
        
        if guess == word:
            log_message('You won today\'s game in {}! Congrats.'.format(attemptnum))
        
        # Add 1 to the attempt counter
        attemptnum = attemptnum + 1
        
        if attemptnum > 5:
            log_message('Sorry, no win today. Try again tomorrow!')
        
        
        
       
window.close()