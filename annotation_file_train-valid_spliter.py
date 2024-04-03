
""" 
Prompt:
write me python code to copy files from source folder to destination folder as follow conditions
1. File type is '.txt' in the source folder
2. File name is found in the destination folder which its type is '.jpg' 

claude-3-sonnet-20240229: 
Here's a Python script that copies text files from a source folder to a destination folder, 
but only if the file name (without the extension) exists in the destination folder with a .jpg extension:
------------------------------------------
import os
import shutil

# Set the source and destination folder paths
source_folder = "/path/to/source/folder"
dest_folder = "/path/to/destination/folder"

# Iterate over files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        # Get the file name without the extension
        base_name = os.path.splitext(filename)[0]
        
        # Check if a file with the same name and .jpg extension exists in the destination folder
        jpg_file = os.path.join(dest_folder, f"{base_name}.jpg")
        if os.path.isfile(jpg_file):
            # Copy the text file to the destination folder
            src_file = os.path.join(source_folder, filename)
            dest_file = os.path.join(dest_folder, filename)
            shutil.copy2(src_file, dest_file)
            print(f"Copied {filename} to {dest_folder}")

-------------------------------------------------            
Here's how the script works:

1 Import the necessary modules: os for interacting with the file system, and shutil for copying files.
2 Set the source and destination folder paths.
3 Iterate over files in the source folder using os.listdir(source_folder).
4 Check if the file is a text file by checking if its name ends with .txt.
5 Get the base name of the file (without the extension) using os.path.splitext(filename)[0].
6 Check if a file with the same base name and .jpg extension exists in the destination folder using os.path.isfile(jpg_file).
7 If the corresponding .jpg file exists, copy the text file to the destination folder using shutil.copy2(src_file, dest_file).
8 Print a message indicating that the file was copied.
"""

import os
import shutil

# Set the source and destination folder paths
source_folder = "recc_vlog2_v2/anotation"
dest_folder = "recc_vlog2_v2/valid"

# Iterate over files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        # Get the file name without the extension
        base_name = os.path.splitext(filename)[0]
        
        # Check if a file with the same name and .jpg extension exists in the destination folder
        jpg_file = os.path.join(dest_folder, f"{base_name}.jpg")
        if os.path.isfile(jpg_file):
            # Copy the text file to the destination folder
            src_file = os.path.join(source_folder, filename)
            dest_file = os.path.join(dest_folder, filename)
            shutil.copy2(src_file, dest_file)
            print(f"Copied {filename} to {dest_folder}")