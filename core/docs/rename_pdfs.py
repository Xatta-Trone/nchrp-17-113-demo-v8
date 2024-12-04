import os
import json
import shutil

# Define the base directory (excluding the initial "docs" part)
base_dir = "."

# Load the JSON data
with open("items_updated.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Process each item in JSON data
for item in data:
    pdf_path = item.get("pdf")
    if pdf_path:
        # Construct the full path (excluding the initial "docs/" part)
        full_path = os.path.join(base_dir, pdf_path[5:])
        
        if os.path.exists(full_path):
            # Generate new filename with the first 20 characters of the original name
            dir_path, original_filename = os.path.split(full_path)
            new_filename = original_filename[:20] + ".pdf"
            new_full_path = os.path.join(dir_path, new_filename)
            
            # Rename the file
            shutil.move(full_path, new_full_path)
            
            # Update JSON item with the new path and add "pdf1" key
            item["pdf1"] = "docs/" + os.path.relpath(new_full_path, base_dir).replace("\\", "/")
        else:
            print(f"File not found: {full_path}")

# Save the updated JSON data
with open("items_shortened.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("PDFs renamed and JSON updated successfully.")
