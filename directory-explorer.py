#--------------------------------------------------------------------------------------------------------------------------

# This program lists all files in a specified directory, displaying each file's name, type, size, and creation date.
# It performs the following steps:
# 1. Reads all items in the specified directory and filters out only files.
# 2. Determines the MIME type of each file using the `mimetypes` library to identify the file type.
# 3. Retrieves the file size in kilobytes (KB) and the creation date, formatting them for readability.
# 4. Sorts the files by size in descending order (from largest to smallest).
# 5. Outputs the file information in a neatly formatted table with columns for the file name, type, size, and creation date.

#*----------* Made by GladysPotatoGarden (Quincy Z.) *----------*-----------------------------------------------------------

import os
import mimetypes
from datetime import datetime

# set path
# this is where you will set the path variable that you want the program to explore. 
# for example you could use "C:\Users\Gladys\Documents"

directory_path = r"C:\Users\USERNAME\DIRECTORY"

file_info_list = []

contents = os.listdir(directory_path)

for item in contents:
    item_path = os.path.join(directory_path, item)
    
    if os.path.isfile(item_path):
        # use mimetypes to guess the file type
        mime_type, _ = mimetypes.guess_type(item_path)
        file_type = mime_type if mime_type else "Unknown"
        
        # get the file size in KB
        file_size = os.path.getsize(item_path) / 1024 
        
        # get file creation date and format it
        creation_time = os.path.getctime(item_path)
        creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # append the information to the list as a tuple
        file_info_list.append((item, file_type, file_size, creation_date))

# sorting
file_info_list = sorted(file_info_list, key=lambda x: x[2], reverse=True)

# format
header = f"| {'File Name':<40} | {'File Type':<30} | {'Size (KB)':<10} | {'Date Created':<20} |"
divider = "-" * len(header)

print(divider)
print(header)
print(divider)
for file_name, file_type, file_size, creation_date in file_info_list:
    print(f"| {file_name:<40} | {file_type:<30} | {file_size:<10.2f} | {creation_date:<20} |")
print(divider)
