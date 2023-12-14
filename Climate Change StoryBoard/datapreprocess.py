import csv

data = [
    ["Decade", "Heatwave Season"],
    ["1960s", 25],
    ["1970s", 32],
    ["1980s", 38],
    ["1990s", 45],
    ["2000s", 51],
    ["2010s", 68]
]

# Define the filename for the CSV file
filename = "heatwave.csv"

# Write the data to the CSV file while specifying data types
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the column headers separately
    writer.writerow(data[0])
    
    # Write the data rows with proper data types
    for row in data[1:]:
        writer.writerow([str(row[0]), int(row[1])])

print("CSV file '{}' has been created.".format(filename))
