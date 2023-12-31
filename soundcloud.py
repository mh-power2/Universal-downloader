import os
import subprocess

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Soundcloud_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def soundcloud(URL):

    # Define the command to run scdl
    command = ['scdl', '-l', URL.split('&utm')[0]]
    # Run the command
    subprocess.run(command, cwd=download_directory)
