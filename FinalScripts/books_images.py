import json

def append_image_url(input_file='books.json', output_file='books_with_images.json'):
    # Load the existing JSON data
    with open(input_file, 'r') as file:
        books = json.load(file)

    # Process each book entry
    for ean, book_data in books.items():
        # Generate the image URL using the EAN number
        image_url = f"https://storage.googleapis.com/paysfer_books/{ean}.jpg"
        
        # Add the imageURL key to the book entry
        book_data['productgroupimageurl1'] = image_url

    # Save the modified JSON data with image URLs
    with open(output_file, 'w') as file:
        json.dump(books, file, indent=4)

    print(f"Image URLs added. Check '{output_file}'.")

# Call the function
append_image_url()
