import numpy as np
from math import sqrt, ceil
import cv2
import os


########## CHANGE ################
outputdir = "C:/Users/Max/Documents/images/" # Directory where the samples need to be stored (with "/" at the end)
width = 256 # image width
height = 256 # image height

interpolation = cv2.INTER_CUBIC # interpolation algorithms
#################################
dim = (width, height)
j = 0


# Go through every file in directory
for root, dirs, files in os.walk(outputdir): 
    for f in files:
        filename = os.fsdecode(f)
        file = os.path.join(root, filename)
        

        # Read image
        img = cv2.imread(f"{root}/{filename}")

        # Fix image size
        resized = cv2.resize(img, dim, interpolation=interpolation)
        cv2.imwrite(f"{root}/{filename}", resized)

        # Print iteration
        j = j + 1
        print(f"Iteration: {j} - {filename}")