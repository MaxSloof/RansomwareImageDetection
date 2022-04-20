import os
from re import search
import kaggle
import time

# Command for Terminal - Copy underlying line #
# Windows line:
# python C:/Users/Max/Documents/GitHub/misc/kaggle_local_data_transfer.py

# MacOS line:
# python3 /Users/maxsloof/Github/data_acq/misc/kaggle_local_data_transfer.py

# Ask whether you are on MacOS or Windows
print("\n")
print("What Operating System are you using?")
print("Windows (0) / MacOS (1)")
userchoiceOS = int(input("Enter number: "))
print("--------------")

if userchoiceOS == 0:
    from plyer import notification

# Ask what notebook you want to save the latest version of
print("What notebook do you want to save the latest version of?")
print("CNN (0) / DCGAN (1) / DCGAN-Classification (2) / ResNet (3) / DenseNet (4) / CGAN (5) / ResNet-CGAN (6) / DenseNet-CGAN (7) / Malimg-DenseNet-CGAN (8) / Malimg-DenseNet (9) / Malimg-cgan")
userchoice = int(input("Enter number: "))
print("--------------")

# Determine the type of NN
if userchoice == 0:
    nt_type = "cnn-kaggle"
    type_dir = "cnn"
    search_file = "cnn"

elif userchoice == 1:
    nt_type = "dcgan-kaggle"
    type_dir = "dcgan"
    search_file = "dcgan"
    
elif userchoice == 2:
    nt_type = "dcgan-classification-kaggle"
    type_dir = "dcgan_classification"
    search_file = "dcgan-classification"
    
elif userchoice == 3:
    nt_type = "ResNet-kaggle"
    type_dir = "ResNet"
    search_file = "ResNet"

elif userchoice == 4:
    nt_type = "DenseNet-kaggle"
    type_dir = "DenseNet"
    search_file = "DenseNet"

elif userchoice == 5:
    nt_type = "cgan-kaggle"
    type_dir = "conditional_gan"
    search_file = "cgan"

elif userchoice == 6:
    nt_type = "resnet-cgan-kaggle"
    type_dir = "ResNet"
    search_file = "ResNet"

elif userchoice == 7:
    nt_type = "DenseNet-cgan-kaggle"
    type_dir = "DenseNet"
    search_file = "DenseNet"

elif userchoice == 8:
    nt_type = "malimg-densenet-cgan"
    type_dir = "malimg_dataset"
    search_file = "DenseNet"

elif userchoice == 9:
    nt_type = "malimg-densenet"
    type_dir = "malimg_dataset"
    search_file = "DenseNet"

elif userchoice == 10:
    nt_type = 'malimg-cgan-ckpt'
    type_dir = 'malimg_dataset'
    search_file = 'cgan'


# Retrieve the notebook status from Kaggle
status = str(kaggle.api.kernel_status(user_name="maxsloof", kernel_slug=nt_type))

# Show progress in CMD / Terminal
while "queued" in status:
    print(f"{nt_type} notebook still queued")
    time.sleep(30)
    status = str(kaggle.api.kernel_status(user_name="maxsloof", kernel_slug= nt_type))
    
while "running" in status:
    print(f"{nt_type} notebook still running")
    time.sleep(30)
    status = str(kaggle.api.kernel_status(user_name="maxsloof", kernel_slug= nt_type))

# Show notification when notebook is complete / has encountered error
if "complete" in status:
    if userchoiceOS == 0:
        notification.notify(
            title=f"{nt_type} notebook has finished",
            message=f"The {nt_type} notebook has been completed on Kaggle. The output will now be saved to the a new folder in the GitHub directory.",
            timeout = 30
        )
    if userchoiceOS == 1:
        print("Notebook has been completed!")

if "error" in status:
    if userchoiceOS == 0:
        notification.notify(
            title=f"{nt_type} notebook encountered error",
            message=f"The {nt_type} notebook has encountered an error on Kaggle. The output will now be saved to the a new folder in the GitHub directory.",
            timeout = 30
        )
    if userchoiceOS == 1:
        print("Error has been encountered!")

# Set right directory based on OS
if userchoiceOS == 0:
    dir = f"C:/Users/Max/Documents/GitHub/{type_dir}"
if userchoiceOS == 1:
    dir = f"/Users/maxsloof/Github/data_acq/{type_dir}"

vnum = 0
# Find the latest version number
file_exists = []

for files in os.listdir(dir):
    filename = os.path.splitext(files)[0]
    try:
        vnum = max(vnum, int(filename[-3:]))
        file_exists.append(True)
    except:
        continue
else: 
    file_exists.append(False)

# If this is the first notebook you want to save, a new folder will be created with version #001
if sum(file_exists) == 0:
    vnum = 1
    print("No matches found")

else: 
    print(f"{sum(file_exists)} matches(es) found")
    print("--------------")
    vnum  = vnum + 1

# Print new folder name
print(f"New folder name: {nt_type}-v{vnum:03}")
print("--------------")

# Create new folder with the name of the notebook and the version number
if userchoiceOS == 0:
    new_dir = f"C:/Users/Max/Documents/GitHub/{type_dir}/{nt_type}-v{vnum:03}"
if userchoiceOS == 1:
    new_dir = f"/Users/maxsloof/Github/data_acq/{type_dir}/{nt_type}-v{vnum:03}"

os.mkdir(new_dir)

# Download checkpoints from latest run
os.system(f"kaggle kernels pull maxsloof/{nt_type} -p {new_dir} -m")
os.system(f"kaggle kernels output maxsloof/{nt_type} -p {new_dir}")