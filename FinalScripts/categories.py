import pandas as pd

val = 'childcategories'

# Specify the file paths
input_txt_file = val + '.txt'
output_excel_file = val + '.xlsx'

# Initialize an empty list to store the rows
data = []

# Read the text file
with open(input_txt_file, 'r') as file:
    for line in file:
        # Remove any leading/trailing whitespace and split the line by commas
        row = line.strip().split('","')
        # Remove the surrounding quotes
        row = [col.strip('"') for col in row]
        data.append(row)

# Convert the list to a pandas DataFrame
df = pd.DataFrame(data, columns=['Code', 'Description'])

# Save the DataFrame to an Excel file
df.to_excel(output_excel_file, index=False)

print(f"Excel file created: {output_excel_file}")
