import numpy as np
from math import sqrt, ceil
import cv2
import os


# This script converts a file into a grayscale image with a fixed resolution 
# THIS SCRIPT DOES NOT STORE THE FULL RESOLUTION IMAGES

##### CHANGE #######
inputdir = "C:/Users/Max/Documents/executables" # Directory of samples
outputdir = "C:/Users/Max/Documents/images/" # Directory where the samples need to be stored (with "/" at the end)
width = 256 # image width
height = 256 # image height

interpolation = cv2.INTER_CUBIC # interpolation algorithms
#################################
dim = (width, height)
j = 0

# Go through every file in directory
for root, dirs, files in os.walk(inputdir): 
    for f in files:
        filename = os.fsdecode(f)
        
        if ".exe" in filename:
            index = filename.find(".exe")
            filename = filename[:index] 

        file = os.path.join(root, f)
            
        # Read the whole file to data
        with open(file, 'rb') as binary_file:
            data = binary_file.read()
        binary_file.close()

        # Data length in bytes
        data_len = len(data)

        # d is a vector of data_len bytes
        d = np.frombuffer(data, dtype=np.uint8)

        # Assume image shape should be close to square
        sqrt_len = int(ceil(sqrt(data_len)))  # Compute square toot and round up

        # Requiered length in bytes.
        new_len = sqrt_len * sqrt_len

        # Number of bytes to pad (need to add zeros to the end of d)
        pad_len = new_len - data_len

        # Pad d with zeros at the end.
        # padded_d = np.pad(d, (0, pad_len))
        padded_d = np.hstack((d, np.zeros(pad_len, np.uint8)))

        # Reshape 1D array into 2D array with sqrt_len pad_len x sqrt_len (im is going to be a Grayscale image).
        im = np.reshape(padded_d, (sqrt_len, sqrt_len))

        # Save image to correct folder within directory
        cv2.imwrite(f"{outputdir}{filename}.png", im)

        # Read image
        img = cv2.imread(f"{outputdir}{filename}.png")

        # Fix image size
        resized = cv2.resize(img, dim, interpolation=interpolation)
        cv2.imwrite(f"{outputdir}{filename}.png", resized)

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

        # Show progress
        j = j + 1
        print(f"File: {j} - {filename}")

        # Display image
        # cv2.imshow('im' ,im)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        