import os
import requests
from tqdm import tqdm

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Wallhaven_Wallpapers/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def download_wallpapers(query, num_images):
    # Define the URL for the Wallhaven API
    url = f"https://wallhaven.cc/api/v1/search?q={query}"
    # Initialize an empty list to store the links
    links = []
    # Make a GET request to the Wallhaven API
    res = requests.get(url)
    # Parse the JSON response
    jsonData = res.json()
    # Extract the links from the JSON data and append them to the list
    for link in jsonData["data"]:
        # Extract the filename from the URL
        filename = link["path"].split("/")[-1]
        # Append the filename to the list of links
        links.append((link["path"], filename))

    # Initialize a counter for successful downloads
    successful_downloads = 0
    # Download each wallpaper
    for i, (wallpaper_url, filename) in enumerate(links):
        # If the maximum number of downloads is reached, stop the loop
        if num_images is not None and successful_downloads >= num_images:
            break
        # If the download is successful, increment the counter
        if download_wall(wallpaper_url, filename, download_directory):
            successful_downloads += 1


def download_wall(url, filename, download_folder):
    # Define the path where the wallpaper will be saved
    path = os.path.join(download_folder, filename)
    # Check if the file already exists
    if os.path.isfile(path):
        # If the file exists, print a message and return without downloading the file
        print(f"==> File {filename} already exists. Skipping download.")
        return False
    # Make a GET request to the URL of the wallpaper, streaming the response
    res = requests.get(url, stream=True)
    # Print a message indicating that the download is starting
    print(f"==> Downloading... {filename}")
    # Get the total size of the file from the headers of the response
    total_size = int(res.headers.get("content-length", 0))
    # Define the block size for the download
    block_size = 1024
    # Open the file in write-binary mode and create a progress bar
    with open(path, "wb") as file, tqdm(total=total_size,
                                        unit="B",
                                        unit_scale=True,
                                        unit_divisor=1024,
                                        colour="green") as bar:
        # Download the file in chunks and update the progress bar
        for data in res.iter_content(block_size):
            file.write(data)
            bar.update(len(data))
    # Return True if the download is successful
    return True
