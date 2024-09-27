import pandas as pd
import re

# Function to read the text file and split based on multiple spaces
def txt_to_excel(input_txt_file, output_excel_file):
    with open(input_txt_file, 'r') as file:
        lines = file.readlines()
    
    data = []
    
    for line in lines:
        # Use regex to split by multiple spaces
        split_line = re.split(r'\s{2,}', line.strip())
        data.append(split_line)
    
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to an Excel file
    df.to_excel(output_excel_file, index=False)

# Example usage:
txt_to_excel('100KTtlingv2.txt', 'output.xlsx')
