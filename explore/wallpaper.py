'''
author: Tarkan Zarrouk
date: 02/07/2024
A file dedicated to creating a walmart wallpaper
engine
'''

# Organizing imports by alphabetical order
# Managing data types from C
import ctypes
# Manage windows
import os
# library dedicated to requests
import urllib.request
# Import time library for timer
import time


def getWallpaper():
    # "Download" an image from the internet
    # https -> Hyper Text Transfer Protocol Secure
    # Setting the directory of / / allows us to specifiy
    response = urllib.request.urlopen("https://picsum.photos/1920/1080")
    # allows us to look into the directory as a "list" (sorta)
    # print(response.read())
   
   
    # Allows us to store the image into a file for future use
    file_name = "temp.jpg"
    # open allows us to open, create, delete files
    # Convetion file input output <--- f_out mainly used in unit 3, file stuff
    with open(file_name, mode="wb") as f_out:
        f_out.write(response.read())
    return os.path.join(os.getcwd(), file_name)    

def setWallpaper():
    # Invoke function for reference
    image_path = getWallpaper()
    # Set the currenet user's desktop wallpaper
    # We can use SystemParametersInfoW function using python
    # To edit the a lot of desktop functions
    # getcwd gets the full absolute file path of the currrent
    # File directory
    succeeed = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    return succeeed

setWallpaper()
