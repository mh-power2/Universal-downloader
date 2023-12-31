import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os
import time
import chromedriver_autoinstaller
from datetime import datetime

cwd = os.getcwd()
relative_path = r'Google_Images_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def download_gimages(query, num_of_images):

    # Get current time and format it as a string, replacing the colon with a hyphen
    current_time = datetime.now().strftime('%H-%M-%S')

    # Create a new directory with the current time as the name
    subfolder_path = os.path.join(download_directory, current_time)
    os.makedirs(subfolder_path)

    # Set up Chromedriver
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.minimize_window()
    os.chdir(subfolder_path)

    # Perform image search
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    driver.get(url)

    # Scroll down to load more images
    scrolls = 0
    while scrolls < num_of_images:
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)  # Give time for new images to load
        scrolls += 1

    # Find image elements
    img_results = driver.find_elements(By.XPATH,
                                       "//img[contains(@class,'Q4LuWd')]")
    img_urls = [img.get_attribute('src') for img in img_results]

    # Download the specified number of images
    for i in range(num_of_images):
        urllib.request.urlretrieve(str(img_urls[i]), f"{query}{i + 1}.jpg")

    # Quit the driver and reset directory
    driver.quit()
    os.chdir(cwd)
