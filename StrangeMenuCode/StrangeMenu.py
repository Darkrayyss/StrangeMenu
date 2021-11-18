import time
from Functions import *
from DiegoSapp import DiegoSapp
from SimpleInterface import SimpleInterface
# Para diegoSapp: [A] contiene users, [B] contiene passwords

#################### Main functions ####################

def DisplayCredits():
    console_print("I plan to do a graphic interface like the credits in 'interactive USM', Diego know what I mean")
    return

def action(number):
    if number == 0:
        return
    if number == 1:
        console_print("Hello motherfucker!")
        console_print("Are you happy now ?")
        return
    if number == 2:
        DiegoSapp()
        return
    if number == 3:
        SimpleInterface()
    if number == 4:
        console_print("This option is not available yet")
    if number == 5:
        console_print("This is not an EASTER EGG, don't trie write '1234'")
    if number == 6:
        console_print("This option is not available yet")
    if number == 7:
        console_print("This option is not available yet")
    if number == 8:
        DisplayCredits()
    return

def menu():
    print("\nWelcome to the menu !\n")
    print("1) Say 'hello.'")
    print("2) Join to DiegoSapp.")
    print("3) Open a rare interface.")
    print("4) Nothing for now.")
    print("5) Nothing for now.")
    print("6) Nothing for now.")
    print("7) Open USM interactive ?..")
    print("8) Credits.")
    print("9) Exit.")
    return


#################### Main ####################
if __name__ == '__main__':
    console_print("Welcome to the 'first' Diego's program in Python")
    key = 0
    while (0 <= key < 9):
        action(key) # Apply the action. key = 0 => Nothing
        menu() # Deploy menu
        key = getkey() # Select the option   
    console_print("Nice to see you !") # Goodbye
    time.sleep(2)     