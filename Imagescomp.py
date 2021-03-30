#!/usr/bin/env python3
import os
from PIL import Image
import glob

def load_images(folder):
    images = os.listdir(folder)
    dst = "/opt/icons/"
    try:
        for img in images:
            with Image.open(folder+img) as im:
                im = Image.open(os.path.join(folder+img))
                #Rotating Images 90 degree Clockwise
                new_im = im.rotate(-90)
                #Resizing all images from 192x192 to 128x128
                new_im = new_im.resize((128,128))
                #Saving all images in new file
                new_im = new_im.convert('RGB')
                new_im.save(dst+img , format = 'jpeg')
    except IOError as e:
        print(e)


if __name__ == "__main__":
    dir = load_images("/home/student-00-1ab94beefbed/images/")
