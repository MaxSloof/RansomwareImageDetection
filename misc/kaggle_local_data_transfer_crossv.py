import os
import kaggle
import time

# Command for Terminal - Copy underlying line #
# Windows line:
# cd C:\Users\Max\OneDrive - Erasmus University Rotterdam\Documents\GitHub\misc
# python kaggle_local_data_transfer_crossv.py

# MacOS line:
# python3 /Users/maxsloof/Github/data_acq/misc/kaggle_local_data_transfer_crossv.py

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
print("CrossV-CNN (0) / CrossV-CGAN-CNN  (1) / CrossV-DenseNet  (2) / CrossV-CGAN-DenseNet  (3) /") 
print("Malimg-CrossV-CNN (4) / Malimg-CrossV-CGAN-CNN (5) / Malimg-CrossV-DenseNet (6) / Malimg-CrossV-CGAN-DenseNet (7)")
userchoice = int(input("Enter number: "))
print("--------------")

# Determine the type of NN
if userchoice == 0:
    nt_type = "crossv-cnn"
    type_dir = "cross_validation"
    search_file = "crossv-cnn"

elif userchoice == 1:
    nt_type = "crossv-cgan-cnn"
    type_dir = "cross_validation"
    search_file = "crossv-cgan-cnn"
    
elif userchoice == 2:
    nt_type = "crossv-densenet"
    type_dir = "crossv_validation"
    search_file = "crossv-densenet"
    
elif userchoice == 3:
    nt_type = "crossv-cgan-densenet"
    type_dir = "malimg_dataset"
    search_file = "crossv-cgan-densenet"

elif userchoice == 4:
    nt_type = "malimg-crossv-cnn"
    type_dir = "malimg_dataset"
    search_file = "malimg-crossv-cnn"

elif userchoice == 5:
    nt_type = "malimg-crossv-cgan-cnn"
    type_dir = "malimg_dataset"
    search_file = "malimg-crossv-cgan-cnn"

elif userchoice == 6:
    nt_type = "malimg-crossv-densenet"
    type_dir = "malimg_dataset"
    search_file = "malimg-crossv-densenet"

elif userchoice == 7:
    nt_type = "malimg-crossv-cgan-densenet"
    type_dir = "malimg_dataset"
    search_file = "malimg-crossv-cgan-densenet"


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
    dir = f"C:/Users/Max/OneDrive - Erasmus University Rotterdam/Documents/GitHub/{type_dir}"
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
    new_dir = f"C:/Users/Max/OneDrive - Erasmus University Rotterdam/Documents/GitHub/{type_dir}/{nt_type}-v{vnum:03}"
if userchoiceOS == 1:
    new_dir = f"/Users/maxsloof/Github/data_acq/{type_dir}/{nt_type}-v{vnum:03}"

os.mkdir(new_dir)

# Download checkpoints from latest run
os.system(f"kaggle kernels pull maxsloof/{nt_type} -p {new_dir} -m")
os.system(f"kaggle kernels output maxsloof/{nt_type} -p {new_dir}")