import os
import shutil


def organize_files(directory):
    # Dictionary to map file extensions to folder names
    extension_folders = {
        'images': ['jpg', 'jpeg', 'png', 'gif'],
        'documents': ['pdf', 'doc', 'docx', 'txt'],
        'videos': ['mp4', 'avi', 'mov'],
        'audio': ['mp3', 'wav'],
        'archives': ['zip', 'tar', 'gz'],
        'other': []  # For files with unrecognized extensions
    }

    # Create directories for each type
    for folder in extension_folders:
        path = os.path.join(directory, folder)
        if not os.path.exists(path):
            os.makedirs(path)

    # Process each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext[1:].lower()  # Remove the dot and convert to lowercase

        # Determine the folder to move the file to
        moved = False
        for folder, extensions in extension_folders.items():
            if ext in extensions:
                destination_folder = os.path.join(directory, folder)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                moved = True
                break

        # If the extension is not recognized, move to 'other'
        if not moved:
            shutil.move(file_path, os.path.join(directory, 'other', filename))

    print("Files have been organized.")


if __name__ == "__main__":
    # Set the directory you want to organize
    target_directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(target_directory)
