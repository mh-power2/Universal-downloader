import os
import subprocess

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Lightnovels_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

Format = "epub"


def download_novel(Link, Range):

    Misc_command = " --suppress --auto-proxy"

    if (Range.lower() == "all"):
        command = [
            'lncrawl', '--single', '-o', download_directory, '-s', Link,
            '--format', 'epub', '--all'
        ] + Misc_command.split()
    else:
        command = [
            'lncrawl', '--single', '-o', download_directory, '-s', Link,
            '--format', 'epub', '--range', Range
        ] + Misc_command.split()

    subprocess.run(command)
