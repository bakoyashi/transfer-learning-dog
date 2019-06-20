import os, bs4, json
import urllib.request, urllib.error

keywords = ['rose', 'sunflower', 'lilium']

image_count = 50

for keyword in keywords:
    print("download now ...",  keyword)

    save_directory = "./dataset/" + keyword
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)


