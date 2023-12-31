import os
import subprocess
# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Youtube_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def download_video(URL, quality=None):
    # Define the path to the yt-dlp.exe
    yt_dlp_path = os.path.join(cwd, 'Binaries', 'yt-dlp', 'yt-dlp.exe')

    # Map quality to format codes
    quality_to_format = {
        '144p': '160+bestaudio',
        '240p': '133+bestaudio',
        '480p': '135+bestaudio',
        '720p': '136+bestaudio',
        '1080p': '137+bestaudio',
        '2K': '138+bestaudio',
        '4K': '139+bestaudio',
        '8K': '272+bestaudio'
    }

    # Get the format code from the quality
    format_code = quality_to_format.get(quality, '135+bestaudio')

    # Define the command to run yt-dlp.exe
    command = [
        yt_dlp_path, '-f', format_code, '-o',
        download_directory + '/%(title)s.%(ext)s', URL
    ]

    # Run the command
    subprocess.run(command, shell=True)
