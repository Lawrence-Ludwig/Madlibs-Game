
"""
Created on Fri Jan 29 15:24:59 2021

@author: Lawrence Ludwig
"""
#imports
import sys


def title_screen():
    # Startup stuff
    print('Commands:')
    print('Type H to help')
    print('Type S to start')
    print('Type C for Creddits')
    print('exit to end ')
    print('Get for the gethub of the progect')
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
    if (title_input == 'get' or title_input = 'Get'):
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
    print('')
    print('')
    restart()

def creddits():
    print('creddits working')
    restart()


def get_hub():
    print('raw code working')
    restart()

def start():
    print('start working')
    restart()

title_screen()
    
