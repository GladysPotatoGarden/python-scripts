📂 Directory Explorer & 📸 Photo Mover v2
Organize and Manage Files Automatically with Simple, Efficient Scripts

Overview

Directory Explorer and Photo Mover v2 are two Python scripts designed to help you manage your files quickly and automatically:

    Directory Explorer: A minimalistic script for viewing files in a clean, text-based format and sorting them by size.
    Photo Mover v2: An automation script that organizes image files by moving them from common directories (e.g., Desktop, Documents, Downloads) to the default Pictures folder at every startup, while keeping a log of each action.

    "Life is short, have fun while u can!"
    — Made by GladysPotatoGarden (Quincy)

Directory Explorer
Features

    Text-Based Display: View files in a straightforward, organized display within your terminal, removing the need for a complex user interface.
    Sorting by File Size: Sorts files by size for easy comparison and navigation.

Usage

    Configure Directory Path: Add the desired directory path to the variable at the top of the script.
    Run the Script: Execute the script to view files and their sizes in a simple, organized output.

Photo Mover v2
Features

    Automatic Image Organization: Scans Desktop, Documents, and Downloads folders at startup, moving all image files to the Pictures directory.
    Auto-Generated Log: Creates a log file in a folder called python-script-logs within Documents, recording each file moved with timestamps for reference.

Setup Instructions

    Edit Directory Paths (Optional): You can adjust the folder paths in the script to customize which directories are scanned.
    Build with PyInstaller: Create an executable with:

    bash

    python -m pip install pyinstaller
    pyinstaller --onefile photo-mover-v2.py

    Add to Startup: Place the executable (or a shortcut) in the system’s startup folder so it runs every time the computer boots.
        On Windows, open the Startup folder by pressing Win + R and typing shell:startup. Place the shortcut to your executable here.

Future Enhancements

Documentation will soon include additional configuration options and usage examples.
Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Contributions for enhanced functionality or additional scripts are welcome!
License

This project is licensed under the MIT License. See the LICENSE file for details.

Author:

GladysPotatoGarden (Quincy)

Have questions or suggestions? Reach out via GitHub or submit an issue for further improvements!
