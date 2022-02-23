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
    j = j + 1
    if file.endswith(".txt"): # Can be deleted for real
        filename = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]
        url = f"https://www.virustotal.com/api/v3/files/{filename}"
        r = requests.request("GET", url, headers=headers)

        response = r.text
        with open("response.html", "w") as fWrite:
            fWrite.write(response)
        fWrite.close()

        fRead = open("response.html", "r")
        searchLines = fRead.readlines()
        fRead.close()

        for i, line in enumerate(searchLines):
            if "Microsoft" in line:
                for l in searchLines[i+4:i+5]:
                    if "result" in l:
                        index_start = l.find("/") + 1
                        index_end = l.find('"', index_start)
                        famname = l[index_start:index_end]
                        newfilename = f"{famname}_{j}"
                        print(newfilename)

                        # Add line to ledger
                        print(f"{newfilename}{file_ext} = {newfilename}{file_ext}", file = open(ledgerpath, "a+"))


                        # Rename the hash file name to family name
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