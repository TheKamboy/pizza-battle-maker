import player
import enemy
import sprites
from consolemenu import *
from consolemenu.items import *

namedone = False
hpdone = False
spritedone = False
strengthdone = False
exitbattlemaker = False
spriteselectedsize = 0

tr = True


# Strength, HP, Name, Sprite
def main():
    global exitbattlemaker
    clear_terminal()
    menu = ConsoleMenu("Battle Maker Menu", "Make your battle here", show_exit_option=False)

    op1 = MenuItem("Name", should_exit=tr)
    op2 = MenuItem("Enemy Sprite\n", should_exit=tr)
    op3 = MenuItem("Health", should_exit=tr)
    op4 = MenuItem("Strength\n", should_exit=tr)
    op5 = MenuItem("START\n\n", should_exit=tr)
    ex = MenuItem("Back to Main Menu", should_exit=tr)

    menu.append_item(op1)
    menu.append_item(op2)
    menu.append_item(op3)
    menu.append_item(op4)
    menu.append_item(op5)
    menu.append_item(ex)

    menu.show()

    i = menu.selected_option

    if i == 0:
        namemaker()
    elif i == 1:
        spritesize()
    elif i == 2:
        hpmaker()
    elif i == 3:
        pass
    elif i == 4:
        pass
    elif i == 5:
        yesno = input("Are you sure you want to exit? (y/N) ").lower().strip()
        if yesno == "y":
            exitbattlemaker = True
        else:
            main()

    if not exitbattlemaker:
        main()


def reset():
    global namedone, strengthdone, spritedone, hpdone, exitbattlemaker, spriteselectedsize
    namedone = False
    strengthdone = False
    spritedone = False
    hpdone = False
    exitbattlemaker = False
    spriteselectedsize = 0


def namemaker():
    global namedone
    clear_terminal()
    a = input("Player Name: ")
    print()
    b = input("Enemy Name: ")
    print()
    player.name = a
    enemy.name = b
    namedone = True


def spritesize():
    clear_terminal()
    menu = ConsoleMenu("What size of sprite do you want?", show_exit_option=False)

    sma = MenuItem("Small (1 Line)", should_exit=tr)  # 0
    med = MenuItem("Medium (3 Lines)", should_exit=tr)  # 1
    big = MenuItem("Big (5 Lines)", should_exit=tr)  # 2

    menu.append_item(sma)
    menu.append_item(med)
    menu.append_item(big)

    menu.show()

    i = menu.selected_option

    if i == 0:
        smallsprite()
    elif i == 1:
        mediumsprite()
    elif i == 2:
        bigsprite()


def smallsprite():
    global spriteselectedsize
    spriteselectedsize = 0
    clear_terminal()
    a = input(": ")
    enemy.sprite = fr"""
{a}
"""
    spriteareyousure()


def mediumsprite():
    global spriteselectedsize
    spriteselectedsize = 1
    clear_terminal()
    a = input(": ")
    b = input(": ")
    c = input(": ")
    enemy.sprite = fr"""
{a}
{b}
{c}
"""
    spriteareyousure()


def bigsprite():
    global spriteselectedsize
    spriteselectedsize = 2
    clear_terminal()
    a = input(": ")
    b = input(": ")
    c = input(": ")
    d = input(": ")
    e = input(": ")
    enemy.sprite = fr"""
{a}
{b}
{c}
{d}
{e}
"""
    spriteareyousure()


def spriteareyousure():
    global spritedone, spriteselectedsize
    clear_terminal()
    print("Is this what you want your sprite to look like?:")
    print()
    print(enemy.sprite)
    print()
    yesno = input("Y/n: ").lower().strip()
    if yesno == "n":
        if spriteselectedsize == 0:
            smallsprite()
        elif spriteselectedsize == 1:
            mediumsprite()
        elif spriteselectedsize == 2:
            bigsprite()
    else:
        spritedone = True


def hpmaker():
    pass
