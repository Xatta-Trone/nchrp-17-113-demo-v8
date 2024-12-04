import json

# Load JSON data
with open("items_shortened.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create a mapping from `pdf` to `pdf1` paths for quick lookup
pdf_map = {item["pdf"].split('/')[-1]: item["pdf1"] for item in data if "pdf1" in item}

# Update `related_measures` links
for item in data:
    if "related_measures" in item:
        for measure in item["related_measures"]:
            link_filename = measure["link"]
            # Update `link` with `pdf1` path if match is found in pdf_map
            if link_filename in pdf_map:
                measure["link"] = pdf_map[link_filename]

# Save the updated JSON data
with open("items_updated_links.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated related_measures links with pdf1 paths where applicable.")
