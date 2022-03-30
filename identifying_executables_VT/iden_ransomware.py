import requests
import os
import numpy

# This script goes through a list of ransomware samples (not in specific folders) with a hash string as their filename
# It compares the hash value with the VirusTotal database. 
# The Microsoft report for that sample is retrieved and the name of the ransomware family + a counter is given to the sample. 

# Set wd
dir = "path"                   # Path to where the ransomware files with hash as filename are located (without final "/")
os.chdir(dir)                  # The files should not be in folders 
ledgerpath = "path/ledger.txt" # Path to ledger text document

# Includes API key
headers = {"Accept": "application/json",
           "x-apikey": "key"} # Your VirusTotal API key

# To name each file uniquely
j = input("starting value ...")

# Go through each file in the directory
for file in os.listdir(dir):

    # Iterate j so every file can get unique name
    j = j + 1

    # If there have been more than 19,000 API requests, stop the loop.
    # The academic API from VirusTotal has an API limit of 20,000
    if j > 1: break # stop after j iterations

    if file.endswith(".txt"): # Can be deleted for real
        
        # split the hash and file extension from each other
        oldfilename = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]

        # Create unique API request for every hash
        url = f"https://www.virustotal.com/api/v3/files/{oldfilename}"
        r = requests.request("GET", url, headers=headers)

        # Write the response as HTML file
        response = r.text
        with open("response.html", "w") as fWrite:
            fWrite.write(response)
        fWrite.close()

        # Open the response HTML file as an array of lines
        fRead = open("response.html", "r")
        searchLines = fRead.readlines()
        fRead.close()

        # Go through each line and find where Microsoft is mentioned
        for i, line in enumerate(searchLines):
            if "Microsoft" in line:
                
                # Save the fourth and fifth line after that
                for l in searchLines[i+4:i+5]:

                    # If 'result' is found in one the lines, isolate the ransomware family name
                    if "result" in l:
                        index_start = l.find("/") + 1
                        index_end = l.find('"', index_start)
                        famname = l[index_start:index_end]

                        # Each ransomware family is added without considering the letter behind the dot
                        if "." in famname: 
                            index_int = famname.find(".")
                            foldername = famname[:index_int]
                        elif "!" in famname: 
                            index_int = famname.find("!")
                            foldername = famname[:index_int]
                        else: foldername = famname

                        # Give every file a unique name based on the iteration
                        newfilename = f"{famname}_{j}"
                        print(newfilename)

                        # Add line to ledger
                        print(f"{oldfilename}{file_ext} = {newfilename}{file_ext}", file = open(ledgerpath, "a+"))

                        # Rename the hash file name to family name
                        # If directory exists, do not create a new one. If it does not exist, create a new one
                        if os.path.exists(f"C:/Users/Max/Documents/virus_test/{foldername}"): # Destination path
                            os.rename(f"C:/Users/Max/Documents/virus_test/{oldfilename}{file_ext}", # Origin path
                                  f"C:/Users/Max/Documents/virus_test/{foldername}/{newfilename}{file_ext}") # Destination path
                        else: 
                            os.makedirs(f"C:/Users/Max/Documents/virus_test/{foldername}") # Destination path
                            os.rename(f"C:/Users/Max/Documents/virus_test/{oldfilename}{file_ext}", # Origin path
                                  f"C:/Users/Max/Documents/virus_test/{foldername}/{newfilename}{file_ext}") # Destination path
                    continue
                continue
            continue
        continue