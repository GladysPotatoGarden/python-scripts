# python-scripts
 

Directory Explorer and Photo Mover v2 Scripts
Overview

This repository contains two Python scripts:

    File Viewer: A lightweight tool for viewing and organizing files in a text-based format.
    Photo Mover v2: An automated script that organizes image files by moving them to the default Pictures directory and logs actions for easy tracking.

Directory Explorer
Description

The Directory Explorer script allows users to view files in a clean and organized display without a graphical user interface. You simply specify the directory path at the top of the script, and it will display all files in that directory in an ordered, readable format.
Features

    Simple Text-Based Display: View files in an uncluttered, text-based format.
    Sort by File Size: Files are automatically sorted by size for better organization.

    "Life is short, have fun while able to do so!"
    — Made by GladysPotatoGarden (Quincy)

Photo Mover v2
Description

The Photo Mover v2 script is an automated tool designed to keep your Pictures directory organized by regularly moving image files from commonly cluttered folders to Pictures. This script is designed to run at startup and operates seamlessly in the background.
How It Works

    Folder Scanning: Each time the script runs, it checks the Desktop, Documents, and Downloads folders.
    Image Organization: All image files found are moved to the Pictures directory by default.
    Automatic Logging: Creates a log file in the Documents/python-script-logs folder, tracking all processed files with timestamps for easy reference.

Setup Instructions

    Edit Directory Path: If necessary, adjust the directory paths within the script to suit your preferences.
    Build with PyInstaller: To create an executable version, build the script using PyInstaller.
    Add to Startup: Place the executable or a shortcut to it in your system’s startup folder to ensure it runs automatically at each boot.

Future Enhancements

Documentation for the Photo Mover v2 will be expanded soon to cover additional configuration options.

Enjoy the simplicity and functionality! 😊
