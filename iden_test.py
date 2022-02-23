import requests
import os
import numpy

wdir = "C:/Users/Max/Documents/virus_test"

# Set wd
os.chdir(wdir)

file = open("response.html", "r")
searchLines = file.readlines()
file.close()
for i, line in enumerate(searchLines):
  if "Microsoft" in line:
    for l in searchLines[i+4:i+5]:
        if "result" in l:
            index_start = l.find("/") + 1
            index_end = l.find('"', index_start)
            k = l[index_start:index_end]
            famname = f"{k}"
            print(famname)



    continue