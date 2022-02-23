import requests
import os
import numpy

# Set wd
wdir = "C:/Users/Max/Documents/virus_test"
os.chdir(wdir)
ledgerpath = "C:/Users/Max/Documents/ledger.txt"

# Includes API key
headers = {"Accept": "application/json",
           "x-apikey": "f9f8fb829768faaa42dfe6d5997ad73f517aa6af08f0255a84544f9a519bed73"}

# To name each file uniquely
j = 0

# Go through each file in the directory
for file in os.listdir(wdir):

    # Iterate j so every file can get unique name
    j = j + 1

    # If there have been more than 19,000 API requests, stop the loop.
    # The academic API from VirusTotal has an API limit of 20,000
    if j > 3:
        break

    if file.endswith(".txt"): # Can be deleted for real
        
        # split the hash and file extension from each other
        filename = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]

        # Create unique API request for every hash
        url = f"https://www.virustotal.com/api/v3/files/{filename}"
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

                        # Give every file a unique name based on the iteration
                        newfilename = f"{famname}_{j}"
                        print(newfilename)

                        # Add line to ledger
                        print(f"{newfilename}{file_ext} = {newfilename}{file_ext}", file = open(ledgerpath, "a+"))

                        # Rename the hash file name to family name
                        # If directory exists, do not create a new one. If it does not exist, create a new one
                        if os.path.exists(f"C:/Users/Max/Documents/virus_test/{famname}"):
                            os.rename(f"C:/Users/Max/Documents/virus_test/{filename}.txt",
                                  f"C:/Users/Max/Documents/virus_test/{famname}/{newfilename}{file_ext}")
                        else: 
                            os.makedirs(f"C:/Users/Max/Documents/virus_test/{famname}")
                            os.rename(f"C:/Users/Max/Documents/virus_test/{filename}.txt",
                                  f"C:/Users/Max/Documents/virus_test/{famname}/{newfilename}{file_ext}")
                    continue
                continue
            continue
        continue