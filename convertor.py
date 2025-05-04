import os

def convert_file_extensions(directory, from_extension, to_extension):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if the file has the source extension (case-insensitive)
            base, ext = os.path.splitext(filename)
            if ext.lower() == from_extension.lower():
                old_file = os.path.join(root, filename)
                new_filename = base + to_extension  # Preserve the base name
                new_file = os.path.join(root, new_filename)

                try:
                    # Rename (convert) the file extension
                    os.rename(old_file, new_file)
                    print(f"✅ Converted '{filename}' to '{new_filename}'")
                except Exception as e:
                    print(f"❌ Failed to rename '{filename}': {e}")

# Example usage
folder_path = r'D:\Private\Private\New folder\picutre'  # Replace with your folder path
source_extension = '.webp'   # Source extension
target_extension = '.png'   # Target extension

convert_file_extensions(folder_path, source_extension, target_extension)
import os

def convert_file_extensions(directory, from_extension, to_extension):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if the file has the source extension (case-insensitive)
            base, ext = os.path.splitext(filename)
            if ext.lower() == from_extension.lower():
                old_file = os.path.join(root, filename)
                new_filename = base + to_extension  # Preserve the base name
                new_file = os.path.join(root, new_filename)

                try:
                    # Rename (convert) the file extension
                    os.rename(old_file, new_file)
                    print(f"✅ Converted '{filename}' to '{new_filename}'")
                except Exception as e:
                    print(f"❌ Failed to rename '{filename}': {e}")

# Example usage
folder_path = 'D:/Picutre'  # Replace with your folder path
source_extension = '.webp'   # Source extension
target_extension = '.png'   # Target extension

convert_file_extensions(folder_path, source_extension, target_extension)
