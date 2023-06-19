from tabulate import tabulate
import os
import subprocess
import msvcrt as m
from termcolor import colored, cprint
import sys


def print_menu(title, list_options):
    screenClean()
    print(title)
    for en, i in enumerate(list_options):
        if en > 0:
            print(f"{en}. {i}")
    print(f"{0}. {list_options[0]}")
    """Prints options in standard menu format like this:
    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program
    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """


def print_message(message):
    cprint(message, 'green')
    """Prints a single message to the terminal.
    Args:
        message: str - the message
    """


def print_general_results(label, result):
    cprint(f"{label} {result}", 'blue')
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, header):
    cprint(f"{tabulate(table, headers=header, tablefmt='fancy_grid')}", 'cyan')
    """Prints tabular data like above.
    Args:
        table: list of lists - the table to print out
    """


def get_input(label):
    option = input(label)
    return option
    """Gets single string input from the user.
    Args:
        label: st
        r - the label before the user prompt
    """


def get_inputs(labels):
    """Gets a list of string inputs from the user.
    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    cprint(message, 'red')
    """Prints an error message to the terminal.
    Args:
        message: str - the error message
    """

def screenClean():
    """Function to clear consol screen depends of OS"""
    myOs = sys.platform
    if myOs == 'win32':
        try:
            os.system('cls')
        except NameError:
           print ('\033[2J')
    elif myOs == 'linux':
        try:
            os.system('clear')
        except NameError:
            print ('\033[2J')
    elif myOs == 'darwin':
        try:
            os.system('cls')
        except NameError:
            print ('\033[2J')
    else:
        print('\033[2J')

def getch():
    print_message("Please click any button on Your keyboard to continue.")
    m.getch()