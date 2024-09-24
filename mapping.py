import json

def merge_jsons(books_with_images_path, output_data_path, merged_output_path):
    # Load the JSON files
    with open(books_with_images_path, 'r') as books_file:
        books_data = json.load(books_file)

    with open(output_data_path, 'r') as output_file:
        output_data = json.load(output_file)

    # Merge the two JSONs based on the EAN
    for ean, output_info in output_data.items():
        if ean in books_data:
            # Add price, discount_level, and weight after publisher field
            books_data[ean]['price'] = output_info.get('price', '')
            books_data[ean]['discount_level'] = output_info.get('discount_level', '')
            books_data[ean]['weight'] = output_info.get('weight', '')
        else:
            # If the EAN from output_data.json is not in books_with_images.json, add the whole entry
            books_data[ean] = output_info

    # Save the merged data to a new JSON file
    with open(merged_output_path, 'w') as merged_file:
        json.dump(books_data, merged_file, indent=4)

if __name__ == "__main__":
    books_with_images_path = 'books_with_images.json'  # Path to books_with_images.json
    output_data_path = 'output_data.json'  # Path to output_data.json
    merged_output_path = 'merged_output.json'  # Path to the final merged output JSON

    # Merge the JSON files
    merge_jsons(books_with_images_path, output_data_path, merged_output_path)

    print(f"Merged data saved to {merged_output_path}")
