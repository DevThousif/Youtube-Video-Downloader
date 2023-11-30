from pytube import YouTube
from sys import argv
import os
try:
   
    url = input("Enter the YouTube URL: ")
    
    youtube = YouTube(url)
    
    print("Title:", youtube.title)
    print("Views:", youtube.views)

  
    youtubedownload = youtube.streams.get_highest_resolution()
    
   
    youtubedownload.download ('C:\Coding\python\Youtube Downloader\Downloaded Video')
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))