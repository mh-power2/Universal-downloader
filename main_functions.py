# Import necessary libraries
import os
import time
import gdown
import sys
import subprocess
import pyTextColor
import shutil

# Create an instance of pyTextColor
pytext = pyTextColor.pyTextColor()

# Import functions needed
from aria2 import download_manager
from aria2_functions import is_valid_url
from Youtube import download_video
from soundcloud import soundcloud
from Light_novels import download_novel
from sources import sources
from spotifiy import spotify
from edit_video import *
from wallhaven import download_wallpapers
from google_images import download_gimages
from photos import download_photos

from start_aria import run_aria2
from FFMPEG import *

import subprocess


def initialize_app():
    """
    Initialize all dependencies:
    - Install the required packages listed in 'requirements.txt'
    - Run the Aria2 downloader in the background
    - Check if yt_dlp is installed
    - Install FFMPEG
    """

    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    run_aria2()
    yt_dlp_install()
    ffmpeg_install()


def handle_invalid_url(url):
    """
    Handles invalid URLs by printing an error message.

    Args:
        url (str): The invalid URL.

    Returns:
        None
    """
    # Print the error message
    print(f"Invalid URL: {url}")

    # Pause execution for 1 second
    time.sleep(1)


def handle_invalid_choice():
    """Handle an invalid choice.

    Prints an error message, waits for 1 second, and clears the console.
    """
    print(
        pytext.format_text(text="Wrong choice... Please try again.",
                           color="#ff0000"))
    time.sleep(1)
    os.system("cls")


def download_youtube():
    """Download YouTube videos or playlists."""
    # Clear the console screen
    os.system("cls")

    # Prompt user for the YouTube video or playlist link
    URL = input(
        "Enter the link of the video/playlist or type any character to go back: "
    )

    # Check if the entered URL is valid
    if is_valid_url(URL):
        # Prompt user for the desired video quality
        QUALITY = input(
            "Enter the quality (144p,240p,480p,720p,1080p,2K,4K,8K): ")

        # Download the video with the specified quality
        download_video(URL, QUALITY)

        # Wait for 3 seconds
        time.sleep(3)

        # Clear the console screen
        os.system("cls")

        # Print a message indicating that the download has finished
        print("Download Finished")

        # Wait for 3 seconds
        time.sleep(3)
    else:
        # Print an error message if the URL is invalid
        print("Invalid URL... or Going back")

        # Wait for 2 seconds
        time.sleep(2)


def download_soundcloud():
    """
    Downloads SoundCloud tracks, playlists, or users.

    Prompts the user for a URL and checks if it is a valid SoundCloud URL.
    If it is valid, it calls the soundcloud function and waits for 3 seconds.
    If it is not valid, it prints an error message and waits for 2 seconds.
    """
    os.system("cls")  # Clear the console
    URL = input(
        "Enter a URL for a track/playlist/user or enter any character to go back: "
    )

    if is_valid_url(URL):
        soundcloud(URL)
        time.sleep(3)
        os.system("cls")
    else:
        print("Wrong URL entered.. or Going back")
        time.sleep(2)


def download_lightnovels():
    """Download light novels.

    Options:
    1. Show Sources: Display a list of available sources.
    2. Enter Link to download: Prompt the user to enter a URL and download the novel.

    Args:
        None

    Returns:
        None

    """
    os.system("cls")
    option = input("1-Show Sources\n2-Enter Link to download\n3-Back\n")

    if option == "1":
        # Show available sources
        for i, source in enumerate(sources.items(), start=1):
            print(f"{i}. {source[1]['name']} {source[1]['link']}")
        input('Enter anything to go back!')
        os.system("cls")

    elif option == "2":
        # Download novel from the provided URL
        URL = input("Enter the URL: ")
        if is_valid_url(URL):
            Rng = input(
                "Enter the range in this format (start end) or type all: ")
            download_novel(URL, Rng)
            os.system("cls")
            print("Novel Downloaded Successfully!")
            time.sleep(2)
        else:
            print("Wrong URL entered..")
            time.sleep(2)

    elif option == "3":
        pass
    else:
        print("Wrong choice..")
        time.sleep(0.7)
        download_lightnovels()


def download_spotify():
    """
    Downloads a song from Spotify using the provided URL.

    Args:
        None

    Returns:
        None
    """
    # Clear the console
    os.system("cls")

    # Prompt the user for the URL of the song
    URL = input("Enter the URL of the song or type any character to go back: ")

    # Check if the URL is valid
    if is_valid_url(URL):
        # Download the song from Spotify
        spotify(URL)
        print("Download finished")
    else:
        print("Wrong URL entered.. or going back")

    # Pause for 2 seconds
    time.sleep(2)

    # Clear the console again
    os.system("cls")


