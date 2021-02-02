
"""
Created on Fri Jan 29 15:24:59 2021

@author: Lawrence Ludwig
"""
#imports
import sys
from time import sleep

def title_screen():
    # Startup stuff
    print('Commands:')
    print('Type H to help')
    print('Type S to start')
    print('Type C for Credits')
    print('exit to end ')
    print('------------------')
    print('')
    sleep(.25)
    title_input = input("Please select from the options above:   ")
    # Checking the input
    
    if (title_input =='H') or (title_input == 'h') or (title_input == 'Help') or (title_input == 'help'):
        help_menu()
    elif (title_input == 'S' or title_input == 's' or title_input == 'Start' or title_input == 'start'):
        start()
    elif (title_input == 'C' or title_input == 'c' or title_input == 'Credits' or title_input == 'Credits'):
        Credits()
    elif (title_input == 'exit' or title_input == 'Exit' or title_input == 'e' or title_input == 'E'):
        sys.exit()
    else:
        restart()

def restart():
    title_screen()

def help_menu(): 
    print('Hello This is the help menu!')
    print('When you start the game it will ask')
    print('for a series of words with a type')
    print('such as noun or verb.')
    print('Type a word in and then hit enter.')
    print('Keep doing this until the game stops asking for')
    print('words.')
    print('Then it will show you your completed madlib')
    print('Enjoy!')
    sleep(.25)
    input('Press enter to continue')
    restart()

def Credits():
    print('Link to code github:') 
    print('https://github.com/Lawrence-Ludwig/Madlibs-Game')
    print('Made by Lawrence Ludwig IV!')
    sleep(.25)
    input('Press enter to continue')
    restart()

def start():
    verb1 = input('Type a verb?   ')
    adj1 = input('Type a adjective?   ')
    verb2 = input('Type a verb?   ')
    PoB1 = input('Type a part of body?   ')
    PoB2 = input('Type a part of body?   ')
    noun1 = input('Type a noun?   ')
    verb3 = input('Type a verb?   ')
    animal1 = input('Type a animal?   ')
    noun2 = input('Type a noun?   ')
    verb4 = input('Type a verb?   ')
    adj2 = input('Type a adjective?   ')
    color1 = input('Type a color?   ')
    input('Are your ready?')
    sleep(2)
    input('It doesnt matter because here it is!')
    print('Most doctors agree that bicycle ' + verb1 +' is a ' + adj1 + ' form of exercise. ' + verb2 + " a bicycle enables you to develob your " + PoB1 +  " mucles as well as increase the rate of your " + PoB2 + " beat. More " + noun1 + " around the world. " + verb3 + " bicycles than drive " + animal1 + ". No mater what kind of " + noun2 + " you " + verb4 + ", always be sure to wear a " + adj2 + " helmet. Make sure to have " + color1 + " reflectors too!" )
    sleep(.25)
    input('Press enter to restart')
    restart()

# Start
title_screen()  
