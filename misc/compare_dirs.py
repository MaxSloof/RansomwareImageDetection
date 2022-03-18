import os
import numpy as np

dir_local = "C:/Users/Max/Documents/thesis_data/benign"
dir_google = "H:/My Drive/data/benign"

array_local = np.array([])
for root, dirs, files in os.walk(dir_local):
    for f in files: 
        array_local = np.append(array_local, f)

array_google = np.array([])
for root, dirs, files in os.walk(dir_google):
    for f in files: 
        array_google = np.append(array_google, f)

same_array = np.array([])
not_same_array = np.array([])
for file in array_local:
    if np.any(file == array_google):
        same_array = np.append(same_array, file)
    else: not_same_array = np.append(not_same_array, file)

print("Number of files that are identical: ", len(same_array))
print("Number of files that are NOT identical: ",len(not_same_array))
print("Not identical: ", not_same_array)