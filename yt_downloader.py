from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Description: ", yt.description)
print("Published: ", yt.publish_date)
print("Views: ", yt.views)

home_directory = os.path.expanduser("~")
download_path = os.path.join(home_directory, "youtube_downloads")

# this ensures the download directory exists
os.makedirs(download_path, exist_ok=True)

yd = yt.streams.get_highest_resolution()

file_path = yd.download(download_path)

# Print the relative path
print(f"Downloaded to: {os.path.relpath(file_path, start=home_directory)}")


