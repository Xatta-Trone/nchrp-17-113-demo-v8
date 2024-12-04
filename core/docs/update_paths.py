import os
import json

# Define the base directory (the current directory) where folders are located
base_dir = "."

# Load JSON data
with open("items.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find all PDFs in subdirectories and create a mapping of file names to formatted paths
pdf_paths = {}
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".pdf"):
            # Create a relative path with "docs/" prepended and convert backslashes to forward slashes
            relative_path = "docs/" + os.path.relpath(os.path.join(root, file), base_dir).replace("\\", "/")
            pdf_paths[file] = relative_path

# Update JSON data with the formatted paths
for item in data:
    pdf_name = item.get("pdf")
    if pdf_name in pdf_paths:
        item["pdf"] = pdf_paths[pdf_name]

# Save the updated JSON data
with open("items_updated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("PDF paths updated successfully in items.json.")
