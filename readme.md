# 🔁 File Extension Converter

This Python script allows you to **bulk rename file extensions** within a specified folder and its subfolders. It's especially useful when you have a large number of files with the wrong or undesired extension (e.g., `.webp` to `.png`), and you want to fix them without converting the actual file data.

---

## 📂 Features

- Recursively processes all files in subdirectories
- Renames files with a given source extension to a new target extension
- Case-insensitive extension matching (e.g., `.WEBP` and `.webp` are treated the same)
- Logs success and error messages to the console

---

## ✅ Requirements

- Python 3.x
- No external libraries required

---

## 🚀 Usage

1. Open the script file.
2. Modify the example usage section at the bottom:
   ```python
   folder_path = 'D:/Picutre'          # Path to the folder containing the files
   source_extension = '.webp'          # Current file extension
   target_extension = '.png'           # Desired file extension


# How to Run
    python convert_file_extensions.py
