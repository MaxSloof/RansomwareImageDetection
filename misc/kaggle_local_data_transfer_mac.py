import os

# Command for Terminal - Copy underlying line #
# python3 /Users/maxsloof/Github/data_acq/misc/kaggle_local_data_transfer_mac.py    


# Ask what notebook you want to save the latest version of
print("What notebook do you want to save the latest version of?")
nt_type = input()
print("--------------")

dir = "/Users/maxsloof/Github/data_acq/kaggle_output"
vnum = 1
# Find the latest version number
file_exists = []

for files in os.listdir(dir):
    type = files[:-5]
    if type == nt_type: 
        vnum = max(vnum, int(files[-3:]))
        new_vnum = vnum + 1
        file_exists.append(True)
    else: 
        file_exists.append(False)

# If this is the first notebook you want to save, a new folder will be created with version #001
if sum(file_exists) == 0:
    new_vnum = 1
    print("No matches found")

else: 
    print(f"{sum(file_exists)} matches(es) found")
    print("--------------")

# Print new folder name
print(f"New folder name: {nt_type}-v{new_vnum:03}")
print("--------------")

# Create new folder with the name of the notebook and the version number
new_dir = f"/Users/maxsloof/Github/data_acq/kaggle_output/{nt_type}-v{new_vnum:03}"
script_dir = "/Users/maxsloof/Github/data_acq/dcgan_kaggle"
os.mkdir(new_dir)

# Download checkpoints from latest run
os.system(f"kaggle kernels pull maxsloof/{nt_type} -p {new_dir} -m")
os.system(f"kaggle kernels pull maxsloof/{nt_type} -p {script_dir} -m")
os.system(f"kaggle kernels output maxsloof/{nt_type} -p {new_dir}")