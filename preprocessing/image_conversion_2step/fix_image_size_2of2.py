import numpy as np
from math import sqrt, ceil
import cv2
import os

# This script converts the original resolution images into fixed resolution images
# THIS SCRIPT DOES NOT CHANGE THE FULL RESOLUTION IMAGES

########## CHANGE ################
inputdir = "path" # Directory where the full resolution images are stored (without "/" at the end)
outputdir = "path" # Directory where the fixed resolution images need to be stored (with "/" at the end)
width = 256 # image width
height = 256 # image height

interpolation = cv2.INTER_CUBIC # interpolation algorithms
#################################
dim = (width, height)
j = 0

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

# Go through every file in directory
for root, dirs, files in os.walk(inputdir): 
    for f in files:
        file = os.path.join(root, f)
        filename = os.path.splitext(f)[0]

        # Read image
        img = cv2.imread(f"{root}/{f}")

    
        # Fix image size
        resized = cv2.resize(img, dim, interpolation=interpolation)
        cv2.imwrite(f"{outputdir}/{f}", resized)

        # Remove index after file for creating folders
        if "_" in filename:
            index_int = filename.find("_")
            foldername = filename[:index_int]
        else: foldername = filename

         # Move new image into the right folder
        if os.path.exists(f"{outputdir}{foldername}"):
            os.rename(f"{outputdir}{filename}.png", 
            f"{outputdir}{foldername}/{filename}.png")

        else:
            os.makedirs(f"{outputdir}{foldername}")
            os.rename(f"{outputdir}{filename}.png", 
            f"{outputdir}{foldername}/{filename}.png")


        # Print iteration
        j = j + 1
        print(f"Iteration: {j} - {filename}")