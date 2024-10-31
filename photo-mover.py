import os
import shutil
import mimetypes
import sys

# specify the source directory
source_directory = r"C:\Users\USERNAME\DIRECTORY"

# get the default Pictures path
pictures_directory = os.path.join(os.path.expanduser("~"), "Pictures")

# check if the Pictures directory exists, if it doesn't... print an error and abort
if not os.path.exists(pictures_directory):
    print("Error: The default 'Pictures' directory does not exist.")
    sys.exit(1)  # exit w/ error code 1

contents = os.listdir(source_directory)

for item in contents:
    item_path = os.path.join(source_directory, item)
    
    if os.path.isfile(item_path):
        # use mime to check if file is img
        mime_type, _ = mimetypes.guess_type(item_path)
        if mime_type and mime_type.startswith("image"):
            # move to Pictures system directory
            destination_path = os.path.join(pictures_directory, item)
            shutil.move(item_path, destination_path)
            print(f"Moved: {item} to {pictures_directory}")
