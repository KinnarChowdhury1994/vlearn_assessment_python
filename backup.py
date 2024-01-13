"""
Q4. In DevOps, performing regular backups of important files is crucial:

●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.
"""


import os,shutil,sys
from datetime import datetime

def backup(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Check if destination directory exists, create it if not
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Check if destination file already exists
            while os.path.exists(dest_path):
                # Append timestamp to the file name for uniqueness
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                base, ext = os.path.splitext(filename)
                filename = f"{base}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, filename)

            # Copy the file to the destination directory
            shutil.copy2(source_path, dest_path)
            print(f"Copied: {filename}")

        print("Backup completed successfully!")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    # Call the backup function with the provided directories
    backup(source_directory, destination_directory)
