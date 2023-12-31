# Import necessary libraries
import os
import time
import pyTextColor
from aria2_functions import *

from start_aria import run_aria2

# Create an instance of pyTextColor
pytext = pyTextColor.pyTextColor()

# Define constants
DOWNLOAD_MANAGER_OPTIONS = {
    "1": ("Add Download", add_download),
    "2": ("Pause Download", pause_download),
    "3": ("Resume Download", resume_download),
    "4": ("Remove Download", remove_download),
    "5": ("Show Queue", show_queue),
    "6": ("Schedule link", schedule_link),
    "7": ("Back", None),
}


# Function to prompt user with a message
def prompt_user(message):
    """Prompts the user with a given message and returns the user's input"""
    return input(message)


# Function to handle invalid choice
def handle_invalid_choice():
    """Handles an invalid choice by printing an error message and waits for 0.7 seconds"""
    print(
        pytext.format_text(text="Wrong choice... Please try again.",
                           color="#ff0000"))
    time.sleep(0.7)


# Function to handle operation based on user's choice
def handle_operation(option):
    """Handles the operation based on the user's choice. If the choice is valid, it executes the corresponding function. If the function is 'Quit', it returns True; otherwise, it returns False"""
    title, func = DOWNLOAD_MANAGER_OPTIONS.get(option, (None, None))
    if title is not None:
        if title == "Back":
            return True
        print(pytext.format_text(text=title, color="#00ff00"))
        func()
        return False
    else:
        handle_invalid_choice()
        return False


# Function to manage downloads
def download_manager():
    """Manages downloads by displaying a menu and handling user choices"""

    #repeated initialization in case the user killed the process
    run_aria2()

    while True:
        os.system("cls")  # Clear console

        # Try to flush the buffer
        while msvcrt.kbhit():
            msvcrt.getch()

        # Print menu options
        for key, value in DOWNLOAD_MANAGER_OPTIONS.items():
            print(
                pytext.format_text(text=f"{key}: {value[0]}", color="#0000ff"))

        # Prompt user to choose an option
        choice = prompt_user(
            pytext.format_text(text="Enter your choice: ", color="#ffff00"))

        # Handle user's choice
        if handle_operation(choice):
            break
