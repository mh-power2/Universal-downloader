from FFMPEG import ffmpeg_install
import os
import subprocess

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Spotifiy_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

#check if installed if not then install ffmpeg
ffmpeg_install()


def spotify(URL):

    # Define the command to run scdl
    command = ['spotdl', URL]
    # Run the command
    subprocess.run(command, cwd=download_directory)
