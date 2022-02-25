import os

dir = "C:/Users/Max/Documents/executables" # Directory of samples

for root, dirs, files in os.walk(dir): 
    for filename in files:
        print(os.path.join(root, filename))