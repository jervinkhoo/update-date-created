import os
import datetime

# Set the path of the subfolder whose subfolders' creation date needs to be updated
subfolder_path = "M:\\"

# Set the new creation date and time for the subfolders (year, month, day, hour, minute, second)
new_creation_time = datetime.datetime(2023, 2, 24, 12, 0, 0)

# Loop through all subfolders in the subfolder and update their creation time
for folder_name in os.listdir(subfolder_path):
    folder_path = os.path.join(subfolder_path, folder_name)
    if os.path.isdir(folder_path):
        os.utime(folder_path, (new_creation_time.timestamp(), new_creation_time.timestamp()))