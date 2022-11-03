# Regular Imports
from os import system
import os
import sys

import sprites

# Pip Imports
try:
    from consolemenu import *
    from consolemenu.items import *
except:
    print("Could not find Console Menu. Would you like to install it through pip?")
    yesno = input("(Y/n) ").lower().strip()
    if yesno == 'y' or yesno == '':
        print()
        print("Make sure pip is in PATH.")
        print()
        system('pip install console-menu')
        print()
        print("If install was successful, relaunch the game.")
        exit(0)
    elif yesno == 'n':
        exit(0)

# Game Imports
import player
import enemy
import battlemaker

# For shorter Menu Items
tr = True


# From Stack Overflow because I'm not perfect at Python.
def wait_key():
    """ Wait for a key press on the console and return it. """
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getwch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


def titlescreen():
    clear_terminal()
    print(r"""


    ___  __                                   ____          ____   
   F _ ",LJ   _____    _____     ___ _       / _  `.       F _  ]  
  J `-' |    [__   F  [__   F   F __` L     J_/-7 .'      J |/ | L 
  |  __/FFJ  `-.'.'/  `-.'.'/  | |--| |     `-:'.'.'      | | /| | 
  F |__/J  L .' (_(_  .' (_(_  F L__J J     .' ;_J__  __  F  /_J J 
 J__|   J__LJ_______LJ_______LJ\____,__L   J________LJ__LJ\______/F
 |__L   |__||_______||_______| J____,__F   |________||__| J______F 
                                                                   


    """)
    print()
    print("Press any key to start.")
    wait_key()
    mainmenu()


def mainmenu():
    if battlemaker.exitbattlemaker:
        player.reset()
        enemy.reset()
        battlemaker.reset()
    clear_terminal()
    menu = ConsoleMenu(r"""
    oo____oo____oo_________ooo_____________________________________oo_
    oo____oo____oo__ooooo___oo____ooooo___ooooo__oo_oo_oo___ooooo__oo_
    oo____oo____oo_oo____o__oo___oo___oo_oo___oo_ooo_oo__o_oo____o_oo_
    _oo__oooo__oo__ooooooo__oo___oo______oo___oo_oo__oo__o_ooooooo_oo_
    __oooo__oooo___oo_______oo___oo______oo___oo_oo__oo__o_oo_________
    ___oo____oo_____ooooo__ooooo__ooooo___ooooo__oo______o__ooooo__oo_
    _______________________________________________________________oo_
    """, "Select an option below.")

    op1 = MenuItem('Start Battle Maker', should_exit=tr)
    op2 = MenuItem('Help and Info', should_exit=tr)

    menu.append_item(op1)
    menu.append_item(op2)

    menu.show()

    i = menu.selected_option

    if i == 0:
        battlemaker.main()
    elif i == 1:
        helpandinfo()
    elif i == 2:
        exit(0)
    mainmenu()


# Info
def helpandinfo():
    clear_terminal()
    menu = ConsoleMenu("Help and Info", "Select a option to view it.", show_exit_option=False)

    op1 = MenuItem("Credits", should_exit=tr)
    op2 = MenuItem("Battle Mechanics", should_exit=tr)
    op3 = MenuItem("Battle Maker", should_exit=tr)
    ex = MenuItem("Back to Main Menu", should_exit=tr)

    menu.append_item(op1)
    menu.append_item(op2)
    menu.append_item(op3)
    menu.append_item(ex)

    menu.show()

    i = menu.selected_option

    if i == 0:
        clear_terminal()
        print("Thank you to FiestyPetMaster and Linus (Not Linus Tech Tips) on Discord for helping me in the beginning.")
        print()
        print("Coder and Creator: TheKamboy")
        print("Art Maker: Originally FiestyPetMaster")
        print("Idea Maker: FiestyPetMaster and Linus")
        print()
        print("Helpers: My Family")
        print()
        print("Press any key to go back...")
        wait_key()
    elif i == 1:
        clear_terminal()
        print("Pizza is a RPG. It will work like an RPG. You attack ")
    elif i == 2:
        pass
    elif i == 3:
        mainmenu()
    else:
        mainmenu()
    helpandinfo()


if __name__ == "__main__":
    titlescreen()
else:
    print(sprites.runasscriptplease)
    exit(1)
