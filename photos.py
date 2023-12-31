from bs4 import *
import requests
import os
import time
from datetime import datetime

cwd = os.getcwd()
relative_path = r'Images_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def download_photos(url):
    # Get current time and format it as a string, replacing the colon with a hyphen
    current_time = datetime.now().strftime('%H-%M-%S')

    # Create a new directory with the current time as the name
    subfolder_path = os.path.join(download_directory, current_time)
    os.makedirs(subfolder_path)

    r = requests.get(url)

    htmldata = r.content
    soup = BeautifulSoup(htmldata, 'lxml')
    imgs = soup.find_all('img')

    # Check if the page contains any images
    if not imgs:
        print("The link doesn't contain images")
        os.removedirs(subfolder_path)
        time.sleep(2)
        return

    list_of_imgs = []

    for i in range(len(imgs)):
        img_url = imgs[i]['src']
        list_of_imgs.append(img_url)

    for i in range(len(list_of_imgs)):
        img_data = requests.get(list_of_imgs[i]).content
        # Change the file path to include the subfolder
        with open(os.path.join(subfolder_path, f'img{i}.png'), 'wb') as fd:
            fd.write(img_data)
