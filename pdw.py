import json

def format_price(price_str):
    """Converts a 7-character price string to a formatted dollar value."""
    price = float(price_str) / 100  # Two decimals are implied
    return f"${price:.2f}"

def format_weight(weight_str):
    """Converts a 6-character weight string to a formatted pound value."""
    weight = float(weight_str) / 100  # Two decimals are implied
    return f"{weight:.2f} pounds"

def extract_data_from_file(file_path):
    extracted_data = {}

    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line in file:
            # Extract data based on the given positions
            ean = line[1:14].strip()  # 2-14 (13 characters)
            price = format_price(line[150:157].strip())  # Format price
            discount_level = line[165:168].strip()  # 166-168 (3 characters)
            weight = format_weight(line[238:244].strip())  # Format weight

            # Store the extracted data in the dictionary
            extracted_data[ean] = {
                "ean": ean,
                "price": price,
                "discount_level": discount_level,
                "weight": weight
            }

    return extracted_data

def save_to_json(data, output_file):
    # Write the extracted data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    file_path = '100KStockV2@ingram.dat'  # Input file
    output_file = 'output_data.json'  # Output JSON file

    # Extract the data
    extracted_data = extract_data_from_file(file_path)

    # Save to JSON
    save_to_json(extracted_data, output_file)

    print(f"Data extracted and saved to {output_file}")
