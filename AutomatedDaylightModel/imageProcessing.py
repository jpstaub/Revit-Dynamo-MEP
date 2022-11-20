# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:57:12 2022

@author: jpstaub for Ripcord Engineering and Active House USA

Image processing utility for Velux Daylight Visualizer zone images.

1. Removes Daylight Factor scale from image.
2. Makes Daylight Factor image with transparent background.
3. Crops Daylight Factor image with transparent background.
4. Saves cropped Daylight Factor image with transparent background for use.

Saved images can be overlayed and scaled on background plans to give
architectural context to Daylight Factor results.
"""

# import packages
import cv2
import os

from tkinter import *
from tkinter import filedialog

# filter file
def filter_file(file):
    if('w_zone' in file.split('.')[0]):
        return True

# crop out daylight factor scale
def remove_scale(root, file):
    original = cv2.imread(root + '/' + file)
    image = original[0:800, 200:1446]
    return image

# make grayscale image with cvtColor() function
def make_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

# make mask image with threshold() function
def make_mask(gray):
    mask = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)[1]
    return mask

# make transparent background image by placing the mask into the alpha channel
def make_transparent(image, mask):
    new_img = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    new_img[:, :, 3] = mask
    return new_img 
    
# get bounding rectangle of mask shape (should be one around the nonzero pixels)
def get_bounding(mask):
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    contour = contours[0]
    x,y,w,h = cv2.boundingRect(contour)
    return x,y,w,h

# crop image with bounding rectangle
def crop_image(new_img,x,y,w,h):
    crop = new_img[y:y+h, x:x+w]
    return crop

# save cropped image
def save_image(parent_dir,dest_dir,crop):
    filename = parent_dir + dest_dir + '/' + file.split('.')[0] + '_crop.' + file.split('.')[-1]
    cv2.imwrite(filename, crop)
    return

# define file variables
Tk().withdraw() # hides command line window
parent_dir = filedialog.askdirectory(title='Daylight Visualizer Report Directory')
dest_dir = '/crop'

# make crop directory
if 'crop' not in os.listdir(parent_dir):
    os.mkdir(parent_dir + dest_dir)

# make cropped images
for file in os.listdir(parent_dir):
    if filter_file(file):
        image = remove_scale(parent_dir, file)
        gray = make_gray(image)
        mask = make_mask(gray)
        new_img = make_transparent(image, mask)            
        try:
            x,y,w,h = get_bounding(mask)
        except IndexError:
            msg_error = 'The following file has no image to process: ' + file
            print(msg_error)
        else:      
            crop = crop_image(new_img, x,y,w,h)
            save_image(parent_dir,dest_dir,crop) 
msg_complete = 'File processing is complete!'
print(msg_complete)

