



import csv

# List of dictionaries 
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    {"Name": "Diana", "Age": 28, "City": "Houston"}
]

# Column headers
fields = ["Name", "Age", "City"]

# Write to CSV file
with open("peopleData.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()       # Write column names
    writer.writerows(data)     # Write data rows

print("CSV file 'people.csv' created successfully!")
