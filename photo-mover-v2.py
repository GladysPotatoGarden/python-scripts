import os
import shutil
import mimetypes
import sys
import logging
from datetime import datetime

# specify directories (Desktop, Documents, Downloads)
directories_to_search = [
    os.path.join(os.path.expanduser("~"), "Desktop"),
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Downloads")
]

# get default "Pictures" path
pictures_directory = os.path.join(os.path.expanduser("~"), "Pictures")

# check if the Pictures directory exists... if not, print an error and exit
if not os.path.exists(pictures_directory):
    print("Error: The default 'Pictures' directory does not exist.")
    sys.exit(1)  # exit w/ error code 1

# create directory for logging inside the Documents folder, and set this to the path for the log file
log_directory = os.path.join(os.path.expanduser("~"), "Documents", "python-script-logs")
os.makedirs(log_directory, exist_ok=True) 
log_file_path = os.path.join(log_directory, "file_move_log.log")

# log settings
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# start logger
logging.info("Starting file move process.")

# loop through each directory
for source_directory in directories_to_search:
    # ensure the source directory exists
    if not os.path.exists(source_directory):
        logging.warning(f"The directory '{source_directory}' does not exist. Skipping.")
        continue

    contents = os.listdir(source_directory)

    # loop through each item and only process image files
    for item in contents:
        item_path = os.path.join(source_directory, item)
        
        if os.path.isfile(item_path):
            # check mime type to verify if img file = true
            mime_type, _ = mimetypes.guess_type(item_path)
            if mime_type and mime_type.startswith("image"):
                # move img file
                destination_path = os.path.join(pictures_directory, item)
                
                # duplicate file handling, (adds _copy to duplicate files)
                if os.path.exists(destination_path):
                    base, extension = os.path.splitext(item)
                    destination_path = os.path.join(pictures_directory, f"{base}_copy{extension}")
                
                shutil.move(item_path, destination_path)
                print(f"Moved: {item} from {source_directory} to {pictures_directory}")

                # update log
                logging.info(f"Moved '{item}' from '{source_directory}' to '{destination_path}'")

logging.info("File move process completed.")
