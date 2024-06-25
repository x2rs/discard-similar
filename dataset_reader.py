import json
with open("filled_dataset.json","r",encoding="utf-8") as f:
    raw_data = json.load(f)

with open("filtered_dataset.json","r",encoding="utf-8") as f:
    filtered_data = json.load(f)

print(len(raw_data))
print(len(filtered_data))