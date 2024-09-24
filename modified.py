import json

def modify_bisac_in_json(input_file='books.json', output_file='books_modified.json'):
    # Load the existing JSON data
    with open(input_file, 'r') as file:
        books = json.load(file)

    # Process each book entry
    for ean, book_data in books.items():
        # Extract the bisac array
        bisac_codes = book_data.get('bisac', [])
        
        if bisac_codes:
            # Keep only the first BISAC code in the main bisac array
            primary_bisac = bisac_codes[0]
            book_data['bisac'] = [primary_bisac]
            
            # Move the remaining BISAC codes to the description
            remaining_bisac = bisac_codes[1:]
            if remaining_bisac:
                if 'description' not in book_data:
                    book_data['description'] = {}
                book_data['description']['bisac'] = remaining_bisac

    # Save the modified JSON data
    with open(output_file, 'w') as file:
        json.dump(books, file, indent=4)

    print(f"Modification complete. Check '{output_file}'.")

# Call the function
modify_bisac_in_json()
