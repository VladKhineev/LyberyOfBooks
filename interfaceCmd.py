import os


def clear_console():
    os.system('cls')


def message_output(message):
    clear_console()
    input(message)
    clear_console()