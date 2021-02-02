
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
    print('Type C for Creddits')
    print('exit to end ')
    print('Get for the gethub of the progect')
    sleep(.25)
    title_input = input(">>>")
    # Checking the input
    
    if (title_input =='H') or (title_input == 'h') or (title_input == 'Help') or (title_input == 'help'):
        help_menu()
    if (title_input == 'S' or title_input == 's' or title_input == 'Start' or title_input == 'start'):
        start()
    if (title_input == 'C' or title_input == 'c' or title_input == 'Creddits' or title_input == 'creddits'):
        creddits()
    if (title_input == 'exit' or title_input == 'Exit' or title_input == 'e' or title_input == 'E'):
        sys.exit()
    if (title_input == 'get' or title_input == 'Get'):
        get_hub()
    restart()
    



def restart():
    title_screen()

def help_menu(): 
    print('Hello This is the help menu!')
    print('When you start the game it will ask')
    print('For a series of words with a type')
    print('Such as nown or verb.')
    print('Type a word in and then hit enter.')
    print('Keep doing this intill the game stops asking for')
    print('Words.')
    print('Then it will show you your completed madlib')
    print('Enjoy!')
    input()
    restart()

def creddits():
    print('Link to code gethub:') 
    print('https://github.com/Lawrence-Ludwig/Madlibs-Game')
    restart()


def get_hub():
    print('https://github.com/Lawrence-Ludwig/Madlibs-Game/tree/Lawrence-Ludwig-patch-IDLE-fix')
    restart()

def start():
    print('Type a verb')
    sleep(.25)
    verb1 = input('>>>')
    print('Type a adjective')
    sleep(.25)
    adj1 = input('>>>')
    print('Type a verb')
    sleep(.25)
    verb2 = input('>>>')
    print('Type a part of body')
    sleep(.25)
    PoB1 = input('>>>')
    print('Type a part of body')
    sleep(.25)
    PoB2 = input('>>>')
    print('Type a noun')
    sleep(.25)
    noun1 = input('>>>')
    print('Type a verb')
    sleep(.25)
    verb3 = input('>>>')
    print('Type a animal')
    sleep(.25)
    animal1 = input('>>>')
    print('Type a noun')
    sleep(.25)
    noun2 = input('>>>')
    print('Type a verb')
    sleep(.25)
    verb4 = input('>>>')
    print('Type a adjective')
    sleep(.25)
    adj2 = input('>>>')
    print('Type a color')
    sleep(.25)
    color1 = input('>>>')
    input('Are your reddy')
    input('It doesnt mater because here it is')
    print('Most doctors agree that bicycle ' + verb1 +' is a ' + adj1 + ' form of exercise. ' + verb2 + " a bicycle enables you to develob your " + PoB1 +  " mucles as well as increase the rate of your " + PoB2 + " beat. More " + noun1 + " around the world. " + verb3 + " bicycles than drive " + animal1 + ". No mater what kind of " + noun2 + " you " + verb4 + ", always be sure to wear a " + adj2 + " helmet. Make sure to have " + color1 + " reflectors too!" )
    restart()

title_screen()
    
