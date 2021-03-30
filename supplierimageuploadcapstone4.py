#!/usr/bin/env python3
import requests, os
url = "http://localhost/upload/"
USER = os.getenv('USER')
image_directory = '/home/{}/supplier-data/images/'.format(USER)
files = os.listdir(image_directory)
for image_name in files:
    if not image_name.startswith('.') and 'jpeg' in image_name:
        image_path = image_directory + image_name
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file':opened})




