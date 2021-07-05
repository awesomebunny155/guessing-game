#-----------------------------------------------------------------------------
# Name:        Virtual Lottery Machine: Guess Your Chances! (guessing_game_program.py)
# Purpose:     This guessing game incorporates a lottery application wherin it
# takes the user's attempts and checks it with the random number set by the computer.
# If the user guesses the number correctly, they will gain double the initial credit.
# If the user incorrectly guesses the number, then they will lose 10 points each time
# until they run out of all their credit. 
# Author:      Harini Karthik
# Created:     12-Feb-2021
# Updated:     15-Feb-2021
#-----------------------------------------------------------------------------


# STEP 1: Import the libraries for guessing game
import random
import PySimpleGUI as sg
sg.theme('Dark Blue 4')

# STEP 2: Use randomint function to automatically choose a number
actualNum = random.randint(0, 20)
defaultCredit = 30

# STEP 3: Set the layout screen of the window
layout = [  [sg.Text("Guess a Number : "), sg.Input(key='_IN')],
            [sg.Text(size=(40,1), key='_OUT') ],
            [sg.Text("Default Credit is $30")],
            [sg.Text(size=(40,1), key='_CREDIT')],
            [sg.Button('Ok'), sg.Button('Quit')] ]

# STEP 4: Create the window that follows the layout from step 3
window = sg.Window('Virtual Lottery Machine: Guess Your Chances!!', layout)

# STEP 5: Set up the display and interaction with the window
while True:
    event, values = window.read() 

# STEP 6: Set up the conditions in which the game will quit (through the button)    
    if event == sg.WINDOW_CLOSED  or event == 'Quit':
        break

# STEP 7: Set up conditional statements to repeat the game until credit runs out
    if (defaultCredit > 9):
        if(int(values['_IN']) == actualNum):
            sMsg = "You won :)"
            sCol = "pink"
            defaultCredit *= 2
            actualNum = random.randint(0, 20)
        elif(int(values['_IN']) > actualNum):
            sMsg = "Too high. Try again :("
            sCol = "pink"
            defaultCredit -= 10
        else:
            sMsg = "Too low. Try again :("
            sCol = "pink"
            defaultCredit -= 10
    else:
        sMsg = "Click quit and play again!"
        sCol = "pink"

# STEP 8: Display the results on the window
    window['_OUT'].update(sMsg, text_color=sCol)
    window['_CREDIT'].update('New Credit: ' + str(defaultCredit), text_color="pink")

# STEP 9: Close the window
window.close()
