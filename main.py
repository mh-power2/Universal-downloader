# Import necessary libraries
import os
import pyTextColor

# Import functions needed
from main_functions import *
from advanced_options import advanced_options

# Create an instance of pyTextColor
pytext = pyTextColor.pyTextColor()

#initilaize the app:
initialize_app()

# Define constants
MENU_OPTIONS = {
    "1": ("Download Manager", download_manager, "#FFFFFF"),
    "2": ("Youtube Downloader", download_youtube, "#FF0000"),
    "3": ("Soundcloud Downloader", download_soundcloud, "#FFA500"),
    "4": ("Lightnovels Downloader", download_lightnovels, "#0000FF"),
    "5": ("Spotify Downloader", download_spotify, "#00FF00"),
    "6": ("Video Editing", video_editing, "#00ffff"),
    "7": ("Download Wallpapers", download_wallpapers, "#ff00ff"),
    "8": ("Google Drive Download", google_drive_download, "#ff007f"),
    "9": ("Download Photos", download_photos, "#7fff00"),
    "10": ("Download Google images", download_gimages, "#007fff"),
    "11": ("Advanced Options", advanced_options, "#000000"),
    "12": ("Quit", quit, "#7f7f7f"),
}


# Function to prompt user with a message
def prompt_user(message):
    """Prompts the user with a given message and returns the user's input"""
    return input(message)


# Function to handle operation based on user's choice
def handle_operation(option):
    """Handles the operation based on the user's choice. If the choice is valid, it executes the corresponding function. Otherwise, it calls the handle_invalid_choice function"""
    title, func, color = MENU_OPTIONS.get(option, (None, None, None))
    if title is not None:
        print(pytext.format_text(text=title, color=color))
        func()
    else:
        handle_invalid_choice()


# Main loop for the menu
while True:
    os.system("cls")  # Clear console

    # Print menu options
    for key, value in MENU_OPTIONS.items():
        print(f"{key}: {pytext.format_text(text=value[0], color=value[2])}")

    # Prompt user to choose an option
    choice = prompt_user(
        pytext.format_text(text="Enter your choice: ", color="#ffff00"))

    # Handle user's choice
    handle_operation(choice)