def video_editing():
    """Edit videos.

   Convert video, compress video CPU, or compress video GPU.
   """
    os.system("cls")

    # Define the available options
    options = {
        "1": convert_video,
        "2": compress_video,
        "3": compress_video_GPU,
        "4": None,
    }

    # List of supported formats
    supported_formats = ['mp4', 'flv', 'avi', 'mov', 'wmv', 'mkv']

    # Prompt the user to choose an option
    x = input(
        "1-Convert Video\n2-Compress Video CPU (slow but smaller and better quality)\n3-Compress Video GPU (faster but bigger size and lower quality)\n4-Back\n"
    )

    if (x == "4"):
        return

    elif x in options:
        # Prompt the user for the video path
        while True:
            path = input(
                "Enter the video path or type 'cancel' to exit: ").strip('"')
            if path.lower() == 'cancel':
                print("Operation cancelled.")
                return
            elif os.path.exists(path):
                if (is_video_file(path)):
                    break
            else:
                if (not os.path.exists(path)):
                    print("The path does not exist. Please try again.")
                else:
                    print("the path is not a video file. Please try again.")

        # Prompt the user for the format or CRF based on the chosen option
        if x == "1":
            format = input("Enter the format of the video: ").strip('"')
            if format not in supported_formats:
                print("Unsupported format. Please try again.")
                return
            options[x](path, format)
        else:
            while True:
                try:
                    CRF = int(
                        input(
                            "Enter the quality factor (0-51) the lower the higher the quality but the bigger the size (Ideal 28~32): "
                        ))
                    if 0 <= CRF <= 51:
                        break
                    else:
                        print("Please enter an integer between 0 and 51.")
                except ValueError:
                    print("Invalid input! Please enter an integer.")

            options[x](path, CRF)

        # Print a message indicating that the operation is done
        print("Done!")
        time.sleep(2)
    else:
        # Print an error message if the user enters an invalid option
        print("Wrong choice!")
        time.sleep(1)
        video_editing()


def download_wallpapers():
    """Download wallpapers."""
    query = input("Enter the search query: ")
    number = int(input("Enter the number of images or enter 0 to cancel: "))
    if (number != 0):
        download_wallpapers(query, number)
        print("Download finished!")
        time.sleep(1.5)


def google_drive_download():
    """Download files or folders from Google Drive."""
    if not os.path.exists(os.path.join(os.getcwd(), 'GoogleDrive_Downloads/')):
        os.makedirs(os.path.join(os.getcwd(), 'GoogleDrive_Downloads/'))
    os.system("cls")
    x = input("1-Download a file   2-Download a folder\n")
    if (x == "1"):
        URL = input("Enter the file URL: ")
        if (is_valid_url(URL)):
            gdown.download(URL,
                           output=os.path.join(os.getcwd(),
                                               'GoogleDrive_Downloads/'),
                           fuzzy=True)
            print("\n\nDownload Finished")
            time.sleep(2)
        else:
            print("wrong URL..")
            time.sleep(1.5)
    elif (x == "2"):
        URL = input("Enter the folder URL(maximum 50 files per folder): ")
        if (is_valid_url(URL)):
            gdown.download_folder(URL,
                                  output=os.path.join(
                                      os.getcwd(), 'GoogleDrive_Downloads/'),
                                  quiet=False,
                                  use_cookies=False)
            print("\n\nDownload Finished")
            time.sleep(2)
        else:
            print("wrong URL..")
            time.sleep(1.5)
    else:
        print("Wrong choice...")
        time.sleep(1.5)


def download_photos():
    """Download photos from a website."""
    os.system("cls")
    url = input(
        "Enter the URL of the website you want to download photos from: ")
    if (is_valid_url(url)):
        download_photos(url)
        print("Download Finished")
    else:
        print("Bad URL")
    time.sleep(2)


def download_gimages():
    """Download images from Google Images."""
    os.system("cls")
    name = input("Enter the name of the photos you looking for: ")
    num = int(input("Enter the number of photos you want to download"))
    download_gimages(name, num)
    print("Download Finished")
    time.sleep(5)


def reset_app():
    """Reset the application."""
    if (str.lower(input("Are your really sure you want to this? (yes/no)\n"))
            == "yes"):
        cwd = os.getcwd()
        paths = [
            os.path.join(cwd, 'Binaries/ffmpeg/'),
            os.path.join(cwd, 'Binaries/yt-dlp/'),
            os.path.join(cwd, 'Youtube_Downloads/'),
            os.path.join(cwd, 'Soundcloud_Downloads/'),
            os.path.join(cwd, 'Spotifiy_Downloads/'),
            os.path.join(cwd, 'Video_Output/'),
            os.path.join(cwd, 'Wallhaven_Wallpapers/'),
            os.path.join(cwd, 'Lightnovels_Downloads/'),
            os.path.join(cwd, 'Images_Downloads/'),
            os.path.join(cwd, 'Google_Images_Downloads/'),
            os.path.join(cwd, 'Manager_Downloads/'),
        ]
        for i in paths:
            if os.path.exists(i):
                shutil.rmtree(i)
        print("Resting finished, Application will quit in 3 seconds...")
        time.sleep(3)
        quit()


def quit():
    """Quit the application."""
    os.system("cls")
    sys.exit(0)
