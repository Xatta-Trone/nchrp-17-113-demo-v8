import os

# Supported image extensions
image_extensions = ['.jpg', '.jpeg', '.png',
                    '.bmp', '.gif', '.webp', '.tiff', '.jfif']

# Loop through files in the current directory
for filename in os.listdir():
    if os.path.isfile(filename):
        name, ext = os.path.splitext(filename)
        if ext.lower() in image_extensions:
            new_name = f"{name}.PNG"
            os.rename(filename, new_name)
            print(f"Renamed: {filename} → {new_name}")
