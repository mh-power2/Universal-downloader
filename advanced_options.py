# advanced_options.py
import os
import pyTextColor
from main_functions import handle_invalid_choice, reset_app
from start_aria import kill_aria2

# Create an instance of pyTextColor
pytext = pyTextColor.pyTextColor()


# Function to go back to the main menu
def go_back():
    """Goes back to the main menu"""
    return


# Define constants
ADVANCED_OPTIONS = {
    "1":
    ("Kill Download Manager: use this to kill aria2 process in the case of any problem, warning you will lose all of your queue.",
     kill_aria2, "#FF0000"),
    "2":
    ("Rest Application: this will remove everything, MAKE A COPY OF YOUR DOWNLOADS FIRST!!",
     reset_app, "#FF0000"),
    "3": ("Back", None, "#FFFFFF"),
}


# Function to handle operation based on user's choice
def handle_operation(option, options):
    """Handles the operation based on the user's choice. If the choice is valid, it executes the corresponding function. Otherwise, it calls the handle_invalid_choice function"""
    title, func, color = options.get(option, (None, None, None))
    if title is not None:
        if title == "Back":
            return True
        print(pytext.format_text(text=title, color=color))
        func()
        return False
    else:
        handle_invalid_choice()
        return False


# Function to handle advanced options
def advanced_options():
    """Handles advanced options"""
    while True:
        os.system("cls")  # Clear console

        # Print menu options
        for key, value in ADVANCED_OPTIONS.items():
            print(
                f"{key}: {pytext.format_text(text=value[0], color=value[2])}")

        # Prompt user to choose an option
        choice = input(
            pytext.format_text(text="Enter your choice: ", color="#ffff00"))

        # Handle user's choice
        if handle_operation(choice, ADVANCED_OPTIONS):
            break
