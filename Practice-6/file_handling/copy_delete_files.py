import shutil
import os

# Copy sample_data.txt as a backup
shutil.copy("sample_data.txt", "sample_data_backup.txt")

print("Backup created successfully!") # Append new lines and verify content


file_name = "sample_data_backup.txt"

# Check if file exists before deleting
if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted successfully!")
else:
    print("File does not exist.")
